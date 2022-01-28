from sqlmodel import Field, SQLModel
import datetime


class Pos(SQLModel, table=True):
    sentence: str = Field(default=None, primary_key=True)
    date: datetime.datetime.now()
