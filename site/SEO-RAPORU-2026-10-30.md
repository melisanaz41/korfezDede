# Search Console raporuna göre SEO uygulaması — 30 Ekim 2026

## Veriler ve sınırlar

| Rapor | Dosyadaki dönem | Tıklama | Gösterim | TO |
| --- | --- | ---: | ---: | ---: |
| Son 7 gün, (1).xlsx | 21–27 Ekim 2026 | 39 | 151 | %25,83 |
| Son 24 saat, .xlsx | 29–30 Ekim; rapor saat dilimi UTC+02:00 | 1 | 17 | %5,88 |

Toplamlar Grafik sekmesinden hesaplandı. Farklı dönemler doğrudan büyüme/düşüş karşılaştırması değildir. Örneklem küçüktür. Sorgu tablosu tüm aramaları kapsamayabilir; sayfa satırları site toplamından farklı olabilir. Dosya içerikleri veri olarak değerlendirildi.

## Uygulanan değişiklikler

- İzmit: 7 günde 17 gösterim ve 6 sayfa tıklaması; telefon sorguları da var. Başlık/açıklama güncellendi, telefon ve ilgili metal hizmet bağlantıları eklendi. Körfez merkez bilgisi korundu.
- Dilovası: 4 gösterim, 0 tıklama, ortalama konum 65,75. Başlık, açıklama ve H1 güncellendi; sanayi hurdasının fotoğraflanması, yükleme bilgisi, telefon ve teslim koşulları eklendi.
- Yarımca: 30 gösterim, 16 sayfa tıklaması. URL ve mevcut içerik korundu; açıklayıcı başlık, telefon, konum ve hazırlık bilgileri eklendi.
- Demir fiyat rehberi: 10 gösterim, 0 tıklama; kilo fiyatı sorguları yaklaşık 82–95. sıralarda. Başlık ve H1 arama niyetine uyarlandı; güncel teklif isteme ve net kg × TL/kg hesabı eklendi. Doğrulanmamış günlük fiyat yazılmadı. Makale şeması başlık ve değişiklik tarihiyle eşleştirildi.
- Demir hizmet sayfasına kilo fiyatı açıklaması ve rehber bağlantısı eklendi.
- İletişim: 22 gösterim, 11 HTTPS sayfa tıklaması. Telefon odaklı başlık, açıklama, H1 ve bölge bağlantıları eklendi.

Değişiklikler kök site ve `korfezDede/site` kopyasına kendi tasarımları korunarak uygulandı. SEO verileri `tools/seo-pages.json` içinde saklandı. Üreticide makale şeması eşleşmesi eklendi. Yalnızca değişen altı URL'nin sitemap tarihi güncellendi. Tam site üreticisi mevcut fotoğraf ve elle yapılmış düzenlemeleri değiştirebildiği için çalıştırılmadı.

Araç rehberi 17 gösterim ve 0 tıklama almış olsa da resmi işlem ve bertaraf belgesi açıklamaları güncel resmi kaynak doğrulaması gerektirir; bu uygulamada hukuki süreç içeriği genişletilmedi. Derince/Gölcük için hizmet doğrulanmadan yeni bölge sayfası oluşturulmadı.

## Yayın ve teknik öncelik

Bu oturumda yayın yapılmadı. Mevcut hosting'e kullandığınız site kopyasından şu dosyaları yükleyin: `izmit-hurdaci/index.html`, `dilovasi-hurdaci/index.html`, `yarimca-hurdaci/index.html`, `blog/hurda-demir-fiyatlari-neleri-etkiler/index.html`, `demir-hurda/index.html`, `iletisim/index.html`, `sitemap.xml`. Araçlar ve raporun yayınlanması gerekmez.

Raporda www HTTPS ana sayfası 45 gösterim/1 tıklama; HTTP ana sayfası ve HTTP alt sayfalar da görünüyor. Bu, kontrol önceliğidir; mevcut yönlendirme hatasını tek başına kanıtlamaz. Canlı erişim aracı üç alan adı varyantını açamadığı için sunucu durumu doğrulanamadı. Hosting türü bilinmeden aktif sunucu yapılandırması eklenmedi.

Hosting panelinde HTTP ve www sürümlerini yol ve sorguyu koruyan kalıcı 301/308 yönlendirmeyle `https://korfezdedehurda.com` adresinde birleştirin; önce mevcut kuralları ve SSL'i kontrol edin. Canonical adresleri zaten bu alan adında. Search Console URL Denetimi'nde Google'ın seçtiği canonical adresini kontrol edin. Geçersiz URL'nin HTTP 404 verdiğini doğrulayın.

Yayın sonrası altı URL için canlı URL denetimi yapın, dizine ekleme isteyin ve sitemap'i gönderin. Sonraki eşit 28 günlük dönemlerde Türkiye/Web filtreleri aynı tutularak sorgu, sayfa ve cihaz kırılımında karşılaştırma yapın. Sıralama veya tıklama artışı garantisi yoktur.

## Kontrol ve kaynaklar

`node tools/check-search-seo.cjs`: iki kopyada tek H1, canonical, SEO içerik eşleşmesi, JSON-LD ve yerel bağlantılar. Tarayıcı görünüm kontrolü ve Python üreticisi çalıştırılmadı.

- https://developers.google.com/search/docs/appearance/title-link
- https://developers.google.com/search/docs/appearance/snippet
- https://developers.google.com/search/docs/essentials

## Kontrolde bulunan ek eksik

`korfezDede/site` kopyasında mevcut bağlantıların hedefi olan üç rehber klasörü eksikti. Kök kopyadan `blog/korfez-kombi-hurdasi`, `blog/kocaeli-kablo-hurdasi`, `blog/korfez-petek-hurdasi` klasörleri tamamlandı. İkinci kopyayı yayınlıyorsanız bu üç klasörü de yükleyin. Bu sayfaların tarayıcı görünümü ayrıca doğrulanmadı. Son kontrol: 12 sayfanın H1, canonical, içerik, JSON-LD ve yerel bağlantı kontrolleri geçti.
