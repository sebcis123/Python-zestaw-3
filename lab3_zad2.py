import json

class DaneOsobowe:
    def __init__(self, imie, nazwisko, adres, kod_pocztowy, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.kod_pocztowy = kod_pocztowy
        self.pesel = pesel

    def to_dict(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "adres": self.adres,
            "kod_pocztowy": self.kod_pocztowy,
            "pesel": self.pesel
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            imie=data["imie"],
            nazwisko=data["nazwisko"],
            adres=data["adres"],
            kod_pocztowy=data["kod_pocztowy"],
            pesel=data["pesel"]
        )

    def save_to_json(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return cls.from_dict(data)

if __name__ == "__main__":
    osoba = DaneOsobowe("Cristiano", "Ronaldo", "Lizbona, ul. Suii 1", "07-007", "12345678901")

    # zapis
    osoba.save_to_json("dane_osobowe.json")

    # odczyt
    nowa_osoba = DaneOsobowe.load_from_json("dane_osobowe.json")
    print(nowa_osoba.imie, nowa_osoba.nazwisko, nowa_osoba.adres, nowa_osoba.kod_pocztowy, nowa_osoba.pesel)