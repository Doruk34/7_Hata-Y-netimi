# Assert Kullanımı:

"""
Assert ifadesi, bir koşul ifadesi anlamına gelir,
Koşul doğru olduğu sürece çalışır.
Doğru olmadığı taktirde ise, bir hata mesajı gönderir.
Almış olduğu değer True olduğu taktirde çalışır.

"""

try:
    kullanici_adi = input("kullanıcı Adınızı Giriniz: ")
    assert len(kullanici_adi) !=0
except AssertionError as hata:
    print("Kullanıcı Adı Bölümü Boş Geçilemez!",hata)

