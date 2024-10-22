from fastapi import FastAPI
import joblib  
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the model using joblib
model = joblib.load("model/model.joblib")  

# Define a request body schema
class InputData(BaseModel):
    data: list

# Define a route for the root
@app.get("/hello")
def read_hello():
    return {"message": "Hello World! the model is done ,thanks you "}

# Define a route for making predictions
@app.post("/predict")
def predict(input_data: InputData):
    # Assuming the model expects a 2D array input
    data = input_data.data
    predictions = model.predict([data])
    return {"predictions": predictions.tolist()}
