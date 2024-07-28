from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/api/test")
def test() -> None:
    return {"msg": "Hello"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)
