from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)
    desc = Column(String)
    atk = Column(Integer)
    def_ = Column(Integer)
    image_url = Column(String)
    owned = Column(Integer, default=0)
    wishlist = Column(Boolean, default=False)

class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class DeckCard(Base):
    __tablename__ = "deck_cards"
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey("decks.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))
    quantity = Column(Integer, default=1)
