"""Fantasy acquisition API"""

from fastapi import FastAPI
import onnxruntime as rt
import numpy as np
from schemas import FantasyAcquisitionFeatures, PredictionOutput

api_description = """
This API predicts the range of costs to acquire a player in fantasy football

the endpoints are grouped into the following categories:

## Analytics
Get information about health of the API
 
## Prediction
Get predictions of player acquisition cost.
"""

# Load the ONNX model
sess_10 = rt.InferenceSession("acquisition_model_10.onnx",
                              providers=["CPUExecutionProvider"])
sess_50 = rt.InferenceSession("acquisition_model_50.onnx",
                              providers=["CPUExecutionProvider"])
sess_90 = rt.InferenceSession("acquisition_model_90.onnx",
                              providers=["CPUExecutionProvider"])

