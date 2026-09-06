# Talep formunu Google Form'a bağlama

Form şu an çalışıyor ama e-posta göndermiyor: gönder'e basılınca
yapılandırılmış bir `mailto:` açılıyor. Aşağıdaki adımlar tamamlanınca
gerçek gönderime geçer.

## 1 · Google Form'u aç

forms.google.com → boş form. Şu **9 kısa yanıt alanını** sırayla ekle
(adlar birebir aynı olmalı):

    Name
    Company
    Email
    Phone / WhatsApp
    Country
    Project location
    Message          ← bunu "paragraf" yap
    Category
    Service

`Category` ve `Service` alanlarını en sona koy. Bunlar sitenin otomatik
doldurduğu alanlar — ziyaretçi görmez.

## 2 · Alan kimliklerini çıkar

Formu **Gönder → bağlantı** ile aç, sonra sayfanın kaynağını görüntüle ve
`entry.` ile başlayan numaraları not et. Ya da bana form bağlantısını ver,
ben çıkarırım.

## 3 · Bana ver

- Formun `formResponse` adresi
- 9 alanın `entry.XXXX` numarası

Kalanını ben bağlarım.

## 4 · Konu satırı için Apps Script (isteğe bağlı)

Google Form'un kendi bildirim e-postasının konusu sabittir. İstediğin
`[TRADE] [MARBLE] New Quotation Request` biçimi için yanıt e-tablosuna
şu betik eklenir: Uzantılar → Apps Script → yapıştır → tetikleyici olarak
"form gönderildiğinde" seç.

```javascript
function onFormSubmit(e) {
  const v = e.namedValues;
  const al = (k) => (v[k] && v[k][0]) ? v[k][0] : "";
  const kategori = al("Category") || "GENERAL";
  const hizmet   = al("Service");
  const konu = "[" + kategori.toUpperCase() + "]" +
               (hizmet ? " [" + hizmet.toUpperCase() + "]" : "") +
               " New Website Enquiry";
  const govde =
    "Category: " + kategori + "\n" +
    "Service:  " + (hizmet || "—") + "\n" +
    "──────────────────────────────\n" +
    "Name:     " + al("Name") + "\n" +
    "Company:  " + al("Company") + "\n" +
    "Email:    " + al("Email") + "\n" +
    "Phone:    " + al("Phone / WhatsApp") + "\n" +
    "Country:  " + al("Country") + "\n" +
    "Location: " + al("Project location") + "\n\n" +
    "Message:\n" + al("Message") + "\n";
  MailApp.sendEmail({
    to: "info@arcotratrade.com",
    subject: konu,
    body: govde,
    replyTo: al("Email") || undefined
  });
}
```

## Alternatif

Google Form istemezsen **Web3Forms** (web3forms.com) daha az adım:
e-posta gir, ücretsiz anahtar al, bana ver. Konu satırı formun içinden
ayarlanıyor, Apps Script gerekmiyor.
