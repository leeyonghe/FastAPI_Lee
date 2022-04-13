from typing import Optional
from fastapi import FastAPI
from starlette.responses import FileResponse 

app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse('index.html')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}