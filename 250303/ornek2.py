urun1=int(input("ürünün toplam fiyatı giriniz"))
urun2=int(input("ürünün toplam fiyatı giriniz"))
toplam=urun1+urun2
if toplam <=200:
    print("ödenecek ", toplam)
else:
    odeme=toplam*0,75
    print("ödenecek mitar,odeme")