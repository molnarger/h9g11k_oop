from abc import ABC, abstractmethod
from datetime import datetime


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def get_tipus(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

    def get_tipus(self):
        return "Egyágyas"


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

    def get_tipus(self):
        return "Kétágyas"


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return szoba.ar
        return None

    def foglalas_lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")


# Szálloda, szobák és foglalások inicializálása
szalloda = Szalloda("Harmónia Szálloda")
szalloda.szoba_hozzaad(EgyagyasSzoba("101"))
szalloda.szoba_hozzaad(KetagyasSzoba("201"))
szalloda.szoba_hozzaad(KetagyasSzoba("202"))
szalloda.foglalas("101", datetime(2024, 5, 3))
szalloda.foglalas("201", datetime(2024, 5, 5))
szalloda.foglalas("202", datetime(2024, 5, 6))
szalloda.foglalas("202", datetime(2024, 8, 20))
szalloda.foglalas("202", datetime(2024, 9, 15))

# Felhasználói interfész
print("Üdvözöljük a Harmónia Szállodában!")
while True:
    print("\nVálasszon műveletet:")
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("0. Kilépés")
    valasztas = input("Művelet kiválasztása: ")

    if valasztas == "1":
        szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
        datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            if datum < datetime.now():
                print("Hibás dátum! A foglalás csak jövőbeli dátumra lehetséges.")
                continue
            ar = szalloda.foglalas(szobaszam, datum)
            if ar is not None:
                print(f"A foglalás sikeres! Az ár: {ar} Ft.")
            else:
                print("Nincs ilyen szobaszám!")
        except ValueError:
            print("Hibás dátum formátum!")

    elif valasztas == "2":
        szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
        datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            sikeres = szalloda.foglalas_lemondas(szobaszam, datum)
            if sikeres:
                print("A foglalás sikeresen lemondva.")
            else:
                print("Nem található ilyen foglalás.")
        except ValueError:
            print("Hibás dátum formátum!")

    elif valasztas == "3":
        print("\nFoglalások:")
        szalloda.foglalasok_listazasa()

    elif valasztas == "0":
        print("Köszönjük, hogy a Harmónia Szállodát választotta! Viszlát!")
        break

    else:
        print("Hibás választás! Kérjük, válasszon a rendelkezésre álló lehetőségek közül.")
