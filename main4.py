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

#3 feldolgozás listaelem indexe segítségével
i=0
while i<len(tanulok):
    print(f'(i+1). - Tanuló neve: {tanulok[i]["nev"]}, születési ideje: {tanulok[i]["szid"]}, magasság: {tanulok[i]["magassag"]}')

    i+=1





