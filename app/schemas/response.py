from pydantic import BaseModel

class UUIDResponse(BaseModel):
    uuid: str

class CatResponse(BaseModel):
    cat_image_url: str
