import joblib   
import pandas as pd
from starlette.responses import JSONResponse



#import the model & scaler
with open("model/bagging.pkl", "rb") as f:
    model = joblib.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = joblib.load(f)    

# For ML Flow 
MODEL_VERSION = "1.0.0"


# Function for prediction
def predict_output(user_input:dict):

    #input conversion to dataframe
    input_df=pd.DataFrame([user_input])

    # Scaler apply 
    input_scaled = scaler.transform(input_df)
    
    # Model prediction
    prediction  = model.predict(input_scaled)

    return prediction
