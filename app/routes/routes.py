from fastapi import APIRouter
from app.schemas.schemas import UserCreate, XmlFilesRequest, XlsxBase64Request
from app.services.services import shrani_userja, vrni_vse_userje, obdelaj_xml_datoteke, obdelaj_xlsx


router = APIRouter()


@router.get("/")
def root():
    return {"message": "Poslano iz backenda, backend deala"}


@router.post("/users")
def ustvari_userja(user: UserCreate):
    return shrani_userja(user)


@router.get("/users")
def vrni_vse_uporabnike():
    return vrni_vse_userje()


@router.post("/xml")
async def sprejmi_xml_datoteke(payload: XmlFilesRequest):
    return await obdelaj_xml_datoteke(payload)

@router.post("/xlsx")
async def extract_contacts_base64(payload: XlsxBase64Request):
    return obdelaj_xlsx(payload)
