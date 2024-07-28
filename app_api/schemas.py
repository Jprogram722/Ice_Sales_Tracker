from pydantic import BaseModel
import datetime


class DaysSchema(BaseModel):
    id: int | None = None
    num_bails_sold: int
    max_tempurature: float
    num_stops: int | None = None
    data: datetime
