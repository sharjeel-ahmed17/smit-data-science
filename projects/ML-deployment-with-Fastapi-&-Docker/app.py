from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output,model, MODEL_VERSION
from schema.user_input import UserInput
from schema.model_output import ModelOutput


#fastapi object
app= FastAPI()

# Grade mapping 
grade_map = {0: "F", 1: "E", 2: "D", 3: "C", 4: "B", 5: "A"}

# end point for home
@app.get("/")
def home():
    return {'message': 'Welcome to the Grade Prediction API'}

# end point for health check (for kubernative deployment )
@app.get("/health")
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model': model is not None
    }

# end point for prediction
@app.post("/predict",response_model=ModelOutput)
def predict(input_data: UserInput):


    #User input ko DataFrame
    user_input = {
        "Attendance (%)": input_data.attendance,
        "Assignment Completion (%)": input_data.assignment_completion,
        "Test Score (25%)": input_data.test_score,
        "Practical Score (25%)": input_data.practical_score,
        "Exam Score (50%)": input_data.exam_score
    }
    
    try:
        # Model prediction
        prediction = predict_output(user_input)
        
        # Convert numeric prediction to grade
        grade = grade_map[int(prediction[0])]
        
        #json format return 
        return JSONResponse(status_code=200,content={"predicted_grade": grade})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
