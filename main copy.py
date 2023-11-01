from fastapi import FastAPI
import os

class MYAPI():
    def __init__(self) -> None:
        self.api = FastAPI()
        os.system(f"uvicorn {os.path.basename(__file__)}:MYAPI.api --reload")


    def dssdata(self):
        self.vendas = { 1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
            2:{"item": "garrafa 2L", "preco_unitario": 15, "quantidade":5},
            3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade":5},
            4: {"item": "lata mini", "preco_unitario": 2, "quantidade":5}, }
        
        @self.api.get('/')
        def main():
            return "Main Page"

        @self.api.get('/tailskko')
        def tailskko():
            return "tailskko"

        @self.api.get("/users/{name}")
        def get_user(name: str):
            return {"user": {"name": name}}
        

var1 = MYAPI()