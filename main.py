
import nltk

nltk.download('punkt')
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('stopwords')

bankacilik_verisi = {
    'soru': [
        "Hesabımda ne kadar para var?"
        "Hesap bakiyem ne kadar?",
        "Son işlemim ne zaman yapıldı?",
        "Kredi kartı borcum ne kadar?",
        "Bir sonraki ödeme tarihim ne zaman?"
    ],
    'cevap': [

        "Hesabınızda 1500 TL bulunmaktadır.",
        "Son işleminiz 15 Haziran tarihinde yapılmıştır.",
        "Kredi kartı borcunuz 750 TL'dir.",
        "Bir sonraki ödeme tarihiniz 1 Ağustos tarihindedir."
    ]
}

stop_words = set(stopwords.words('turkish'))


def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)


def cevap_ver(soru):
    temiz_soru = preprocess_text(soru)
    for i in range(len(bankacilik_verisi['soru'])):
        if temiz_soru in preprocess_text(bankacilik_verisi['soru'][i]):
            return bankacilik_verisi['cevap'][i]
    return "Üzgünüm, bu soruya cevap veremiyorum."


soru = "Hesabımda ne kadar para var?"
cevap = cevap_ver(soru)
print("Soru:", soru)
print("Cevap:", cevap)

while True:
    soru = input("Soru: ")
    if soru.lower() == 'exit':
        break
    cevap = cevap_ver(soru)
    print("Cevap:", cevap)





