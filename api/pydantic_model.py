from pydantic import BaseModel
from typing import List
from datetime import date

class Link(BaseModel):
    id: int | None = None
    name: str
    url: str

class Project(BaseModel):
    id: int | None = None
    name: str
    description: str
    image: str = None
    demo_link: Link | List[Link] 

class Certificate(BaseModel):
    id: int | None = None
    name: str
    presented_by: str
    image: str = None
    date: date
    url: str

class Experience(BaseModel):
    id: int | None = None
    company: str
    role: str
    description: str = None
    url: str = None
    start_date: date
    end_date: date = None

class Education(BaseModel):
    id: int | None = None
    name: str
    institution: str
    discipline: str
    description: str = None
    image: str = None
    date: date

class Review(BaseModel):
    id: int | None = None
    name: str
    occupation: str
    review: str
    rating: int
    review_on: str = None
    image: str = None
    date: date

class Skill(BaseModel):
    id: int | None = None
    name: str
    description: str = None
    image: str = None

class Social(BaseModel):
    id: int | None = None
    social: Link | List[Link]

class Contact(BaseModel):
    id: int | None = None
    contant: Link | List[Link]

class User(BaseModel):
    id: int | None = None
    name : str
    position : str
    image : str
    bio : str
    contact : Contact | List[Contact]
    social : List[Social] = None
    skills : List[Skill] = None
    projects : Project | List[Project] = None
    certificates : Certificate | List[Certificate] = None
    experience : Experience | List[Experience] = None
    education : List[Education] = None
    reviews : Review |  List[Review] = None


class Blog(BaseModel):
    id: int | None = None
    title: str
    description: str
    image: str = None
    url: str
    date: date