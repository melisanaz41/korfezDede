// Sadece mobil menü. Sayfa içeriği JS'e bağlı değildir (SEO için).
(function () {
  var dugme = document.querySelector('.menu-dugme');
  var nav = document.getElementById('nav');
  if (!dugme || !nav) return;
  dugme.addEventListener('click', function () {
    var acik = nav.classList.toggle('acik');
    dugme.setAttribute('aria-expanded', acik ? 'true' : 'false');
  });
})();
