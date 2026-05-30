# RWB Renk Takibi — GitHub Pages'e Yükleme

Bu klasördeki dosyalar hazır bir web sitesi. GitHub Pages'e koyunca herkese tek link
atarsın, telefonda açıp "Ana ekrana ekle" deyince app gibi durur.

## Klasördeki dosyalar
- `index.html` — sayfanın kendisi
- `manifest.webmanifest` — "ana ekrana ekle" ayarları
- `sw.js` — internet yokken bile çalışması için
- `icon-192.png`, `icon-512.png` — uygulama ikonu

> Not: Senin GitHub hesabına benim erişimim yok, o yüzden yüklemeyi sen yapacaksın.
> Tarayıcıdan, komut satırı olmadan, sürükle-bırakla halledebilirsin. Adımlar aşağıda.

---

## Adım adım (tarayıcıdan, 5 dakika)

1. **github.com**'a gir, sağ üstten **+ → New repository**.
2. **Repository name:** `rwb-renk` yaz. **Public** seç. **Create repository**.
3. Açılan sayfada **"uploading an existing file"** linkine tıkla
   (yoksa: **Add file → Upload files**).
4. Bu klasörün **içindeki tüm dosyaları** (index.html, manifest.webmanifest, sw.js,
   icon-192.png, icon-512.png) sürükleyip bırak. **Commit changes**'e bas.
5. Üst menüden **Settings → Pages**'e gir.
6. **Build and deployment → Source:** "Deploy from a branch" seç.
   **Branch:** `main`, klasör `/ (root)`. **Save**.
7. 1-2 dakika bekle, sayfayı yenile. Üstte yeşil kutuda linkin çıkar:
   `https://KULLANICIADIN.github.io/rwb-renk/`

Bu linki arkadaşlarına at. Hepsi açabilir.

---

## Telefonda "app" gibi yapmak
- **iPhone (Safari):** linki aç → Paylaş ikonu → **Ana Ekrana Ekle**.
- **Android (Chrome):** linki aç → sağ üst üç nokta → **Ana ekrana ekle / Uygulamayı yükle**.

İkon ana ekrana düşer, tıklayınca tam ekran açılır — normal app'ten farkı olmaz.

---

## İleride güncelleme
Renk sırası veya indirim mantığı değişirse `index.html`'i değiştirip aynı repoya
tekrar yüklemen yeterli. (`sw.js` içindeki `rwb-renk-v1` yazısını `v2` yaparsan
herkeste anında güncellenir.)
