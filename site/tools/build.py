# -*- coding: utf-8 -*-
"""
Körfezde Hurda – site üretici (İSTEĞE BAĞLI).

Kullanım:   python tools/build.py
Ne yapar:   Aşağıdaki veriden tüm HTML sayfalarını, sitemap.xml ve robots.txt dosyalarını yeniden üretir.
Neden:      Menü/alt bilgi gibi ortak alanları tek yerden değiştirir; yeni blog eklemek 1 kayıt ekleme işidir.
Not:        İsterseniz bu dosyayı hiç kullanmayıp üretilmiş .html dosyalarını doğrudan elle de düzenleyebilirsiniz.
"""
import json, os, html
from datetime import date

# ====================== 1) GENEL AYARLAR ======================
SITE = "https://korfezdedehurda.com"      # Alan adı farklıysa (ör. körfez → korfez) sadece burayı değiştirin
AD = "Körfezde Hurda"
YETKILI = "Rasıh Şenses"
TEL_GORUNEN = "0536 847 52 15"
TEL_ULUSLARARASI = "+905368475215"
TEL_HREF = "tel:+905368475215"
WA_HREF = "https://wa.me/905368475215?text=Merhaba%2C%20hurda%20konusunda%20bilgi%20almak%20istiyorum."
ADRES_SATIR = "Abdülhamit Caddesi, Körfez / Kocaeli"
HARITA = "https://www.google.com/maps/search/?api=1&query=Abdülhamit+Caddesi+Körfez+Kocaeli"
BUGUN = date.today().isoformat()
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

FOTOLAR = [  # Kendi fotoğraflarınızı assets/img/ içine koyup sadece "dosya" ve "alt" alanlarını değiştirin
    {"dosya": "foto-1.svg", "alt": "Körfez Kocaeli hurda alım alanı – demir hurda yığını", "yazi": "Demir ve sac hurda alımı"},
    {"dosya": "foto-2.svg", "alt": "Bakır ve alüminyum hurda – Kocaeli hurdacı", "yazi": "Bakır, pirinç ve alüminyum"},
    {"dosya": "foto-3.svg", "alt": "Araç ve sanayi hurdası toplama – Körfez Yarımca Dilovası", "yazi": "Araç ve sanayi hurdası"},
]

# ====================== 2) İÇERİK VERİSİ ======================
HIZMETLER = [
    {
        "slug": "demir-hurda", "ad": "Demir Hurda",
        "title": "Demir Hurda Alımı Körfez, İzmit, Dilovası | Körfezde Hurda",
        "desc": "Körfez, İzmit, Dilovası ve Yarımca’da demir, sac, profil ve inşaat demiri hurdası alımı. Güncel fiyat için arayın: 0536 847 52 15.",
        "h1": "Körfez’de Demir Hurda Alımı",
        "ozet": "Sac, profil, boru, inşaat demiri ve makine parçası hurdası.",
        "giris": "Demir hurda; atölye, inşaat ve sanayi faaliyetlerinde en sık ortaya çıkan hurda türüdür. Körfez, İzmit, Dilovası ve Yarımca hattında çalışan işletmeler ve bireyler için demir hurdanın değerlendirilmesi hem yer açar hem de geri dönüşüme katkı sağlar.",
        "turler": ["Sac ve levha kesim artıkları", "Profil, boru ve köşebent", "İnşaat demiri ve filiz", "Makine, kalıp ve ekipman parçaları", "Dökme demir parçalar", "Eski çelik kapı, korkuluk, raf ve çatı malzemeleri"],
        "hazirlik": ["Demiri yağ, kauçuk, beton ve plastik gibi yabancı maddelerden mümkün olduğunca ayırın.", "Kalın ve ince malzemeyi ayrı yığınlarda toplayın; değerlendirme daha net olur.", "Yük miktarı büyükse fotoğraf göndererek ön bilgi alın."],
    },
    {
        "slug": "bakir-hurda", "ad": "Bakır Hurda",
        "title": "Bakır Hurda Alımı Kocaeli Körfez | Körfezde Hurda",
        "desc": "Kocaeli Körfez’de bakır kablo, bakır boru ve pirinç hurda alımı. Temiz ve ayrıştırılmış malzemede değerlendirme için arayın.",
        "h1": "Körfez’de Bakır Hurda Alımı",
        "ozet": "Kablo, boru, bobin, pirinç ve diğer bakır alaşımları.",
        "giris": "Bakır, hurda piyasasında en çok aranan metallerden biridir. Malzemenin temizliği ve cinsi değerlendirmeyi doğrudan etkiler. Körfez ve çevresindeki atölye, fabrika ve tadilat artıkları için bakır hurdanızı doğru ayrıştırmak, daha sağlıklı bir değerlendirme yapılmasını sağlar.",
        "turler": ["Bakır kablo ve iletkenler", "Bakır boru ve tesisat parçaları", "Bobin ve motor sargıları", "Pirinç (sarı) armatür ve vana", "Radyatör ve soğutucu bakır parçalar", "Elektrik panosu ve trafo artıkları"],
        "hazirlik": ["Kabloların plastik kılıfını soymak yerine önce nasıl değerlendirileceğini sorun; cins ayrımı önemlidir.", "Bakırı pirinç ve alüminyumdan ayrı tutun.", "Islak, çamurlu veya yağlı malzemeyi mümkünse kurutup temizleyin."],
    },
    {
        "slug": "aluminyum-hurda", "ad": "Alüminyum Hurda",
        "title": "Alüminyum Hurda Alımı Körfez Kocaeli | Körfezde Hurda",
        "desc": "Körfez, İzmit ve Dilovası’nda alüminyum profil, jant, teneke ve doğrama hurdası alımı. Bilgi ve değerlendirme için arayın.",
        "h1": "Körfez’de Alüminyum Hurda Alımı",
        "ozet": "Profil, doğrama, jant, kazan ve alüminyum talaş.",
        "giris": "Alüminyum hafif, geri dönüşümü kolay ve değeri korunan bir metaldir. Doğrama, profil, jant ve ev eşyası gibi pek çok kaynaktan çıkar. Alaşım türü ve temizlik, değerlendirmede belirleyici olduğundan malzemeyi ayrı toplamanız faydalı olur.",
        "turler": ["Alüminyum doğrama ve profil", "Jant ve motor parçaları", "Kazan, tencere ve mutfak malzemeleri", "Radyatör ve soğutucu panel", "Baskı levhası ve levha kesim artıkları", "Alüminyum talaş ve sanayi artıkları"],
        "hazirlik": ["Cam, conta ve demir bağlantı parçalarını ayırın.", "Mıknatıs yapışan parçalar alüminyum değildir; ayrı yığına alın.", "Boyalı, kaplamalı ve temiz profilleri ayrı sınıflandırın."],
    },
    {
        "slug": "arac-hurdasi", "ad": "Araç Hurdası",
        "title": "Araç Hurdası Alımı Körfez Kocaeli | Körfezde Hurda",
        "desc": "Körfez, İzmit, Dilovası ve Yarımca’da araç hurdası ve hurda araç değerlendirme hakkında bilgi alın. Önce arayın: 0536 847 52 15.",
        "h1": "Körfez’de Araç Hurdası",
        "ozet": "Kullanım dışı araç ve araç parçası hurdası için bilgi alın.",
        "giris": "Kullanım dışı kalan araçlar, mevzuat gereği belirli usullerle hurdaya ayrılır. Resmi süreç ve gerekli belgeler konusunda önce arayıp bilgi almanızı öneririz; böylece araç sahibi olarak hem zaman kaybetmez hem de sonradan sorun yaşamazsınız.",
        "turler": ["Kazalı ve çalışmayan araçlar", "Ekonomik ömrünü tamamlamış araçlar", "Araç şasesi, kaporta ve metal parçalar", "Katalizör, akü ve radyatör gibi parçalar (ayrı değerlendirilir)"],
        "hazirlik": ["Araç ruhsatı ve kimlik belgenizi hazır bulundurun.", "Aracın trafik kaydı, borç ve haciz durumunu önceden kontrol edin.", "Süreç ve belgeler için hurda aracı teslim etmeden önce bizi arayın."],
    },
]

BOLGELER = [
    {
        "slug": "korfez-hurdaci", "ad": "Körfez",
        "title": "Körfez Hurdacı | Demir, Bakır, Alüminyum Hurda Alımı",
        "desc": "Körfez’de güvenilir hurdacı arıyorsanız: demir, bakır, alüminyum ve araç hurdası alımı. Abdülhamit Caddesi, Körfez. Tel: 0536 847 52 15.",
        "h1": "Körfez Hurdacı",
        "ozet": "Merkez adresimiz Körfez’dedir; Abdülhamit Caddesi.",
        "giris": [
            "Körfez Hurdacı olarak merkezimiz Abdülhamit Caddesi üzerindedir. Körfez’de ev, atölye, iş yeri ve sanayi tesislerinden çıkan demir, bakır, alüminyum ve diğer metal hurdaları için bir telefon uzaklığındayız.",
            "Küçük miktarlı hurda bırakmak isteyenler de, büyük hacimli sanayi hurdasını değerlendirmek isteyenler de bize ulaşabilir. Malzemeniz hakkında fotoğraf ve kısa bir bilgi ile ön değerlendirme yapılır.",
        ],
        "maddeler": ["Körfez merkez ve çevresi", "Atölye, dükkân ve inşaat hurdası", "Bakır, pirinç ve alüminyum hurda", "Mutfak, ev eşyası ve eski metal eşya"],
    },
    {
        "slug": "izmit-hurdaci", "ad": "İzmit",
        "title": "İzmit Hurdacı | Kocaeli Hurda Alımı: Demir, Bakır, Alüminyum",
        "desc": "İzmit’te hurda alımı: demir, bakır, alüminyum ve araç hurdası. Körfez merkezli hurdacı. Bilgi için arayın: 0536 847 52 15.",
        "h1": "İzmit Hurdacı",
        "ozet": "İzmit merkez ve çevresindeki hurda talepleri için.",
        "giris": [
            "İzmit’te hurdasını değerlendirmek isteyen bireyler, esnaf ve işletmeler için Körfez merkezli hizmet veriyoruz. Adresiniz ve malzeme miktarınızla ilgili kısa bir telefon görüşmesi, süreci hızlandırır.",
            "Tadilat, dükkân boşaltma, bahçe ve depo temizliği gibi durumlarda çıkan karışık metal hurdalarını cinslerine göre ayırarak değerlendirebiliriz.",
        ],
        "maddeler": ["İzmit merkez ve çevre ilçelere yakın lokasyonlar", "Tadilat ve yıkım kaynaklı hurda", "Depo ve dükkân temizliği", "Elektrik ve tesisat artıkları"],
    },
    {
        "slug": "dilovasi-hurdaci", "ad": "Dilovası",
        "title": "Dilovası Hurdacı | Sanayi Hurdası ve Metal Alımı",
        "desc": "Dilovası’nda sanayi hurdası, demir, bakır ve alüminyum alımı. Fabrika ve atölyeler için hurdacı. Tel: 0536 847 52 15.",
        "h1": "Dilovası Hurdacı",
        "ozet": "Dilovası sanayi bölgesindeki işletmeler için.",
        "giris": [
            "Dilovası, yoğun sanayi faaliyetleri nedeniyle düzenli olarak hurda üreten bir bölgedir. Fabrika, atölye ve üretim tesislerinde oluşan sac artığı, profil, talaş ve makine hurdalarını değerlendirmek isteyen işletmelerle iletişime açığız.",
            "Düzenli hurda çıkaran firmalar için tekrarlı çalışma düzeni konuşulabilir. Detay için aramanız yeterli.",
        ],
        "maddeler": ["Fabrika ve üretim tesisi hurdası", "Sac, profil, talaş ve kalıp artıkları", "Makine ve ekipman söküm hurdası", "Düzenli ve toplu hurda çalışmaları"],
    },
    {
        "slug": "yarimca-hurdaci", "ad": "Yarımca",
        "title": "Yarımca Hurdacı | Körfez Yarımca Hurda Alımı",
        "desc": "Körfez Yarımca’da hurda alımı: demir, bakır, alüminyum ve sanayi hurdası. Yarımca hurdacı için arayın: 0536 847 52 15.",
        "h1": "Yarımca Hurdacı",
        "ozet": "Körfez’e bağlı Yarımca’da sanayi ve limana yakın bölge.",
        "giris": [
            "Yarımca, Körfez’in sanayi ve liman faaliyetlerinin yoğun olduğu bölgelerinden biridir. Burada çalışan işletmelerin ve çevredeki esnafın hurda ihtiyacı için Körfez merkezden hızlıca ulaşılabilir durumdayız.",
            "Yarımca’daki atölye, depo ve işletmeler için demir, bakır ve alüminyum hurda alımı hakkında bilgi vermeye hazırız.",
        ],
        "maddeler": ["Yarımca sanayi ve depo hurdası", "Liman çevresi iş yeri artıkları", "Metal levha, boru ve profil", "Bakır ve alüminyum parçalar"],
    },
]

# --- BLOG: yeni yazı eklemek için listeye bir kayıt ekleyin, sonra "python tools/build.py" çalıştırın ---
BLOGLAR = [
    {
        "slug": "hurda-demir-fiyatlari-neleri-etkiler", "tarih": "2026-10-01",
        "baslik": "Hurda Demir Fiyatlarını Neler Etkiler?",
        "title": "Hurda Demir Fiyatları Neleri Etkiler? | Körfezde Hurda",
        "desc": "Hurda demir fiyatını belirleyen faktörler: cins, kalınlık, temizlik, miktar ve piyasa. Hurdanızı satmadan önce bilmeniz gerekenler.",
        "govde": """
<p>Hurda demir satmayı düşünen herkesin ilk sorusu aynıdır: “Kilosu ne kadar?” Fiyatlar günlük değişebildiği için sabit bir rakam vermek yanıltıcı olur. Ancak fiyatı belirleyen unsurları bilmek, hurdanızı daha bilinçli değerlendirmenizi sağlar.</p>
<h2>1. Demirin cinsi ve kalınlığı</h2>
<p>Kalın sac, profil ve ağır parçalar, ince ve karışık malzemeden farklı değerlendirilir. Dökme demir, çelik ve inşaat demiri de ayrı sınıflardır.</p>
<h2>2. Temizlik ve yabancı madde</h2>
<p>Demire bağlı beton, plastik, kauçuk, cam, yağ ve toprak; ağırlığı artırsa da değerlendirmeyi olumsuz etkiler. Mümkünse bunları ayırarak getirin ya da hazırlayın.</p>
<h2>3. Miktar</h2>
<p>Büyük ve toplu miktarlar, sevkiyat ve işlem kolaylığı açısından farklı konuşulabilir. Düzenli hurda çıkaran işletmeler için ayrıca çalışma düzeni planlanabilir.</p>
<h2>4. Piyasa koşulları</h2>
<p>Hurda fiyatları; ham madde piyasaları, döviz kuru ve sanayi talebi gibi etkenlerle değişir. Bu yüzden güncel fiyat için satış gününde arayıp sormak gerekir.</p>
<h2>Satmadan önce yapmanız gerekenler</h2>
<ul><li>Malzemeyi cinsine göre ayırın.</li><li>Fotoğraf çekip ön bilgi alın.</li><li>Teslim koşullarını ve ödeme şeklini baştan netleştirin.</li></ul>
<p>Körfez, İzmit, Dilovası ve Yarımca’da demir hurda için <a href="/demir-hurda/">demir hurda sayfamıza</a> göz atabilir ya da doğrudan arayabilirsiniz.</p>
""",
    },
    {
        "slug": "bakir-hurda-nasil-ayrilir-ve-satilir", "tarih": "2026-10-04",
        "baslik": "Bakır Hurda Nasıl Ayrılır ve Satılır?",
        "title": "Bakır Hurda Nasıl Ayrılır ve Satılır? | Körfezde Hurda",
        "desc": "Bakır, pirinç ve kablo hurdasını ayırmanın püf noktaları. Bakır hurdayı satarken değeri korumak için neler yapmalısınız?",
        "govde": """
<p>Bakır; elektrik tesisatı, motor sargıları, borular ve armatürlerde karşımıza çıkar. Doğru ayrıştırılmış bakır hurda, değerlendirmede daha net bir sonuç verir.</p>
<h2>Bakır ve pirinci ayırın</h2>
<p>Bakır kırmızımsı renktedir, pirinç ise sarı tonlardadır. Vana, musluk ve armatürlerin çoğu pirinçtir. Birlikte yığmak değerlendirmeyi belirsizleştirir.</p>
<h2>Kablo hurdası</h2>
<p>Kablolar kalınlığa, kılıfa ve iç yapıya göre farklı değerlendirilir. Kılıfı soyma işini kendiniz yapmadan önce bir telefonla sormak zaman kazandırır.</p>
<h2>Motor ve bobinler</h2>
<p>Elektrik motorlarında demir gövde ve bakır sargı birlikte bulunur. Sökülmüş ve ayrılmış sargılar ile komple motorlar farklı şekilde ele alınır.</p>
<h2>Satış öncesi kontrol listesi</h2>
<ul><li>Bakırı demir ve alüminyumdan ayırın.</li><li>Islak ve yağlı malzemeyi kurutun.</li><li>Cinsleri ayrı torba veya kasada tutun.</li></ul>
<p>Bakır hurdası için <a href="/bakir-hurda/">bakır hurda sayfamızı</a> inceleyebilir, Körfez’deki adresimizle iletişime geçebilirsiniz.</p>
""",
    },
    {
        "slug": "aluminyum-hurda-cesitleri", "tarih": "2026-10-07",
        "baslik": "Alüminyum Hurda Çeşitleri ve Ayrıştırma Rehberi",
        "title": "Alüminyum Hurda Çeşitleri ve Ayrıştırma | Körfezde Hurda",
        "desc": "Alüminyum profil, jant, teneke ve talaş: alüminyum hurda çeşitleri nelerdir, nasıl ayrıştırılır? Kocaeli hurdacı rehberi.",
        "govde": """
<p>Alüminyum, evlerden fabrikalara kadar çok geniş bir alanda kullanıldığı için hurdası da çok çeşitlidir. Çeşidini bilmek, satışta size avantaj sağlar.</p>
<h2>Başlıca alüminyum hurda türleri</h2>
<ul><li><strong>Profil ve doğrama:</strong> Pencere, kapı ve cephe sistemleri.</li><li><strong>Jant ve döküm parçalar:</strong> Araç jantları, motor parçaları.</li><li><strong>Ev eşyası:</strong> Tencere, kazan, tepsi.</li><li><strong>Radyatör ve soğutucu:</strong> Genelde bakır veya pirinçle karışık olabilir.</li><li><strong>Talaş:</strong> İşleme sonrası ortaya çıkan ince parçalar.</li></ul>
<h2>Alüminyumu nasıl anlarsınız?</h2>
<p>Alüminyum hafiftir ve mıknatısa yapışmaz. Bu iki basit kontrol, demir ve alüminyumu ayırmak için yeterlidir.</p>
<h2>Değeri korumak için</h2>
<p>Cam, plastik, conta ve demir bağlantı elemanlarını ayırın. Temiz ve tek cins alüminyum, karışık yığına göre daha rahat değerlendirilir.</p>
<p>Detaylar için <a href="/aluminyum-hurda/">alüminyum hurda sayfamıza</a> bakabilirsiniz.</p>
""",
    },
    {
        "slug": "arac-hurdaya-ayirma-sureci", "tarih": "2026-10-10",
        "baslik": "Araç Hurdaya Ayırma Süreci: Önce Neleri Kontrol Etmelisiniz?",
        "title": "Araç Hurdaya Ayırma Süreci ve Belgeler | Körfezde Hurda",
        "desc": "Aracınızı hurdaya vermeden önce kontrol etmeniz gereken konular: belgeler, borç-haciz durumu ve resmi süreç hakkında genel bilgiler.",
        "govde": """
<p>Aracınız kullanılamaz hale geldiyse ya da ekonomik ömrünü tamamladıysa hurdaya ayırmayı düşünebilirsiniz. Araç hurdası, normal metal hurdadan farklı olarak resmi işlemlere tabidir.</p>
<h2>Başlamadan önce</h2>
<ul><li><strong>Belgeleriniz:</strong> Ruhsat ve kimlik gibi temel belgeleri hazırlayın.</li><li><strong>Kayıt durumu:</strong> Aracın üzerinde borç, haciz veya trafik cezası olup olmadığını kontrol edin.</li><li><strong>Plakalar:</strong> Plaka ve ruhsatın akıbeti için resmi prosedürü öğrenin.</li></ul>
<h2>Süreç değişebilir</h2>
<p>Mevzuat ve uygulama zaman içinde güncellenebilir. Bu yüzden bu yazıyı genel bilgi olarak okuyun; aracınızı teslim etmeden önce güncel şartları bizden veya ilgili resmi kurumlardan öğrenin.</p>
<h2>Parça ve metal değeri</h2>
<p>Aracın metal kısımları geri dönüşüme kazandırılırken, akü, yağ ve benzeri atıkların uygun şekilde ele alınması gerekir. Bu da araç hurdasında doğru adres seçmeyi önemli kılar.</p>
<p>Körfez ve çevresinde araç hurdası için <a href="/arac-hurdasi/">araç hurdası sayfamızı</a> inceleyin veya arayarak bilgi alın.</p>
""",
    },
    {
        "slug": "kocaeli-sanayi-hurdasi-geri-donusum", "tarih": "2026-10-14",
        "baslik": "Kocaeli’nde Sanayi Hurdası ve Geri Dönüşümün Önemi",
        "title": "Kocaeli Sanayi Hurdası ve Geri Dönüşüm | Körfezde Hurda",
        "desc": "Kocaeli’nde Dilovası, Yarımca ve Körfez sanayisinde hurdanın geri dönüşümü neden önemli? İşletmeler için pratik öneriler.",
        "govde": """
<p>Kocaeli, Türkiye’nin en yoğun sanayi bölgelerinden biridir. Körfez, Dilovası ve Yarımca gibi bölgelerde üretim yapan tesisler düzenli olarak sac, profil, talaş ve ekipman hurdası üretir.</p>
<h2>Neden önemli?</h2>
<p>Metal hurdanın geri dönüşümü, ham madde ihtiyacını azaltır ve atık miktarını düşürür. İşletmeler için ise depo alanı açar, çalışma ortamını düzenler.</p>
<h2>İşletmeler için pratik öneriler</h2>
<ul><li>Hurdayı cinsine göre (demir, bakır, alüminyum, paslanmaz) ayrı alanlarda toplayın.</li><li>Yağlı talaşı ve sıvı atıkları metal hurdadan ayrı yönetin.</li><li>Düzenli hurda çıkıyorsa belirli aralıklarla toplama planı yapın.</li><li>Her teslimatta miktar ve cinsi kayıt altına alın.</li></ul>
<h2>Bölgesel hizmet</h2>
<p>Körfez merkezli olarak <a href="/dilovasi-hurdaci/">Dilovası</a>, <a href="/yarimca-hurdaci/">Yarımca</a> ve <a href="/izmit-hurdaci/">İzmit</a> çevresindeki işletmeler için hurda değerlendirme hakkında bilgi veriyoruz.</p>
""",
    },
]

SSS = [
    ("Hangi hurda türlerini değerlendiriyorsunuz?", "Demir, bakır, alüminyum, pirinç ve araç hurdası gibi metal hurdalar hakkında bilgi veriyoruz. Malzemenizin fotoğrafını göndererek ön bilgi alabilirsiniz."),
    ("Hangi bölgelere hizmet veriyorsunuz?", "Merkezimiz Körfez’dedir. Körfez, İzmit, Dilovası, Yarımca ve çevresindeki talepler için bizi arayabilirsiniz."),
    ("Hurda fiyatı nasıl belirlenir?", "Fiyat; malzemenin cinsi, temizliği, miktarı ve güncel piyasa koşullarına göre değişir. Güncel durum için satış gününde arayarak bilgi almanız en doğrusudur."),
    ("Hurdamı satmadan önce neleri hazırlamalıyım?", "Malzemeyi cinsine göre ayırın, yabancı maddeleri (plastik, beton, cam gibi) mümkün olduğunca temizleyin ve ön değerlendirme için fotoğraf çekin."),
]

# ====================== 3) ŞABLON FONKSİYONLARI ======================
def e(s): return html.escape(s, quote=True)

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def isletme_schema():
    return {
        "@context": "https://schema.org", "@type": "LocalBusiness",
        "@id": SITE + "/#isletme", "name": AD, "url": SITE + "/",
        "description": "Körfez, İzmit, Dilovası ve Yarımca’da demir, bakır, alüminyum ve araç hurdası alımı.",
        "telephone": TEL_ULUSLARARASI, "image": SITE + "/assets/img/foto-1.svg",
        "founder": {"@type": "Person", "name": YETKILI},
        "address": {"@type": "PostalAddress", "streetAddress": "Abdülhamit Caddesi", "addressLocality": "Körfez", "addressRegion": "Kocaeli", "addressCountry": "TR"},
        "areaServed": [{"@type": "City", "name": n} for n in ["Körfez", "İzmit", "Dilovası", "Yarımca", "Kocaeli"]],
        "priceRange": "₺",
    }

def kirinti_schema(parcalar):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": a, "item": SITE + b} for i, (a, b) in enumerate(parcalar)]}

def sss_schema(liste):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in liste]}

NAV = [("/", "Ana Sayfa"), ("/demir-hurda/", "Demir"), ("/bakir-hurda/", "Bakır"), ("/aluminyum-hurda/", "Alüminyum"), ("/arac-hurdasi/", "Araç"), ("/blog/", "Blog"), ("/iletisim/", "İletişim")]

def sayfa(yol, title, desc, govde, schemalar=(), og_tip="website", gizle=False):
    url = SITE + yol
    def _cur(h): return ' aria-current="page"' if h == yol else ""
    nav = "".join(f'<li><a href="{h}"{_cur(h)}>{t}</a></li>' for h, t in NAV)
    bolge_link = "".join(f'<li><a href="/{b["slug"]}/">{b["ad"]} Hurdacı</a></li>' for b in BOLGELER)
    hizmet_link = "".join(f'<li><a href="/{h["slug"]}/">{h["ad"]} Alımı</a></li>' for h in HIZMETLER)
    robots = "noindex,follow" if gizle else "index,follow,max-image-preview:large"
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="geo.region" content="TR-41">
<meta name="geo.placename" content="Körfez, Kocaeli">
<meta property="og:type" content="{og_tip}">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{AD}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/foto-1.svg">
<meta name="theme-color" content="#1f2529">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/css/style.css">
{''.join(ld(s) for s in schemalar)}
</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>
<div class="serit"><div class="kap"><span>{ADRES_SATIR}</span><a href="{TEL_HREF}">Hemen ara: {TEL_GORUNEN}</a></div></div>
<header class="ust">
  <div class="kap">
    <a class="logo" href="/">Körfezde<span>Hurda</span></a>
    <button class="menu-dugme" aria-expanded="false" aria-controls="nav">Menü</button>
    <nav class="nav" id="nav" aria-label="Ana menü"><ul>{nav}</ul></nav>
    <a class="ara" href="{TEL_HREF}">Ara: {TEL_GORUNEN}</a>
  </div>
</header>
<main id="icerik">
{govde}
</main>
<footer class="alt">
  <div class="kap">
    <div>
      <h2>{AD}</h2>
      <p>Körfez, İzmit, Dilovası ve Yarımca’da demir, bakır, alüminyum ve araç hurdası için hurdacı.</p>
      <address style="font-style:normal">
        <strong>{YETKILI}</strong><br>
        {ADRES_SATIR}<br>
        <a href="{TEL_HREF}">{TEL_GORUNEN}</a> · <a href="{WA_HREF}" rel="noopener">WhatsApp</a><br>
        <a href="{HARITA}" rel="noopener" target="_blank">Haritada aç</a>
      </address>
    </div>
    <div><h2>Hizmet bölgeleri</h2><ul>{bolge_link}</ul></div>
    <div><h2>Hurda türleri</h2><ul>{hizmet_link}<li><a href="/blog/">Blog</a></li></ul></div>
    <p class="telif">© {date.today().year} {AD} – korfezdedehurda.com. Tüm hakları saklıdır.</p>
  </div>
</footer>
<div class="mobil-bar"><a class="a1" href="{TEL_HREF}">Hemen Ara</a><a class="a2" href="{WA_HREF}" rel="noopener">WhatsApp</a></div>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""

def kirinti_html(parcalar):
    s = ['<a href="/">Ana Sayfa</a>']
    for a, b in parcalar[1:-1]: s.append(f'<a href="{b}">{a}</a>')
    s.append(parcalar[-1][0])
    return '<nav class="kirinti" aria-label="Sayfa yolu">' + " / ".join(s) + "</nav>"

IKONLAR = {
    "tel": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
    "konum": '<path d="M12 21s7-6.2 7-11a7 7 0 10-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "mesaj": '<path d="M4 5h16v11H9l-5 4z"/>',
    "demir-hurda": '<path d="M3 7h18M3 12h18M3 17h18M7 7v10M17 7v10"/>',
    "bakir-hurda": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
    "aluminyum-hurda": '<path d="M7 3h10v18H7zM7 8h10M7 16h10"/>',
    "arac-hurdasi": '<path d="M3 16l2-6a2 2 0 012-1.4h10A2 2 0 0119 10l2 6v3h-3v-2H6v2H3z"/><circle cx="7.5" cy="14" r=".8"/><circle cx="16.5" cy="14" r=".8"/>',
    "bolge": '<path d="M12 3l9 5-9 5-9-5zM3 13l9 5 9-5"/>',
}
def ikon(n): return f'<svg class="ikon" viewBox="0 0 24 24" aria-hidden="true">{IKONLAR[n]}</svg>'

HARITA_EMBED = "https://www.google.com/maps?q=Abd%C3%BClhamit+Caddesi+K%C3%B6rfez+Kocaeli&output=embed"

def fis(baslik="Bize ulaşın"):
    return f"""<div class="iletisim-kart">
  <h3>{baslik}</h3>
  <ul>
    <li>{ikon("tel")}<span><small>{YETKILI}</small><a class="tel" href="{TEL_HREF}">{TEL_GORUNEN}</a></span></li>
    <li>{ikon("konum")}<span><small>Adres</small>{ADRES_SATIR}</span></li>
  </ul>
  <div class="dugmeler"><a class="btn btn-kirmizi" href="{TEL_HREF}">Ara</a><a class="btn btn-cizgi" href="{WA_HREF}" rel="noopener">WhatsApp</a></div>
</div>"""

def harita_kutusu():
    return f'<div class="harita"><iframe src="{HARITA_EMBED}" title="{AD} konum haritası – Abdülhamit Caddesi, Körfez" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>'

def konum_blogu():
    return f"""<section class="bolum acik" id="konum"><div class="kap">
  <div class="bolum-baslik"><h2>Konum ve iletişim</h2><p>Körfez, Abdülhamit Caddesi. Gelmeden önce aramanızı öneririz.</p></div>
  <div class="konum">
    <div class="iletisim-kart">
      <h3>{AD}</h3>
      <ul>
        <li>{ikon("tel")}<span><small>{YETKILI}</small><a class="tel" href="{TEL_HREF}">{TEL_GORUNEN}</a></span></li>
        <li>{ikon("konum")}<span><small>Adres</small>{ADRES_SATIR}</span></li>
        <li>{ikon("bolge")}<span><small>Hizmet bölgeleri</small>Körfez, İzmit, Dilovası, Yarımca</span></li>
      </ul>
      <div class="dugmeler"><a class="btn btn-kirmizi" href="{TEL_HREF}">Hemen ara</a><a class="btn btn-cizgi" href="{WA_HREF}" rel="noopener">WhatsApp</a><a class="btn btn-cizgi" href="{HARITA}" target="_blank" rel="noopener">Yol tarifi</a></div>
    </div>
    {harita_kutusu()}
  </div>
</div></section>"""

def yan_menu():
    h = "".join(f'<li><a href="/{x["slug"]}/">{x["ad"]} Alımı</a></li>' for x in HIZMETLER)
    b = "".join(f'<li><a href="/{x["slug"]}/">{x["ad"]} Hurdacı</a></li>' for x in BOLGELER)
    return f'<aside class="yan">{fis()}<h3>Hurda türleri</h3><ul>{h}</ul><h3>Bölgeler</h3><ul>{b}</ul></aside>'

def cagri_blogu(metin="Hurdanızı değerlendirmek için bizi arayın"):
    return f"""<section class="cagri"><div class="kap"><div><h2>{metin}</h2><p>{YETKILI} · {ADRES_SATIR}</p></div>
<div class="dugmeler" style="margin:0"><a class="btn btn-mavi" href="{TEL_HREF}">{TEL_GORUNEN}</a><a class="btn btn-cizgi" href="{WA_HREF}" rel="noopener">WhatsApp</a></div></div></section>"""

def sss_html(liste):
    return '<div class="sss">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in liste) + "</div>"

def yaz(yol, icerik):
    dosya = os.path.join(OUT, yol.strip("/"), "index.html") if yol != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(dosya), exist_ok=True)
    with open(dosya, "w", encoding="utf-8") as f: f.write(icerik)

def blog_kart(b):
    i = [x["slug"] for x in BLOGLAR].index(b["slug"]) % len(FOTOLAR)
    f = FOTOLAR[i]
    return (f'<article class="blog-kart"><a href="/blog/{b["slug"]}/" tabindex="-1" aria-hidden="true"><img src="/assets/img/{f["dosya"]}" alt="" width="1200" height="800" loading="lazy"></a>'
            f'<div class="gov"><time datetime="{b["tarih"]}">{b["tarih"]}</time><h3><a href="/blog/{b["slug"]}/">{e(b["baslik"])}</a></h3>'
            f'<p>{e(b["desc"])}</p><a class="devam" href="/blog/{b["slug"]}/">Yazıyı oku</a></div></article>')

# ====================== 4) SAYFALARI ÜRET ======================
urls = []

# ---- Ana sayfa ----
foto_html = "".join(f'<figure><img src="/assets/img/{f["dosya"]}" alt="{e(f["alt"])}" width="1200" height="800" loading="{"eager" if i == 0 else "lazy"}"><figcaption>{e(f["yazi"])}</figcaption></figure>' for i, f in enumerate(FOTOLAR))
hizmet_kart = "".join(f'<div class="kutu">{ikon(h["slug"])}<h3>{h["ad"]}</h3><p>{h["ozet"]}</p><a class="devam" href="/{h["slug"]}/">{h["ad"]} alımı</a></div>' for h in HIZMETLER)
bolge_kart = "".join(f'<div class="kutu">{ikon("konum")}<h3>{b["ad"]} Hurdacı</h3><p>{b["ozet"]}</p><a class="devam" href="/{b["slug"]}/">{b["ad"]} hurda alımı</a></div>' for b in BOLGELER)
son_bloglar = "".join(blog_kart(b) for b in sorted(BLOGLAR, key=lambda x: x["tarih"], reverse=True)[:3])
f0 = FOTOLAR[0]
ana = f"""
<section class="hero"><div class="kap">
  <div>
    <h1>Körfez’de hurdacı: demir, bakır ve alüminyum hurda alımı</h1>
    <p class="giris">Körfez, İzmit, Dilovası ve Yarımca’da hurdanızı değerlendirmek için bir telefon yeterli. Merkezimiz Körfez, Abdülhamit Caddesi.</p>
    <div class="dugmeler"><a class="btn btn-kirmizi" href="{TEL_HREF}">Hemen ara: {TEL_GORUNEN}</a><a class="btn btn-cizgi" href="{WA_HREF}" rel="noopener">WhatsApp’tan yaz</a></div>
  </div>
  <figure class="hero-foto"><img src="/assets/img/{f0["dosya"]}" alt="{e(f0["alt"])}" width="1200" height="800" fetchpriority="high"><figcaption>Körfez / Kocaeli</figcaption></figure>
</div></section>

<div class="hizli"><div class="kap">
  <a href="{TEL_HREF}">{ikon("tel")}<span><small>Hemen arayın</small><strong>{TEL_GORUNEN}</strong></span></a>
  <a class="k" href="#konum">{ikon("konum")}<span><small>Adres</small><strong>Abdülhamit Cd., Körfez</strong></span></a>
  <div>{ikon("bolge")}<span><small>Hizmet bölgeleri</small><strong>Körfez · İzmit · Dilovası · Yarımca</strong></span></div>
</div></div>

<section class="bolum"><div class="kap">
  <div class="bolum-baslik"><h2>Hurda sahamızdan görüntüler</h2><p>Demir, bakır, alüminyum ve araç hurdası çalışmalarımızdan kareler.</p></div>
  <div class="foto-sira">{foto_html}</div>
</div></section>

<section class="bolum acik"><div class="kap">
  <div class="bolum-baslik"><h2>Hangi hurdayı alıyoruz?</h2><p>Malzemenizin türüne göre ilgili sayfaya göz atın.</p></div>
  <div class="izgara">{hizmet_kart}</div>
</div></section>

<section class="bolum koyu"><div class="kap">
  <div class="bolum-baslik"><h2>Hizmet bölgelerimiz</h2><p>Merkezimiz Körfez’dedir. Aşağıdaki bölgelerden gelen taleplere bakıyoruz.</p></div>
  <div class="izgara">{bolge_kart}</div>
</div></section>

<section class="bolum"><div class="kap">
  <div class="bolum-baslik"><h2>Hurdanızı satmak için üç adım</h2></div>
  <ol class="adimlar">
    <li><strong>Arayın veya yazın</strong>Malzemenin cinsini ve yaklaşık miktarını anlatın, mümkünse fotoğraf gönderin.</li>
    <li><strong>Bilgi alın</strong>Değerlendirme şartları ve teslim şekli konusunda bilgi verilir.</li>
    <li><strong>Hurdanızı teslim edin</strong>Anlaşılan şekilde malzemeniz değerlendirilir.</li>
  </ol>
</div></section>

<section class="bolum acik"><div class="kap">
  <div class="bolum-baslik"><h2>Hurda rehberi: blogdan son yazılar</h2></div>
  <div class="izgara">{son_bloglar}</div>
  <p style="margin-top:1.6rem"><a class="btn btn-mavi" href="/blog/">Tüm blog yazıları</a></p>
</div></section>

{konum_blogu()}

<section class="bolum"><div class="kap">
  <div class="bolum-baslik"><h2>Sık sorulan sorular</h2></div>
  {sss_html(SSS)}
</div></section>
{cagri_blogu()}
"""
yaz("/", sayfa("/", "Körfez Hurdacı | Demir, Bakır, Alüminyum Hurda Alımı – Kocaeli", "Körfez, İzmit, Dilovası ve Yarımca’da hurdacı: demir, bakır, alüminyum ve araç hurdası alımı. Abdülhamit Caddesi, Körfez. Ara: 0536 847 52 15.", ana, [isletme_schema(), sss_schema(SSS)]))
urls.append("/")

# ---- Hizmet sayfaları ----
for h in HIZMETLER:
    yol = f"/{h['slug']}/"
    kr = [("Ana Sayfa", "/"), (h["ad"] + " Alımı", yol)]
    tur = "".join(f"<li>{t}</li>" for t in h["turler"])
    hz = "".join(f"<li>{t}</li>" for t in h["hazirlik"])
    bl = " · ".join(f'<a href="/{b["slug"]}/">{b["ad"]}</a>' for b in BOLGELER)
    sss_h = [(f"{h['ad']} hakkında bilgi almak için ne yapmalıyım?", f"Bize {TEL_GORUNEN} numarasından ulaşabilir, malzemenizin fotoğrafını WhatsApp’tan gönderebilirsiniz."), SSS[2]]
    g = f"""
<div class="sayfa-baslik"><div class="kap">{kirinti_html(kr)}<h1>{h['h1']}</h1><p>{h['ozet']}</p></div></div>
<div class="kap icerik"><article>
  <p>{h['giris']}</p>
  <h2>Hangi {h['ad'].lower()} türleri değerlendirilir?</h2><ul>{tur}</ul>
  <h2>Satmadan önce hazırlık</h2><ul>{hz}</ul>
  <h2>Hizmet verdiğimiz bölgeler</h2><p>{bl}</p>
  <h2>Sık sorulan sorular</h2>{sss_html(sss_h)}
  <p style="margin-top:1.5rem"><a class="btn btn-mavi" href="{TEL_HREF}">Ara: {TEL_GORUNEN}</a></p>
</article>{yan_menu()}</div>
{cagri_blogu()}"""
    yaz(yol, sayfa(yol, h["title"], h["desc"], g, [isletme_schema(), kirinti_schema(kr), sss_schema(sss_h)]))
    urls.append(yol)

# ---- Bölge sayfaları ----
for b in BOLGELER:
    yol = f"/{b['slug']}/"
    kr = [("Ana Sayfa", "/"), (b["ad"] + " Hurdacı", yol)]
    paragraflar = "".join(f"<p>{p}</p>" for p in b["giris"])
    md = "".join(f"<li>{m}</li>" for m in b["maddeler"])
    hl = "".join(f'<li><a href="/{h["slug"]}/">{b["ad"]} {h["ad"].lower()} alımı</a></li>' for h in HIZMETLER)
    sss_b = [(f"{b['ad']}’da hurda alıyor musunuz?", f"{b['ad']} ve çevresindeki hurda talepleri için bizi arayabilirsiniz. Merkezimiz Körfez, Abdülhamit Caddesi’dedir. Tel: {TEL_GORUNEN}."), SSS[3]]
    g = f"""
<div class="sayfa-baslik"><div class="kap">{kirinti_html(kr)}<h1>{b['h1']}</h1><p>{b['ozet']}</p></div></div>
<div class="kap icerik"><article>
  {paragraflar}
  <h2>{b['ad']}’da hangi hurdalara bakıyoruz?</h2><ul>{md}</ul>
  <h2>{b['ad']} için hurda türleri</h2><ul>{hl}</ul>
  <h2>Adres ve iletişim</h2>
  <p>{YETKILI}<br>{ADRES_SATIR}<br><a href="{TEL_HREF}">{TEL_GORUNEN}</a></p>
  <h2>Sık sorulan sorular</h2>{sss_html(sss_b)}
  <p style="margin-top:1.5rem"><a class="btn btn-mavi" href="{TEL_HREF}">{b['ad']} için ara</a></p>
</article>{yan_menu()}</div>
{cagri_blogu(f"{b['ad']}’da hurdanız mı var?")}"""
    yaz(yol, sayfa(yol, b["title"], b["desc"], g, [isletme_schema(), kirinti_schema(kr), sss_schema(sss_b)]))
    urls.append(yol)

# ---- Blog liste ----
kr = [("Ana Sayfa", "/"), ("Blog", "/blog/")]
kartlar = "".join(blog_kart(b) for b in sorted(BLOGLAR, key=lambda x: x["tarih"], reverse=True))
g = f"""
<div class="sayfa-baslik"><div class="kap">{kirinti_html(kr)}<h1>Hurda Rehberi ve Blog</h1><p>Hurda demir, bakır, alüminyum ve araç hurdası hakkında pratik bilgiler.</p></div></div>
<section class="bolum"><div class="kap"><div class="izgara">{kartlar}</div></div></section>
{cagri_blogu()}"""
yaz("/blog/", sayfa("/blog/", "Hurda Blogu: Demir, Bakır, Alüminyum Rehberi | Körfezde Hurda", "Hurda fiyatları, ayrıştırma, araç hurdası ve Kocaeli sanayi hurdası hakkında rehber yazılar.", g, [isletme_schema(), kirinti_schema(kr)]))
urls.append("/blog/")

# ---- Blog yazıları ----
for b in BLOGLAR:
    yol = f"/blog/{b['slug']}/"
    kr = [("Ana Sayfa", "/"), ("Blog", "/blog/"), (b["baslik"], yol)]
    makale = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": b["baslik"], "description": b["desc"],
              "datePublished": b["tarih"], "dateModified": b["tarih"], "mainEntityOfPage": SITE + yol,
              "author": {"@type": "Person", "name": YETKILI}, "publisher": {"@type": "Organization", "name": AD, "url": SITE + "/"},
              "image": SITE + "/assets/img/foto-1.svg", "inLanguage": "tr-TR"}
    g = f"""
<div class="sayfa-baslik"><div class="kap">{kirinti_html(kr)}<h1>{e(b['baslik'])}</h1></div></div>
<div class="kap icerik"><article>
  <p class="meta"><time datetime="{b['tarih']}">{b['tarih']}</time> · {YETKILI}</p>
  {b['govde']}
</article>{yan_menu()}</div>
{cagri_blogu()}"""
    yaz(yol, sayfa(yol, b["title"], b["desc"], g, [makale, kirinti_schema(kr)], og_tip="article"))
    urls.append(yol)

# ---- İletişim ----
kr = [("Ana Sayfa", "/"), ("İletişim", "/iletisim/")]
g = f"""
<div class="sayfa-baslik"><div class="kap">{kirinti_html(kr)}<h1>İletişim</h1><p>Körfez, Kocaeli – hurda için bize ulaşın.</p></div></div>
<div class="kap" style="padding:3rem 0">
  <div class="kartlar3">
    <div class="kutu">{ikon("tel")}<h3>Telefon</h3><p>{YETKILI}</p><a href="{TEL_HREF}">{TEL_GORUNEN}</a></div>
    <div class="kutu">{ikon("mesaj")}<h3>WhatsApp</h3><p>Fotoğraf göndererek ön bilgi alın.</p><a class="devam" href="{WA_HREF}" rel="noopener">Mesaj gönder</a></div>
    <div class="kutu">{ikon("konum")}<h3>Adres</h3><p>{ADRES_SATIR}</p><a class="devam" href="{HARITA}" target="_blank" rel="noopener">Yol tarifi al</a></div>
  </div>
  {harita_kutusu()}
  <div style="margin-top:2rem" class="kutu">
    <h3>Hurdanızı bildirirken</h3>
    <ul><li>Hurdanın cinsini (demir, bakır, alüminyum, araç vb.) söyleyin.</li><li>Yaklaşık miktarı ve bulunduğu konumu belirtin.</li><li>Mümkünse bir fotoğraf gönderin.</li></ul>
    <p style="margin:0">Hizmet bölgeleri: Körfez, İzmit, Dilovası, Yarımca ve çevresi.</p>
  </div>
</div>
{cagri_blogu("Hurdanız için hemen arayın")}"""
yaz("/iletisim/", sayfa("/iletisim/", "İletişim | Körfezde Hurda – Körfez, Kocaeli", "Körfezde Hurda iletişim: Abdülhamit Caddesi, Körfez / Kocaeli. Rasıh Şenses – 0536 847 52 15.", g, [isletme_schema(), kirinti_schema(kr)]))
urls.append("/iletisim/")

# ---- 404 ----
g = f"""<section class="bolum"><div class="kap"><h1>Sayfa bulunamadı</h1><p>Aradığınız sayfa taşınmış ya da hiç var olmamış olabilir.</p>
<p><a class="btn btn-mavi" href="/">Ana sayfaya dön</a> <a class="btn btn-kirmizi" href="{TEL_HREF}">{TEL_GORUNEN}</a></p></div></section>"""
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
    f.write(sayfa("/404.html", "Sayfa bulunamadı | Körfezde Hurda", "Sayfa bulunamadı.", g, gizle=True))

# ---- sitemap & robots ----
oncelik = lambda u: "1.0" if u == "/" else ("0.9" if u.count("/") == 2 and not u.startswith("/blog") else "0.7")
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += f"  <url><loc>{SITE}{u}</loc><lastmod>{BUGUN}</lastmod><priority>{oncelik(u)}</priority></url>\n"
sm += "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

# ---- görsel yer tutucular ----
def yer_tutucu(n, renk):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800"><rect width="1200" height="800" fill="{renk}"/><g stroke="#ffffff22" stroke-width="2">' + "".join(f'<path d="M{-800+i*120} 800L{i*120+400} 0"/>' for i in range(0, 20)) + f'</g><text x="600" y="380" fill="#fff" font-family="Arial" font-size="64" font-weight="700" text-anchor="middle">FOTOĞRAF {n}</text><text x="600" y="450" fill="#ffffffb0" font-family="Arial" font-size="34" text-anchor="middle">1200 × 800 – kendi fotoğrafınızı ekleyin</text></svg>'
for i, c in enumerate(["#1856b8", "#0a2351", "#d3202a"], 1):
    open(os.path.join(OUT, "assets/img", f"foto-{i}.svg"), "w", encoding="utf-8").write(yer_tutucu(i, c))

print(f"{len(urls)} sayfa üretildi → {OUT}")
