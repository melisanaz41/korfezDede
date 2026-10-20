# Körfezde Hurda – korfezdedehurda.com

Saf HTML + CSS (+ 10 satırlık menü JS'i) ile hazırlanmış, SEO odaklı statik hurdacı sitesi.

## Klasör yapısı

```
/                       → Ana sayfa (index.html)
/korfez-hurdaci/        → Bölge sayfaları (Körfez, İzmit, Dilovası, Yarımca)
/demir-hurda/ ...       → Hurda türü sayfaları (demir, bakır, alüminyum, araç)
/blog/                  → Blog listesi + /blog/yazi-adi/ yazıları
/iletisim/              → İletişim
/assets/css/style.css   → Tüm tasarım (renkler :root içinde)
/assets/img/            → Fotoğraflar (foto-1/2/3.svg yer tutucudur)
/tools/build.py         → İsteğe bağlı sayfa üretici
sitemap.xml, robots.txt, 404.html
```

## VS Code'da çalıştırma

1. Klasörü VS Code'da açın.
2. "Live Server" eklentisini kurun, `index.html` üzerinde sağ tık → **Open with Live Server**.
   (Bağlantılar `/` ile başladığı için siteyi klasörü kök alarak açmanız gerekir; Live Server bunu yapar.)

## Fotoğraf ekleme (3 alan)

1. Fotoğraflarınızı `assets/img/` içine koyun (öneri: 1200×800, `.webp` veya `.jpg`, 200 KB altı).
2. `tools/build.py` içindeki `FOTOLAR` listesinde `dosya`, `alt` ve `yazi` alanlarını değiştirin.
3. `python tools/build.py` çalıştırın.

`alt` metni SEO için önemlidir; ör. "Körfez Kocaeli demir hurda yığını".

## Yeni blog yazısı ekleme

`tools/build.py` içindeki `BLOGLAR` listesine bir kayıt ekleyin (slug, tarih, baslik, title, desc, govde), sonra:

```
python tools/build.py
```

Sitemap, blog listesi ve ana sayfadaki "son yazılar" otomatik güncellenir. (Python kullanmak istemezseniz `blog/` altındaki bir yazı klasörünü kopyalayıp elle düzenleyebilir, `sitemap.xml`'e satır ekleyebilirsiniz.)

## Yayına almadan önce kontrol edin

- [ ] **Alan adı:** Kodda `https://korfezdedehurda.com` kullanıldı. Türkçe karakterli (körfez…) bir alan adı aldıysanız ya da yazım farklıysa `build.py` başındaki `SITE` değerini değiştirin. Not: Türkçe karakterli alan adları (IDN) bazı yerlerde bozuk görünebilir, ASCII yazımı da ayrıca almanız önerilir.
- [ ] **Hizmet metinleri:** Alınan hurda türleri, hizmet bölgeleri, SSS cevapları taslaktır. Gerçekte yaptığınız işe göre düzenleyin. Fiyat, çalışma saati, nakliye, ödeme, lisans gibi iddiaları ancak doğruysa ekleyin.
- [ ] **Araç hurdası:** Mevzuat ve gerekli belgeler konusunda yazıyı güncel şartlara göre kontrol edin.
- [ ] **Fotoğraflar:** Kendi fotoğraflarınızı yükleyin.
- [ ] **Çalışma saatleri:** Belli ise `isletme_schema()` içine `openingHours` ekleyin.

## SEO kurulumu

1. Siteyi yayınlayın (Netlify, Cloudflare Pages, GitHub Pages veya klasik hosting; hepsi statik siteyi destekler).
2. **Google Search Console**'a alan adını ekleyin, `https://korfezdedehurda.com/sitemap.xml` adresini gönderin.
3. **Google İşletme Profili** oluşturun (ikinci faz). Adres, telefon ve adı sitedeki bilgilerle birebir aynı yazın.
4. Düzenli blog yazın (ayda en az 2–4), yazılardan ilgili hizmet ve bölge sayfalarına bağlantı verin.
