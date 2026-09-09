from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="student-ml-api")


class PredictionInput(BaseModel):
    value: float


def get_version():
    version_file = "VERSION"

    if os.path.exists(version_file):
        with open(version_file, "r") as f:
            return f.read().strip()

    return "1.0.0"


@app.get("/health")
def health():
    version = get_version()

    response = {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": version
    }

    if version == "1.1.0":
        response["model_version"] = "model-1"

    return response


@app.post("/predict")
def predict(payload: PredictionInput):
    prediction = payload.value * 2

    return {
        "input": payload.value,
        "prediction": prediction
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=5000
    )