from sqlmodel import Field, SQLModel
import datetime


class Pos(SQLModel, table=True):
    sentence: str = Field(default=None, primary_key=True)
    date: Field(sa_column=sqlmodel.Column(sqlmodel.DateTime(timezone=True),nullable=False))
