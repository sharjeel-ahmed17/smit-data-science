from pydantic import BaseModel, Field
from typing import Literal, Annotated

# pydantic model for input data (validation)
class UserInput(BaseModel):

    attendance: Annotated[float, Field(...,ge=0, lt=100, description="Attendance percentage must be between 0 and 100")]
    assignment_completion: Annotated[float, Field(...,ge=0, lt=100, description="Assignment completion percentage must be between 0 and 100")]
    test_score: Annotated[float, Field(...,ge=0, lt=25, description="Test score must be between 0 and 25")]
    practical_score: Annotated[float, Field(...,ge=0, lt=25, description="Practical score must be between 0 and 25")]
    exam_score: Annotated[float, Field(...,ge=0, lt=50, description="Exam score must be between 0 and 50")]

