import datetime
from sqlmodel import Field, SQLModel
from datetime import datetime, timedelta

class Pos(SQLModel, table=True):
    sentence: str = Field(default=None, primary_key=True)
    time: datetime = Field((datetime.utcnow() + timedelta(hours=5, minutes=30)).strftime('%d-%b-%y %H:%M:%S'))
