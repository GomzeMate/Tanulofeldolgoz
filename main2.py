#0
print("Tanulók kezelése.")

#1
tanulok = []

while True:
    print("\nKérem a tanuló adatait:")
    nev=input("Tanuló neve: ")
    szid=input("Születési idő: ")
    magassag = int(input("Magassag: "))

    tanulo = (nev, szid, magassag)
    tanulok.append(tanulo)

    valasz=input("További tanuló (igen/nem): ")
    if valasz.lower() != "igen":
        break

#3 feldolgozás listaelem indexe segítségével
i=0
while i<len(tanulok):
    print(f"Tanuló neve: {tanulok[i][0]}, születési ideje: {tanulok[i][1]}, magasság: {tanulok[i][2]}")

    i+=1




for item in tanulok:
    print(f"Tanuló neve: {item[0]}, születési ideje: {item[1]}, magasság: {item[2]}")
