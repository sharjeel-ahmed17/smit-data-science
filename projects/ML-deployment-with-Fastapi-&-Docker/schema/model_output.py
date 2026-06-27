from pydantic  import BaseModel, Field

# validation of output data from model
class ModelOutput(BaseModel):
    predicted_grade: str = Field(..., description="Predicted grade for the student")