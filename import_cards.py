import requests
from sqlalchemy.orm import Session
from models import Card, Base
from main import engine, SessionLocal

Base.metadata.create_all(bind=engine)

def import_cards():
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    response = requests.get(url)
    data = response.json()["data"]

    db: Session = SessionLocal()

    for card in data:  # alle Karten
        new_card = Card(
            name=card["name"],
            type=card["type"],
            desc=card["desc"],
            atk=card.get("atk", 0),
            def_=card.get("def", 0),
            image_url=card["card_images"][0]["image_url"]
        )
        db.merge(new_card)

    db.commit()
    db.close()

if __name__ == "__main__":
    import_cards()
