from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def read_hello():
    return {"message": "Hello World! I m abdallah alzoghby is update  and now  and zamelak"}
