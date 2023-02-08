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

#3 feldolgozás lista alias elem (item) segítségével
for item in tanulok:
    print(f"Tanuló neve: {item[0]}, születési ideje: {item[1]}, magasság: {item[2]}")
