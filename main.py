from fastapi import FastAPI

# 1. Initialize the application (The brain communicating with Uvicorn)
app = FastAPI()

# 2. Create a basic route (The Hello World)
# When Uvicorn receives a visitor at the main door ("/"), it triggers this.
@app.get("/")
def read_root():
    return {"message": "Hello World! This is my first cloud container 🚀"}

# 3. Create a route returning static data
# When Uvicorn receives a visitor asking for "/data", it returns this JSON.
@app.get("/data")
def get_data():
    return {
        "user": "Analyst_01",
        "role": "Data Scientist",
        "status": "Learning Docker"
    }