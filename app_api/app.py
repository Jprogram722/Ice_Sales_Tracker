from fastapi import FastAPI
import uvicorn
from database import connect
from schemas import DaysSchema
from controllers import insert_into_days_table

app = FastAPI()


@app.get("/api/routes")
def routes():
    conn, cursor = connect()
    cursor.execute("SELECT * FROM route")

    res = cursor.fetchall()

    conn.close()

    route_data = []

    for row in res:
        route_data.append({"id": row[0], "route": row[1]})

    return route_data


@app.post("/api/days_info")
def record_day_info(days_data: DaysSchema):
    res = insert_into_days_table(days_data)
    return res


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
