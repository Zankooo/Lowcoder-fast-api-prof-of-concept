from fastapi import APIRouter
from app.schemas.schemas import UserCreate, XmlFilesRequest
from app.services.services import shrani_userja, vrni_vse_userje, obdelaj_xml_datoteke


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

