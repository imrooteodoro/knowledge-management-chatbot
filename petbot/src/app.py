from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.routes import routes


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)

