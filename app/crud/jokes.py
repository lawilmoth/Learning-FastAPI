from sqlalchemy.orm import Session

from .. import models
from .. import schemas

def get_jokes(db: Session, response_model=list[schemas.Joke]):
    return db.query(models.Joke).all()

def get_joke(db: Session, joke_id:int):
    return db.query(models.Joke).filter(models.Joke.id == joke_id).first()

def create_joke(db:Session, joke: schemas.JokeCreate):
    db_joke = models.Joke(**joke.model_dump())
    db.add(db_joke)
    db.commit()
    db.refresh(db_joke)
    return db_joke

def delete_joke(db:Session, joke_id:int):
    joke = db.query(models.Joke).filter(models.Joke.id == joke_id).first()
    if joke:
        db.delete(joke)
        db.commit()
    return joke