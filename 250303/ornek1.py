bagaj=int(input("toplam bagaj miktarı giriniz"))
if bagaj <=20:
    print("herhangi bir ücret ödemeniz gerekmiyor")
else:
    fark=bagaj-20
    print(" fazla bagaj için  10*fark tl ödemelsiniz" )
print("iyi yolculuklar")