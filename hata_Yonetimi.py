# print(a) # NameError
# print("deneme"a) # Syntaxerror
# print(5/0) # ZeroDivisionError
# a=int("merhaba") # ValueError

# try
# Hata olma olasılığı beklenilen komutlar bu satır girintisine yazılır.

# except
# Hata olması taktirde çalışacak komutlar bu satır girintisine yazılır.

# finally
# İster hata olsun ister olmasın sürekli olarak çalışmasını istediğimiz komutlar buraya yazılır.
# Veri içerisinde program sonlandıktan sonra veri değişken yapılarının içindeki verileri temizler.

"""
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(f"Girilen Sayıların Bölümü: {x/y}")
except:
    print("Bir Hata Oluştu!")
"""

"""
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    print(f"Girilen Sayıların Bölümü: {x/y}")
except ZeroDivisionError:
    print("Bir sayıyı 0 a bölemezsiniz!")
except ValueError:
    print("Lütfen Sayı Giriniz!")

"""
# while True:

#     try:
#         x = int(input("X: "))
#         y = int(input("Y: "))
#         print(f"Girilen Sayıların Bölümü: {x/y}")
#     except ZeroDivisionError as hata:
#         print("Bir sayıyı 0 a bölemezsiniz!")
#         print(hata)
#     except ValueError as hata:
#         print("Lütfen Sayı Giriniz!")
#         print(hata)
#     else:
#         print("İşlem başarılı bir şekilde gerçkleşti!")
#         break

"""finaly"""
"""
while True:

    try:
        x = int(input("X: "))
        y = int(input("Y: "))
        print(f"Girilen Sayıların Bölümü: {x/y}")
    except (ZeroDivisionError,ValueError) as hata:
        print("Bir hata oluştu:")
        print(hata)
    else:
        print("İşlem başarılı bir şekilde gerçkleşti!")
        break
    finally:
        #print("Önbellek Temizlendi")
        pass

"""

while True:

    try:
        x = int(input("X: "))
        y = int(input("Y: "))
        print(f"Girilen Sayıların Bölümü: {x/y}")
    except Exception as hata:
        print("Bir hata oluştu:")
        print(hata)
    else:
        print("İşlem başarılı bir şekilde gerçkleşti!")
        break
    finally:
        #print("Önbellek Temizlendi")
        pass