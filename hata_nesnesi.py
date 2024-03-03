"""raise"""
# Python programlama dilinde olmayan hata nesneleri oluşturmamızı sağlar.

# x = 10

# if x > 5:
#     raise Exception ("X değeri 5 ten büyük olamaz!")

def paralo_kontrol(psw):
    import re

    if len(psw) < 8:
        raise Exception ("En az 8 karakterli bir şifre giriniz!")
    
    elif not re.search("[a-z]",psw):
        raise Exception ("Parolanız Küçük Harf İçermelidir!")
    elif not re.search("[A-Z]",psw):
        raise Exception ("Parolanız Büyük Harf İçermelidir!")
    elif not re.search("[\d]",psw): # Rakam decimal
    # elif not re.search("[0-9]",psw):#rakam
        raise Exception("Parolanız Rakam İçermelidir!")
    elif not re.search("[@#$½{/*-+!^+%&/(=_:;><}\"]]",psw):
        raise Exception("Parolanız Özel Karakter İçermelidir!")
    elif not re.search("[\s]",psw): # Boşluk
        raise Exception("Parolanız Boşluk Karakter İçermelidir!")

while True:
    parola = input("Parola Giriniz: ")

    try:
        paralo_kontrol(parola)
    except Exception as hata:
        print(hata)
    else:
        print("Parolanız Güçlü Parola Oluşturma İlkelerini Karşılıyor!")
        break
    finally:
        pass

import re
def parola_kontol():
	passwd = input("Bir şifre giriniz:")
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	
	# compiling regex
	pat = re.compile(reg)
	
	# searching regex				 
	mat = re.search(pat, passwd)
	
	# validating conditions
	if mat:
		print("Password is valid.")
	else:
		print("Password invalid !!")

# Driver Code	 
if __name__ == '__main__':
	parola_kontol()
    
    
"""
import re

def main():
	passwd = input("Bir şifre giriniz:")
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
  
  Bu regular expression, bir parolanın belirli karmaşıklık kurallarına uymasını sağlamak için kullanılır. İşte bu ifadenin her bir bölümünün açıklaması:

^: Girişin başlangıcını belirtir.

(?=.*[a-z]): Bu bir "positive lookahead" ifadesidir ve en az bir küçük harf içermesi gerektiğini belirtir.

(?=.*[A-Z]): Yine bir "positive lookahead" ifadesidir ve en az bir büyük harf içermesi gerektiğini belirtir.

(?=.*\d): Bir başka "positive lookahead" ifadesidir ve en az bir rakam içermesi gerektiğini belirtir.

(?=.*[@$!%*#?&]): Yine bir "positive lookahead" ifadesidir ve en az bir özel karakter içermesi gerektiğini belirtir. Burada kullanılan özel karakterler: @ $ ! % * # ? &

[A-Za-z\d@$!#%*?&]{6,20}: Bu kısım, parolanın uzunluğunu belirtir. En az 6 karakter ve en fazla 20 karakter içermelidir. A-Za-z\d@$!#%*?& ifadesi, parolanın sadece bu karakterleri içermesine izin verir.

$: Girişin sonunu belirtir.

Bu ifade, bir parolanın en az bir küçük harf, bir büyük harf, bir rakam, bir özel karakter içermesi ve belirli bir uzunluk aralığında olması gerektiğini kontrol eder. Özel karakterler ve uzunluk sınırları ihtiyaca göre değiştirilebilir.
	
	# compiling regex
	pat = re.compile(reg)
	
	# searching regex				 
	mat = re.search(pat, passwd)
	
	# validating conditions
	if mat:
		print("Password is valid.")
	else:
		print("Password invalid !!")

# Driver Code	 
if __name__ == '__main__':
	main()
""" 
    