from fastapi import FastAPI
#import tensorflow as tf



app = FastAPI()

#model = tf.keras.models.load_model('C:\Users\abdal\Downloads\model\app_test\my_ml_project\app\random_forest_model.h5')
#print("Model loaded successfully!")


@app.get("/hello")
def read_hello():
    return {"message": "Hello World! I am here"}
