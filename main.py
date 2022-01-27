from fastapi import FastAPI
from sqlmodel import Session, SQLModel, select
import spacy
from models import Pos
from create_db import engine



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/poss/")
def pos_tag(pos: Pos):
    with Session(engine) as session:
        session.add(pos)
        session.commit()
        session.refresh(pos)        
        text_string = pos.sentence
        doc = nlp(text_string)
        tokens = [token.text for token in doc]
        return tokens

@app.get("/pos/")
def read_poses():
    with Session(engine) as session:
        poses = session.exec(select(Pos)).all()
        return poses
