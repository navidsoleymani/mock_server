from pydantic import BaseModel


class SpiderSchema(BaseModel):
    pk: int = 1
    name: str = 'spider'
    description: str | None = 'for sample'
