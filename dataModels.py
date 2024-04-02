from typing import List
from typing_extensions import TypedDict
from pydantic import BaseModel
 
 
class Doc(TypedDict):
    id:int
    category: str
    content: str
 
Corpus = List[Doc]
 
class Result(BaseModel):
    id: int
    content: str
    category: str
    score: float
 
    def __str__(self):
        """
        Returns a string representation of the result.
        """
        return f"Document ID: {self.id}, Category: {self.category}, Score: {self.score:.2f}\nContent: {self.content}"
    
 