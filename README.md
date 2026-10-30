# SE Primer — YZM301

Mobil öncelikli, üç karar aşamalı yazılım mühendisliği kriz simülasyonu.

## Kurulum
Node.js 18+ gerekir.
```bash
npm install
npm run dev
```
Tarayıcı: http://localhost:5173

## Test
Bir terminalde `npm run dev`, diğerinde `npm run test:e2e`. Cypress sekiz A/B karar yolunun tamamını, yeniden başlatmayı, kişiselleştirmeyi ve uzman sayacını sınar. Testler hazırlanmıştır; bu paketin oluşturulması testlerin çalıştırıldığı anlamına gelmez.

## Ürün kararı: yapmadığımız üç özellik
1. Kullanıcı hesabı eklemedik, çünkü tek oturumluk öğrenme akışında kayıt zorunluluğu gereksiz sürtünme yaratır.
2. İkinci senaryo eklemedik, çünkü üç kararın tüm dallarını test etmek önceliklidir.
3. Gerçek hasta verisi kullanmadık, çünkü öğretim hedefi sentetik vaka ile karşılanabilir ve mahremiyet riski yaratılmamalıdır.

## Önemli teslim notları
- **AI tutor:** Canlı LLM entegrasyonu değil, cevap vermeyen deterministik Sokratik soru sistemi; 20 örnek için `docs/tutor-eval.md` bulunur. Gerçek model değerlendirmesi olarak sunulmamalıdır.
- **Google Stitch:** `DESIGN.md` tasarım belgesi ve aktarım promptu içerir; Stitch proje bağlantısı henüz yoktur.
- **Google AI Studio:** Proje yerel Vite/React uygulamasıdır; AI Studio üzerinde yayımlanmış bağlantı henüz yoktur.
- **Cypress video:** Test yapılandırmasında video açıktır; `npm run test:e2e` sonrasında Cypress video üretir. 60 saniyelik demo ayrıca kaydedilmelidir.

## Teslim bağlantıları
GitHub kaynak dalı: https://github.com/Mervebeyazal/mini_recipe/tree/se-primer-yzm301
AI Studio uygulaması: yayınlanmadı.
Demo videosu: kaydedilmedi/yayınlanmadı.

## Kaynaklar
Ders ödevi: SE Primer — YZM301 (2026); Cypress dokümantasyonu (docs.cypress.io); 6698 sayılı KVKK (kvkk.gov.tr).