# Körfezde Hurda SEO çalışması — 27 Ekim 2026

## İlk uygulama

Mevcut URL'ler ve canonical adresleri korundu. Ana sayfa, demir, bakır ve İzmit sayfalarının başlık, açıklama ve H1 alanları güncellendi. Hizmet sayfalarına malzeme ayrımı, fiyat değerlendirmesi ve teslim hazırlığı bilgileri; ilgili rehberlere ve iletişim sayfasına bağlantılar eklendi. Yalnızca bu dört URL'nin sitemap lastmod tarihi değiştirildi.

SEO alanlarının ortak kaynağı `tools/seo-pages.json` dosyasıdır. `tools/build.py` bu veriyi okur. Üretici çalıştırılmadı: mevcut üretici fotoğraf ve başka elle yapılmış düzenlemeleri de yeniden oluşturabilir. Tüm siteyi yeniden üretmeden önce mevcut sürümle farklarını inceleyin.

## Arama ve sayfa eşleştirmesi

| Arama | Öncelikli sayfa |
| --- | --- |
| körfez hurda | `/` |
| körfez demir hurda | `/demir-hurda/` |
| körfez bakır hurda | `/bakir-hurda/` |
| izmit hurda | `/izmit-hurdaci/` |

Körfez bölge sayfası korunmuştur. Aynı sorguda birden fazla sayfanın görünmesi tek başına sorun değildir. Search Console sorgu/sayfa verisi görülmeden sayfa birleştirme veya yönlendirme yapılmamalıdır.

## Yayın ve ölçüm sırası

1. Önce yedek alın. Değişen dört HTML dosyasını ve sitemap.xml dosyasını mevcut hosting'e yükleyin. `tools` ve bu dokümanın ziyaretçilere sunulması gerekli değildir. Bu oturumda yayın yapılmadı.
2. Canlı URL'lerin HTTP 200 döndürdüğünü; HTTP, HTTPS ve www sürümlerinin tek ana alan adına yönlendiğini; geçersiz bir adresin gerçekten HTTP 404 döndürdüğünü kontrol edin. Ağ erişimi başarısız olduğundan bu oturumda canlı sunucu davranışı doğrulanamadı. Bu sonuç sitenin herkese kapalı olduğunu kanıtlamaz.
3. Google Search Console'da dört URL'yi URL Denetimi ile kontrol edin. Google'ın seçtiği canonical adresini, dizin durumunu ve canlı test sonucunu kaydedin. Güncellenen sayfalar için dizine ekleme isteyin; sitemap.xml dosyasını gönderin.
4. Değişiklikten önceki son 28 günün sorgu ve sayfa performansını dışa aktarın. Türkiye, cihaz ve arama türü filtrelerini aynı tutun. Bildirilen 7–12. sayfa sıralamaları kullanıcı gözlemidir; doğrulanmış başlangıç ölçümü değildir.
5. Yayından 2–4 hafta sonra tarama/dizin durumunu; 6–8 hafta sonra tıklama, gösterim, tıklama oranı ve ortalama konumu önceki eşit dönemle karşılaştırın. Talep ve mevsim etkilerini göz önünde bulundurun. Bu süreler sonuç garantisi veya sabit bekleme koşulu değildir.

## Sonraki aşama için gerekli bilgiler

- Search Console'dan son üç ayın sorgu/sayfa raporu ve Sayfa Dizine Ekleme raporu. Mümkünse dört hedef sorgu için hangi URL'lerin gösterim aldığını da ekleyin.
- Google İşletme Profili bağlantısı; gerçek işletme adı, tam adres ve çalışma saatlerinin doğrulanması. İzmit'te ayrı bir şube varsa ancak doğrulanınca eklenmeli.
- Gerçek iş fotoğrafları ve sunulan hizmetlerin doğrulanması: yerinden alım, minimum miktar, yükleme, ödeme ve teslim koşulları.

Bu bilgilerle yerel profil tutarlılığı, gerçek hizmet ayrıntıları ve sayfa performansı üzerinde ikinci uygulama yapılabilir. Yeni bölge sayfalarını çoğaltmak yerine mevcut sayfaların yararını ve işletme kanıtlarını güçlendirin.

## Kaynaklar

- Google başlık önerileri: https://developers.google.com/search/docs/appearance/title-link
- Google SEO başlangıç rehberi: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Yerel işletme yapılandırılmış verileri: https://developers.google.com/search/docs/appearance/structured-data/local-business
