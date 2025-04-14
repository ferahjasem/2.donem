sayi1=int(input("sayı gır"))
sayi2=int(input("sayı gır"))
islem=input("işlem secin(+,-,*,/):")
if islem=="+":
    sonuc=sayi1+sayi2
    print("sonuc")
elif islem=="-":
    sonuc=sayi1-sayi2
    print("sonuc")
elif islem=="*":
    sonuc=sayi1*sayi2
    print("sonuc")
elif islem=="/":
    sonuc=sayi1/sayi2
    print("sonuc")
else:
    print("yanlıs işlem girdiniz")
