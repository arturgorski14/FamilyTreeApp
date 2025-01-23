from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

FRONTEND_PORT = "8080"
LOCAL_NETWORK_ADDRESSES = [f"http://192.168.0.{x}:{FRONTEND_PORT}" for x in range(100, 131)]


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        f"http://localhost:{FRONTEND_PORT}",
        *LOCAL_NETWORK_ADDRESSES,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Hello": "from FastAPI"}


@app.get("/families")
def get_user_families():
    families = [
        {"name": "Pełna rodzina", "description": "Główne drzewo genealogiczne"},
        {"name": "LOTR", "description": "Wyimaginowane drzewo genealogiczne z LOTRa"},
    ]
    return families
