from typing import List
from typing_extensions import TypedDict
from pydantic import BaseModel
 
 
class Doc(TypedDict):
    id:int
    tipo: str
    title: str
    year: int
    url: str
    authors: str
    abstract: str
 
Corpus = List[Doc]
 
class Result(BaseModel):
    id: int
    tipo: str
    title: str
    year: int
    url: str
    authors: str
    abstract: str
    score: float
 
    # def __str__(self):
    #     """
    #     Returns a string representation of the result.
    #     """
    #     return f"Document ID: {self.id}, Category: {self.category}, Score: {self.score:.2f}\nContent: {self.content}"
    
 