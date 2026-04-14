from typing import List
from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    ime: str
    telefonska_stevilka: str
    datum_rojstva: date


class XmlFilesRequest(BaseModel):
    files: list[str]


class XlsxBase64Request(BaseModel):
    files: list[str]