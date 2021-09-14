from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

@app.get("/")
def root (): 
    return {"Message": "Hello World!"} # Returning a Python dictionary with key:value pair

@app.get("/about")
def about ():
    return {"Data": "About" }


inventory = {} # Allows the user to pass input

@app.get ("/get-item/{item_id}") 
def get_item (item_id: int = Path(None, description = "The ID of the item you would like to view")):
    return inventory [item_id]

@app.get ("/get-by-name/") # GET query to allow a user to pass a string and integer for ID. It will return the item ID if it is equal to the item within inventory, otherwise it will return 'Not found'
def get_item (item_id: int, name: str = None  ):
    for item_id in inventory:
        if inventory[item_id].name == name: 
            return inventory[item_id] 
    return {"Data": "Not found"}

@app.post ("/create-item/{item_id}")
def create_item(item_id:int, item: Item): 
    if item_id in inventory: 
        return {"Error": "Item ID already exists"}
          
    inventory[item_id] = item
    return inventory[item_id]
