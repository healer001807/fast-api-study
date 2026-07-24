from  fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# 定义类
class Item(BaseModel):
    name:str
    price:float
    is_offer:bool | None = None

@app.get("/")
def read_root():
    return {"hello world"}

@app.get("/items/{item_id}")
def read_item(item_id:int ,q:str | None=None):
    return {"item_id":item_id,"q":q}

# 异步
@app.get('/read_results')
async def read_results():
    results = await some_library()
    return results


def some_library():
    return {"username":"123"}

# put请求
@app.put("/item/{item_id}")
def update_item(item_id:int ,item:Item):
    return {"item_id":item_id,"item_name":item.name,"item_price":item.price,"item_is_offer":item.is_offer}