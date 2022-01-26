import nltk
from fastapi import FastAPI
from sqlmodel import Session, SQLModel, select
from models import Pos
from create_db import engine



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/pos/")
def pos_tag(pos: Pos):
    with Session(engine) as session:
        session.add(pos)
        session.commit()
        session.refresh(pos)
        sentence = pos.sentence
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        return tagged

@app.get("/pos/")
def read_poses():
    with Session(engine) as session:
        poses = session.exec(select(Pos)).all()
        return poses