from pydantic import BaseModel
from typing import List

class Lesson(BaseModel):
    lesson_id: int
    topics: str

class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]

class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]

# Each Module has lessons, each course has modules