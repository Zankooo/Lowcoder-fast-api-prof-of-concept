import json
import os
import base64
import xml.etree.ElementTree as ET
from fastapi import HTTPException

POT_DO_DATOTEKE = "podatki/uporabniki.json"

def shrani_userja(user):
    os.makedirs("podatki", exist_ok=True)

    nov_uporabnik = {
        "ime": user.ime,
        "telefonska_stevilka": user.telefonska_stevilka,
        "datum_rojstva": str(user.datum_rojstva)
    }

    if os.path.exists(POT_DO_DATOTEKE):
        with open(POT_DO_DATOTEKE, "r", encoding="utf-8") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
    else:
        users = []

    users.append(nov_uporabnik)

    with open(POT_DO_DATOTEKE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

    return {
        "message": f"Uporabnik {user.ime} je shranjen v sistem!"
    }



def vrni_vse_userje():
    if os.path.exists(POT_DO_DATOTEKE):
        with open(POT_DO_DATOTEKE, "r", encoding="utf-8") as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                users = []
    else:
        users = []

    return users


async def obdelaj_xml_datoteke(payload):
    files_base64 = payload.files
    telefonske_stevilke = []

    for i, file_base64 in enumerate(files_base64):
        try:
            if "," in file_base64:
                file_base64 = file_base64.split(",", 1)[1]

            vsebina = base64.b64decode(file_base64)
            xml_text = vsebina.decode("utf-8")
            root = ET.fromstring(xml_text)

            stevilka = root.findtext(".//telefonska_stevilka")
            if stevilka:
                telefonske_stevilke.append(stevilka)

        except ET.ParseError:
            raise HTTPException(
                status_code=400,
                detail=f"Datoteka na indeksu {i} vsebuje neveljaven XML"
            )
        except UnicodeDecodeError:
            raise HTTPException(
                status_code=400,
                detail=f"Datoteka na indeksu {i} ni veljaven UTF-8 XML"
            )
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Napaka pri obdelavi datoteke na indeksu {i}: {str(e)}"
            )

    os.makedirs("podatki", exist_ok=True)
    pot_do_datoteke = "podatki/telefonske_cifre.json"

    obstojece_stevilke = []

    if os.path.exists(pot_do_datoteke):
        with open(pot_do_datoteke, "w", encoding="utf-8") as f:
            json.dump({"telefonske_stevilke": []}, f, ensure_ascii=False, indent=2)

    obstojece_stevilke = []

    vse_stevilke = obstojece_stevilke + telefonske_stevilke

    with open(pot_do_datoteke, "w", encoding="utf-8") as f:
        json.dump(
            {"telefonske_stevilke": vse_stevilke},
            f,
            ensure_ascii=False,
            indent=2
        )

    return {
        "message": "Telefonske številke so bile dodane v datoteko.",
        "telefonske_stevilke": telefonske_stevilke,
        "vse_stevilke": vse_stevilke
    }