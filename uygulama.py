liste = ["1","2","3","4a","abc","@","50","70"]

# 1) Liste verisi içerisindeki sayısal elemanları bulma:
"""
for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except ValueError:
        continue

"""
# 2) Kullanıcı "a" veya "A" değeri girmedikçe girilen input değerinin sayı olup olmadığını kontrol etme
# Eğer sayı değilsede hata versin.
"""
while True:
    sayi = input("Bir değer giriniz: ")
    if sayi=="a" or sayi=="A" :
        break
    try:
        sonuc = float(sayi)
        print("Girilen Sayı: \n",sonuc)
        break
    except ValueError as hata:
        print("Geçersiz bir değer girdiniz!\n",hata)
    finally:
        pass
    """
# 3) Girilen parola içerisinde türkçe karakter var ise hata versin.

def parola_kontrol(psw):
    turkce_karakter = "ğüşıöçÖÇĞÜİŞ"
    for i in psw:
        if i in turkce_karakter:
            raise TypeError ("Paralo Türkçe Karakter İçeremez!")
        else:
            pass
    print("Parola Oluşturuldu!")

parola = input("Parola Giriniz: ")
try:
    parola_kontrol(parola)
except TypeError as hata:
    print(hata)