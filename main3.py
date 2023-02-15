#0
print("Tanulók kezelése.")

#1
tanulok = []

while True:
    print("\nKérem a tanuló adatait:")
    tanulo={}
    tanulo["nev"]=input("Tanuló neve: ")
    tanulo["szid"]=input("Születési idő: ")
    tanulo["magassag"] = int(input("Magassag: "))

    tanulok.append(tanulo)

    valasz=input("További tanuló (igen/nem): ")
    if valasz.lower() != "igen":
        break

#3 feldolgozás lista alias elem (item) segítségével
for item in tanulok:
    #!!!!! Figyeljünk arra hogy az f string és a kulcsoknak a határolói különbözőek.
    print(f'Tanuló neve: {item["nev"]}, születési ideje: {item["szid"]}, magasság: {item["magassag"]}')
