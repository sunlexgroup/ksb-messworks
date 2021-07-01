from pydantic import BaseModel


class TagDescription(BaseModel):
    tag: str
    description: str

    class Config:
        orm_mode = True