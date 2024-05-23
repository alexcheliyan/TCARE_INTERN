
from fastapi import FastAPI,Path,Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url:HttpUrl
    name:str
class Item(BaseModel):
    name:str
    description:str | None=None
    price:int
    tax:int |None = None
    tags: list[str]=[]
    image: list[Image] | None=None

@app.put("/items/{item_id")
async def update_items(item_id:int,item:Item):
    results = {"item_id":item_id,"item":item}
    return results
