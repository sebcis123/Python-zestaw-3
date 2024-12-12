from dataclasses import dataclass
import json

@dataclass
class DaneOsobowe:
    imie: str
    nazwisko: str
    adres: str
    kod_pocztowy: str
    pesel: str

    def to_json(self) -> str:

        return json.dumps(self.__dict__, ensure_ascii=False)

    @staticmethod
    def from_json(json_data: str) -> 'DaneOsobowe':

        data = json.loads(json_data)
        return DaneOsobowe(**data)

    def save_to_json(self, filename: str):

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.__dict__, file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> 'DaneOsobowe':

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return DaneOsobowe(**data)

if __name__ == "__main__":
    osoba = DaneOsobowe(
        imie="Cristiano",
        nazwisko="Ronaldo",
        adres="Lizbona, ul. Suii 1",
        kod_pocztowy="07-007",
        pesel="12345678901"
    )

    # zapis
    osoba.save_to_json("dane_osobowe.json")

    # odczyt
    nowa_osoba = DaneOsobowe.load_from_json("dane_osobowe.json")
    print("Załadowane dane:", nowa_osoba)
