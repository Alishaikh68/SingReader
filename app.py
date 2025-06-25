from flask import Flask, render_template, Response, jsonify, make_response, request, send_from_directory, redirect, url_for, session
import cv2
import pickle
import numpy as np
import mediapipe as mp
import time
from db import get_db_connection, init_user_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize database
init_user_db()

# Load model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

mdl_dict = pickle.load(open('./modelind.p', 'rb'))
mdl = mdl_dict['model']

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3)

mp_hnd = mp.solutions.hands
hnds = mp_hnd.Hands(static_image_mode=False, min_detection_confidence=0.3)

# Video capture variables
cap = None
video_active = False
detected_text = ""
last_detected_char = ""
last_update_time = 0
min_time_gap = 1

cap = None
vid_active = False
det_txt = ""
last_char = ""
last_upd_time = 0
min_gap = 1


labels_dict = {
    0: '0', 10: 'A', 1: '1', 11: 'B', 2: '2', 12: 'C', 3: '3', 13: 'D',
    4: '4', 14: 'E', 5: '5', 15: 'F', 6: '6', 16: 'G', 7: '7', 17: 'H',
    8: '8', 18: 'I', 9: '9', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N',
    24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V',
    32: 'W', 33: 'X', 34: 'Y', 35: 'Z',
}

lbl_dict = {
    0: '0', 10: 'A', 1: '1', 11: 'B', 2: '2', 12: 'C', 3: '3', 13: 'D',
    4: '4', 14: 'E', 5: '5', 15: 'F', 6: '6', 16: 'G', 7: '7', 17: 'H',
    8: '8', 18: 'I', 9: '9', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N',
    24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V',
    32: 'W', 33: 'X', 34: 'Y', 35: 'Z',
}

# Route: Public Home
@app.route('/')
def index():
    return render_template('home.html')

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            return redirect(url_for('home'))
        else:
            error = 'Incorrect username or password. Please try again.'

    return render_template('login.html', error=error)

# Route: Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        existing_user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if existing_user:
            error = 'Username already taken. Please choose another.'
        else:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))

        conn.close()

    return render_template('register.html', error=error)


# Route: Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Route: Protected Page
@app.route('/second_page') 
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('inde.html')

@app.route('/how_it_Works')
def How_it_Works():
    return render_template('how_it_Works.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/explore')
def explore():
    return render_template('Explore.html') 

@app.route('/ASL')
def ASL():
    return render_template('ASl.html')

@app.route('/ISL')
def ISL():
    return render_template('ISl.html')


# Video stream generation
def gen_frames():
    global video_active, cap, detected_text, last_detected_char, last_update_time
    while video_active:
        if cap is None or not cap.isOpened():
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FPS, 30)

        success, frame = cap.read()
        if not success:
            continue

        H, W, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        data_aux = []
        x_, y_ = [], []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

                wrist_x, wrist_y = hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y
                index_x, index_y = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y
                distance_wrist_index = np.sqrt((index_x - wrist_x) ** 2 + (index_y - wrist_y) ** 2)
                data_aux.append(distance_wrist_index)

            if len(data_aux) < 84:
                data_aux.extend([0] * (84 - len(data_aux)))
            elif len(data_aux) > 84:
                data_aux = data_aux[:84]

            prediction = model.predict([np.asarray(data_aux)])
            predicted_character = labels_dict.get(int(prediction[0]), "Unknown")

            current_time = time.time()
            if predicted_character != last_detected_char and predicted_character != "Unknown":
                if current_time - last_update_time > min_time_gap:
                    last_detected_char = predicted_character
                    detected_text += predicted_character
                    last_update_time = current_time
            elif predicted_character != last_detected_char:
                last_detected_char = predicted_character

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 4)
            cv2.putText(frame, predicted_character, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 15), 3, cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_frms():
    global vid_active, cap, det_txt, last_char, last_upd_time
    while vid_active:
        if cap is None or not cap.isOpened():
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FPS, 30)

        success, frm = cap.read()
        if not success:
            continue

        H, W, _ = frm.shape
        frm_rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
        res = hnds.process(frm_rgb)
        data = []
        x_, y_ = [], []

        if res.multi_hand_landmarks:
            for hand in res.multi_hand_landmarks:
                for i in range(len(hand.landmark)):
                    x = hand.landmark[i].x
                    y = hand.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand.landmark)):
                    x = hand.landmark[i].x
                    y = hand.landmark[i].y
                    data.append(x - min(x_))
                    data.append(y - min(y_))

                wrist_x, wrist_y = hand.landmark[0].x, hand.landmark[0].y
                index_x, index_y = hand.landmark[8].x, hand.landmark[8].y
                dist_wrist_index = np.sqrt((index_x - wrist_x) ** 2 + (index_y - wrist_y) ** 2)
                data.append(dist_wrist_index)

            if len(data) < 84:
                data.extend([0] * (84 - len(data)))
            elif len(data) > 84:
                data = data[:84]

            pred = mdl.predict([np.asarray(data)])
            pred_char = lbl_dict.get(int(pred[0]), "Unknown")

            curr_time = time.time()
            if pred_char != last_char and pred_char != "Unknown":
                if curr_time - last_upd_time > min_gap:
                    last_char = pred_char
                    det_txt += pred_char
                    last_upd_time = curr_time
            elif pred_char != last_char:
                last_char = pred_char

            # Draw bounding box and prediction
            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10
            x2 = int(max(x_) * W) + 10
            y2 = int(max(y_) * H) + 10

            cv2.rectangle(frm, (x1, y1), (x2, y2), (255, 255, 255), 4)
            cv2.putText(frm, pred_char, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 15), 3, cv2.LINE_AA)

        ret, buff = cv2.imencode('.jpg', frm)
        frm = buff.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frm + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    global cap, video_active
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if not video_active:
        video_active = True
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 30)
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feedind')
def vid_feed():
    global cap, vid_active
    if not vid_active:
        vid_active = True
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 30)
    return Response(gen_frms(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_video')
def stop_video():
    global cap, video_active
    video_active = False
    if cap:
        cap.release()
        cap = None
    return "Video Feed Stopped"

@app.route('/stop_videoind')
def stop_vid():
    global cap, vid_active
    vid_active = False
    if cap:
        cap.release()
        cap = None
    return "Video Feed Stopped"


@app.route('/start_video')
def start_video():
    global cap, video_active, detected_text, last_detected_char, last_update_time
    if not video_active:
        video_active = True
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 30)
        detected_text = ""
        last_detected_char = ""
        last_update_time = 0
    return "Video Feed Started"

@app.route('/start_videoind')
def start_vid():
    global cap, vid_active, det_txt, last_char, last_upd_time
    if not vid_active:
        vid_active = True
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 30)
        det_txt = ""
        last_char = ""
        last_upd_time = 0
    return "Video Feed Started"


@app.route('/get_detected_text')
def get_detected_text():
    global detected_text
    if request.args.get('reset') == 'true':
        detected_text = ""
    response = make_response(jsonify({'detected_text': detected_text}))
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/get_detected_textind')
def get_det_txt():
    global det_txt
    if request.args.get('reset') == 'true':
        det_txt = ""
    resp = make_response(jsonify({'detected_text': det_txt}))
    resp.headers['Cache-Control'] = 'no-cache'
    return resp

@app.route('/clear_detected_text')
def clear_detected_text():
    global detected_text
    detected_text = ""
    return "Detected text cleared"

@app.route('/clear_detected_textind')
def clear_det_txt():
    global det_txt
    det_txt = ""
    return "Detected text cleared"

@app.route('/flutter')
def flutter_app():
    return send_from_directory('static/flutter', 'index.html')

@app.route('/flutter/<path:filename>')
def flutter_files(filename):
    return send_from_directory('static/flutter', filename)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
