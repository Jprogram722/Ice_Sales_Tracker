from pydantic import BaseModel
from datetime import datetime


class DaysSchema(BaseModel):
    id: int | None = None
    num_bails_sold: int
    max_tempurature: float | None = None
    num_stops: int | None = None
    route: int | None = None
    date: datetime | None = datetime.now().strftime('%Y-%m-%d')
