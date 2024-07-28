from fastapi import FastAPI
import uvicorn
from database import connect

app = FastAPI()


@app.get("/api/test")
def test() -> None:
    return {"msg": "Hello"}


@app.get("/api/routes")
def routes() -> None:
    conn, cursor = connect()
    cursor.execute("SELECT * FROM route")

    res = cursor.fetchall()

    conn.close()

    route_data = []

    for row in res:
        route_data.append({"id": row[0], "route": row[1]})

    return route_data


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
