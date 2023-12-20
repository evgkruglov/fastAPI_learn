from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# запуск через uvicorn main:app --reload
@app.get("/")
async def index():
    return FileResponse("index.html")

if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)
