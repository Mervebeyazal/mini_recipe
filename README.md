# SE Primer · YZM301 — Yazılım Test ve Gerçekleme

**Etkileşimli mühendislik karar simülasyonu.** Sağlık randevu sistemi arızasında üç karar (mimari, test, KVKK), iki son, rol/seviye/hedef uyarlaması, her karardan sonra teknik açıklama ve cevap vermeyen Sokratik tutor.

> **Durum (30.10.2026):** Kod ve bağımlılıksız demo hazır. Gerçek Chromium davranış testi: 8/8 karar yolu ve 2 ek kontrol **geçti**. Kural tabanlı tutor: 20/20 senaryoda tanımlı cevap sızdırma kalıbı görülmedi. **Cypress çalıştırılması / Google Stitch projesi / Google AI Studio yayını henüz doğrulanmadı.** Bu ayrım teslim kanıtları için önemlidir.

## Hızlı çalıştırma

Node veya npm **gerekmez**. `index.html` ES modules kullandığı için yerel HTTP sunucu üzerinden açın:

```bash
python3 -m http.server 5173
```

Tarayıcı: http://localhost:5173 (telefon ile aynı ağda makinenin IP'si üzerinden açılabilir; ağ kuralları geçerli). `index.html` dosyasını doğrudan `file://` ile açmak ES module kısıtlarına takılabilir.

## Değerlendirme / test komutları

```bash
node tests/tutor-eval.mjs  # 20 gerçek kural tabanlı tutor yanıtını ve oranı üretir
npm install                # yalnızca Cypress testleri için, ağ bağlantısı gerekir
npm run test:e2e           # başka terminalde sunucu açıkken
```

Cypress testleri `cypress/e2e/primer.cy.js` dosyasında 8 karar yolunu ve kritik davranışları kapsar. `cypress.config.js` test videosunu açar. CI iş akışı `.github/workflows/ci.yml` içindedir. **Cypress geçti iddiası ancak CI çıktısı veya yerel test koşusu alındıktan sonra kurulabilir.**

## Kanıtlar

- Spesifikasyon, kapsam, 5 kabul örneği ve akış: [`spec.md`](spec.md)
- Üç mobil ekran, tasarım ilkeleri ve Stitch aktarım promptu: [`DESIGN.md`](DESIGN.md), [`docs/STITCH_BRIEF.md`](docs/STITCH_BRIEF.md)
- Tutor 20 gerçek çıktı, hata sınıfları, oran: [`docs/tutor-eval.md`](docs/tutor-eval.md)
- Gerçek tarayıcı kontrol senaryoları: [`tests_browser.py`](tests_browser.py), [`evidence/browser-checks.json`](evidence/browser-checks.json)
- Üç mobil ekran görüntüsü: [`design/01-intro.jpg`](design/01-intro.jpg), [`design/02-scene.jpg`](design/02-scene.jpg), [`design/03-ending.jpg`](design/03-ending.jpg)
- Google AI Studio'ya aktarım açıklaması: [`docs/AI_STUDIO_BRIEF.md`](docs/AI_STUDIO_BRIEF.md)
- 60 saniyelik oynanış video dosyası: teslim ZIP'i içinde `SE_Primer_60s_Demo.mp4` olarak ayrıca verilir. Bu **Cypress koşusu kaydı değil**, gerçek tarayıcı ekranlarından oluşturulan açıklamalı ürün demosudur.

## Ürün kararı: kapsam dışı üç özellik

1. **Kullanıcı hesabı eklemedik**, çünkü tek oturumluk öğrenme akışında gereksiz kayıt zorunluluğu sürtünme yaratır.
2. **İkinci senaryo eklemedik**, çünkü mevcut sağlık vakasının sekiz karar yolunun tamamını test etmek önceliklidir.
3. **Gerçek hasta verisi kullanmadık**, çünkü sentetik vaka eğitim hedefini sağlar ve kişisel veri riskini doğurmaz.

## Teknik tasarım

- `src/main.js`: vanilla JavaScript, ES modules, DOM tabanlı durum makinesi ve sayaç.
- `src/tutor.mjs`: çevrimdışı deterministik sorular, kullanıcı metni sunucuya gönderilmez.
- `src/style.css`: 390px mobil öncelikli CSS, rol ve hedefe duyarlı sahne.
- `tests/tutor-eval.mjs`: 20 senaryonun yeniden üretilebilir kontrolü.

### Yapılmadı (dürüst teslim sınırı)

- **Üretken AI tutor:** Mevcut tutor bir LLM değil. Google AI Studio/Gemini entegrasyonu ve orada yayımlama yapılmadı.
- **Google Stitch:** Üç mobil ekran tarayıcıdan görselleştirildi; Stitch üzerinde bağımsız proje oluşturulmadı.
- **Cypress yürütme kanıtı:** Cypress test dosyaları hazır ama bu ortamda Cypress binary'si yüklenemedi. Gerçek tarayıcı davranışlarını Chromium + Playwright ile kontrol ettik.

## Teslim bağlantıları

- GitHub kaynak: `https://github.com/Mervebeyazal/mini_recipe/tree/se-primer-yzm301` (ayrı bir `se-primer` deposu için GitHub'da yeni repo açılmalıdır; mevcut entegrasyonda repo oluşturma yetkisi yok).
- Google AI Studio: **Henüz yayımlanmadı**.
- Demo video: ZIP içinde, dış bağlantı **henüz yayımlanmadı**.

### Referanslar

Ders PDF'i: *SE Primer — YZM301*, 2026. Cypress docs: https://docs.cypress.io. Kişisel Verilerin Korunması Kanunu: https://www.kvkk.gov.tr.
