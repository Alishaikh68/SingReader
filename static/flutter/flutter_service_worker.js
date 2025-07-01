'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"assets/AssetManifest.bin": "ae77101d5dbdac9894a74323669a1b6a",
"assets/AssetManifest.bin.json": "199b92096aaa3537da4444a36ee5cae9",
"assets/AssetManifest.json": "b9b4af5f1fad01c4ced796087260d787",
"assets/assets/ISL_Gifs/good.gif": "1a72249232768df68d4f6890a878c270",
"assets/assets/ISL_Gifs/hello.gif": "64e7fcaf718eea3f969426d975fa455a",
"assets/assets/ISL_Gifs/morning.gif": "39eb8aa8a0bcfe780980ea65f4206d5e",
"assets/assets/ISL_Gifs/you.gif": "759daabb76a71f7b9772a7ac581fdb69",
"assets/assets/letters/0.png": "16cb9018d3063cc233c098d6752044d7",
"assets/assets/letters/1.png": "eef7bf592cafae8cc456f74a9f13fc15",
"assets/assets/letters/2.png": "e5c7c158f856047ac75aee0f36f50665",
"assets/assets/letters/3.png": "17d939ed4497891ef8a8736ea84b80f9",
"assets/assets/letters/4.png": "635573eec502e287f05a53e38f92d09d",
"assets/assets/letters/5.png": "b7415fe9ca04b2413c0711a7fd2418bf",
"assets/assets/letters/6.png": "4684aa7b3871cbf23ba8588f5fa241e4",
"assets/assets/letters/7.png": "4a142c052d1de939e95601eb44a22d50",
"assets/assets/letters/8.png": "59d0fb72318364a8d00eabcc782279ef",
"assets/assets/letters/9.png": "728a4907d4c5a3b2ca0a65ae1208839b",
"assets/assets/letters/a.png": "94298b6d7f07c29381739f285102b496",
"assets/assets/letters/b.png": "925bdd050d469f1bc02ef8ce0b61a626",
"assets/assets/letters/c.png": "95f332b5f782f6e3ec07bd5e9bb1a44c",
"assets/assets/letters/d.png": "8d62099773beb606fb817f5c8165cb7f",
"assets/assets/letters/e.png": "9941bffa4a8fc5a812051ad9ad30e874",
"assets/assets/letters/f.png": "c5cc505c01662448db4d7c510d1e3cc3",
"assets/assets/letters/g.png": "46dbfcdb276c76d1365fc61384b73a39",
"assets/assets/letters/h.png": "fa60e1ddd496fb9619c1654f503a7b90",
"assets/assets/letters/i.png": "ec7fce84d50e853e25a2e66024052827",
"assets/assets/letters/j.png": "dee6491c9062b061d2de39e315acd8cf",
"assets/assets/letters/k.png": "582f4ea9222a71cc7a67bc9ff644d9a5",
"assets/assets/letters/l.png": "9361d390b8fd31ebac7578e70ffc9c5e",
"assets/assets/letters/m.png": "edfeabff7f17f8772da1b55dc0da084e",
"assets/assets/letters/n.png": "2d0d023cc04fa5eee6f47b13b3db37e5",
"assets/assets/letters/o.png": "edb5f2063a1d70e654a5ae715572bce5",
"assets/assets/letters/p.png": "5d841947c759297c574b1727e0f66547",
"assets/assets/letters/q.png": "f58e1a02b1c132abef882d18e0a8a3ba",
"assets/assets/letters/r.png": "4bf6595352820d6ac64dba5f260e6b83",
"assets/assets/letters/s.png": "349888264738ed009ab89ee49886fbe8",
"assets/assets/letters/space.png": "c9dfc1411615c97d8cd454a9e6667740",
"assets/assets/letters/t.png": "21274f438825a861a70894c6328fe99e",
"assets/assets/letters/u.png": "3efa410c1d10684d50aac8d962272b87",
"assets/assets/letters/v.png": "0e92b6a10de5b56a810841a40712c79b",
"assets/assets/letters/w.png": "f099f9828b8e2f45fbe8e3ad8c3c78be",
"assets/assets/letters/x.png": "d087fdcc7c8994f876976e3c0a5047a3",
"assets/assets/letters/y.png": "3c24ce0a8af505fe7af6224169c3400f",
"assets/assets/letters/z.png": "14318111fb65b8b4ff6b68038c958cc7",
"assets/assets/logo/sanket_icon.png": "735305433c5260fd394ff772cf79af1f",
"assets/assets/logo/sanket_splash.png": "2f289d8dae9d15319d67c0ddbf9dd38b",
"assets/FontManifest.json": "dc3d03800ccca4601324923c0b1d6d57",
"assets/fonts/MaterialIcons-Regular.otf": "a3e9854b67536d7a6e9f65caff08b925",
"assets/NOTICES": "204825671ec7ccdcf715646d3c14e37d",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "33b7d9392238c04c131b6ce224e13711",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"canvaskit/canvaskit.js": "86e461cf471c1640fd2b461ece4589df",
"canvaskit/canvaskit.js.symbols": "68eb703b9a609baef8ee0e413b442f33",
"canvaskit/canvaskit.wasm": "efeeba7dcc952dae57870d4df3111fad",
"canvaskit/chromium/canvaskit.js": "34beda9f39eb7d992d46125ca868dc61",
"canvaskit/chromium/canvaskit.js.symbols": "5a23598a2a8efd18ec3b60de5d28af8f",
"canvaskit/chromium/canvaskit.wasm": "64a386c87532ae52ae041d18a32a3635",
"canvaskit/skwasm.js": "f2ad9363618c5f62e813740099a80e63",
"canvaskit/skwasm.js.symbols": "80806576fa1056b43dd6d0b445b4b6f7",
"canvaskit/skwasm.wasm": "f0dfd99007f989368db17c9abeed5a49",
"canvaskit/skwasm_st.js": "d1326ceef381ad382ab492ba5d96f04d",
"canvaskit/skwasm_st.js.symbols": "c7e7aac7cd8b612defd62b43e3050bdd",
"canvaskit/skwasm_st.wasm": "56c3973560dfcbf28ce47cebe40f3206",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"flutter.js": "76f08d47ff9f5715220992f993002504",
"flutter_bootstrap.js": "fd2c983528809f183d5c201f488f7269",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"index.html": "c168ac261083a39b35b6893da9139062",
"/": "c168ac261083a39b35b6893da9139062",
"main.dart.js": "bf8d1f58ae686fee2c62cf9dac59a176",
"manifest.json": "6f4ee7c09ce92a7fda07979cf2c5c0f7",
"version.json": "a30602f7c2fa9c1406f44546e0584a0b"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
