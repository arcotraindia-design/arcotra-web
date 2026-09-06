/* ARCOTRA — ortak davranışlar */
(function () {
  "use strict";

  /* mobil menü */
  var btn = document.getElementById("menuBtn");
  var links = document.getElementById("navlinks");
  if (btn && links) {
    btn.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        links.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* kaydırdıkça beliriş */
  var items = document.querySelectorAll(".rv");
  if (!("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(items, function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "140px 0px 0px 0px", threshold: 0.02 });
    Array.prototype.forEach.call(items, function (el) { io.observe(el); });
  }

  /* ── talep formu: bağlamı adresten al ── */
  var form = document.getElementById("enquiry");
  if (!form) return;

  function param(ad) {
    try { return new URLSearchParams(location.search).get(ad) || ""; }
    catch (e) { return ""; }
  }
  function baslikla(s) {
    return s.replace(/-/g, " ").replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  }

  var kategori = param("c");
  var hizmet = param("s");

  var ozet = document.getElementById("ctx-summary");
  var kEl = document.getElementById("ctx-category");
  var sEl = document.getElementById("ctx-service");
  var pEl = document.getElementById("ctx-page");
  var kGoster = document.getElementById("ctx-category-label");
  var sGoster = document.getElementById("ctx-service-label");
  var sSatir = document.getElementById("ctx-service-row");

  if (kEl) kEl.value = kategori ? baslikla(kategori) : "General enquiry";
  if (sEl) sEl.value = hizmet ? baslikla(hizmet) : "";
  if (pEl) pEl.value = document.referrer || location.href;

  if (kategori) {
    if (kGoster) kGoster.textContent = baslikla(kategori);
    if (hizmet && sGoster) { sGoster.textContent = baslikla(hizmet); }
    else if (sSatir) { sSatir.style.display = "none"; }
    if (ozet) ozet.hidden = false;
  }

  /* konu satırı: [KATEGORİ] [HİZMET] … */
  var konu = document.getElementById("ctx-subject");
  if (konu) {
    var p = [];
    if (kategori) p.push("[" + baslikla(kategori).toUpperCase() + "]");
    if (hizmet) p.push("[" + baslikla(hizmet).toUpperCase() + "]");
    p.push(hizmet || kategori ? "New Website Enquiry" : "New Website Enquiry");
    konu.value = p.join(" ");
  }

  /* uç nokta yoksa WhatsApp / e-postaya düş */
  form.addEventListener("submit", function (e) {
    if (form.dataset.endpoint) return;      /* gerçek uç nokta bağlıysa normal gönder */
    e.preventDefault();
    var d = new FormData(form);
    var satir = [];
    d.forEach(function (v, k) {
      if (k.charAt(0) !== "_" && String(v).trim()) satir.push(k + ": " + v);
    });
    var govde = satir.join("\n");
    var konuMetni = (konu && konu.value) || "New Website Enquiry";
    location.href = "mailto:info@arcotratrade.com?subject=" +
      encodeURIComponent(konuMetni) + "&body=" + encodeURIComponent(govde);
  });
})();
