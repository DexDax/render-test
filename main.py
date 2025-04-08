from fastapi import FastAPI

app = FastAPI()

@app.get("/receive-text/")
async def receive_text(text: str):
    return {"message": f"I received '{text}'!"}
