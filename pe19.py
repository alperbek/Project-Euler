# -*- coding: cp1254 -*-
gunler={1:"pazartesi",2:"sali",3:"carsamba",4:"persembe",5:"cuma",6:"cumartesi",
        0:"pazar"}
aylar={"ocak":31,"subat":28,"mart":31,"nisan":30,"mayis":31,"haziran":30,
       "temmuz":31,"agustos":31,"eylul":30,"ekim":31,"kasim":30,"aralik":31}


#1 Ocak 1900 Pazar Gunune Denk Gelmis
#Bu nedenle bir onceki gun Cumartesi ve anahtar degeri 6
oncekiGun=6
toplamGun=sum(aylar.values())
kalan=toplamGun % 7
kalan=(kalan+oncekiGun)%7
gun=gunler[kalan] # 1901 yılının ilk gunu bu degiskende

pazar_sayisi=0



def Pazar(yil):
    global oncekiGun,bugun
    global kalan,gun
    global pazar_sayisi
    if(yil % 4 == 0):
        aylar["subat"]=29
    for i in aylar.values():
        
        if(gun == gunler[0]):
            pazar_sayisi+=1
            
        for m,n in gunler.items():
            if (n == gun):
                oncekiGun=m-1
        kalan =i % 7
        kalan=(kalan+oncekiGun)%7
        gun=gunler[kalan]    
    return


for i in range(1901,2000):
    Pazar(i)

print pazar_sayisi # 171
