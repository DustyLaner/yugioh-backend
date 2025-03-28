from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Card
from pydantic import BaseModel
from fastapi import HTTPException

DATABASE_URL = "sqlite:///./yugioh.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 🌍 CORS aktivieren (für mobile Geräte im WLAN)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Für mehr Sicherheit später auf bestimmte IPs beschränken
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Yu-Gi-Oh API läuft!"}

@app.get("/cards")
def get_cards():
    db = SessionLocal()
    cards = db.query(Card).all()
    return cards

class CardUpdate(BaseModel):
    owned: int

@app.put("/cards/{card_id}")
def update_card(card_id: int, update: CardUpdate):
    db = SessionLocal()
    card = db.query(Card).filter(Card.id == card_id).first()

    if not card:
        raise HTTPException(status_code=404, detail="Karte nicht gefunden")

    card.owned = update.owned
    db.commit()
    db.refresh(card)
    return card
