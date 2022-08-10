from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
from utils import parse_request
import texthero as hero
import pickle
import os

class Product(BaseModel):
    title: str

class ProductRequest(BaseModel):
    products: List[Product]

class ProductResponse(BaseModel):
    categories: List[str]

application = FastAPI(title="Product classification API", 
                      description="API for product classification", version="1.0")

model_path = os.environ['MODEL_PATH']
model = pickle.load(open(model_path, 'rb'))

@application.post("/predict", response_model=ProductResponse,
                      description="Get a classification from model")
async def create_item(item: ProductRequest):

    dict_pred = parse_request(item)
    dataframe = pd.DataFrame(dict_pred)
    
    dataframe['title'] = dataframe['title'].pipe(hero.clean)
    list_predicts = model.predict(dataframe)
        
    return {"categories": list(list_predicts)}