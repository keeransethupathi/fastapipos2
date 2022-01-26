from sqlmodel import Field, SQLModel


class Pos(SQLModel, table=True):
    sentence: str = Field(default=None, primary_key=True)