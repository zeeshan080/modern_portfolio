from typing import Dict, List
from fastapi import FastAPI
from pydantic_model import (
    Project,
    User,
    Blog,
    Skill,
    Social,
    Experience,
    Education,
    Certificate,
)

app = FastAPI()


@app.get("/status")
def status():
    return {"message": "Hello World from FastAPI"}


# GET METHODS
@app.get("/user")
def user() -> User:
    return {"message": "John Doe"}


@app.get("/projects")
def projects() -> List[Project]:
    return [
        {
            "name": "My Project",
            "description": "This is a project description",
            "demo_link": [
                {"id": 1, "name": "Demo 1", "url": "https://demo1.com"},
                {"id": 2, "name": "Demo 2", "url": "https://demo2.com"},
            ],
        }
    ]


@app.get("/projects/{project_id}")
def project(project_id: int) -> Project:
    return {
        "id": project_id,
        "name": "My Project",
        "description": "This is a project description",
        "demo_link": [
            {"id": 1, "name": "Demo 1", "url": "https://demo1.com"},
            {"id": 2, "name": "Demo 2", "url": "https://demo2.com"},
        ],
    }


@app.get("/blogs")
def blogs() -> List[Blog]:
    return {"message": "Blogs"}


@app.get("/blogs/{blog_id}")
def blog(blog_id: int) -> Blog:
    return {"message": f"Blog with id {blog_id}"}


# POST METHODS
@app.post("/projects")
def create_project(project: Project) -> Dict[str, str | int]:
    return {"message": f"Project {project.name} created successfully", "id": 1}


@app.post("/skills")
def create_skill(skill: Skill) -> Dict[str, str | int]:
    return {"message": f"Skill {skill.name} created successfully", "id": 1}


@app.post("/social")
def create_social(social: Social) -> Dict[str, str | int]:
    return {"message": f"Social {social.name} created successfully", "id": 1}


@app.post("/experience")
def create_experience(experience: Experience) -> Dict[str, str | int]:
    return {"message": f"Experience {experience.name} created successfully", "id": 1}


@app.post("/education")
def create_education(education: Education) -> Dict[str, str | int]:
    return {"message": f"Education {education.name} created successfully", "id": 1}


@app.post("/certificates")
def create_certificate(certificate: Certificate) -> Dict[str, str | int]:
    return {"message": f"Certificate {certificate.name} created successfully", "id": 1}


@app.post("/blogs")
def create_blog(blog: Blog) -> Dict[str, str | int]:
    return {"message": f"Blog {blog.title} created successfully", "id": 1}


# DELETE METHODS
@app.delete("/projects/{project_id}")
def delete_project(project_id: int) -> Dict[str, str | int]:
    return {"message": f"Project with id {project_id} deleted successfully", "id": 1}


@app.delete("/skills/{skill_id}")
def create_skill(skill_id: int) -> Dict[str, str | int]:
    return {"message": f"Skill {skill_id} deleted successfully", "id": 1}


@app.delete("/social/{social_id}")
def create_social(social_id: int) -> Dict[str, str | int]:
    return {"message": f"Social {social_id} deleted successfully", "id": 1}


@app.delete("/experience/{experience_id}")
def create_experience(experience_id: int) -> Dict[str, str | int]:
    return {"message": f"Experience {experience_id} deleted successfully", "id": 1}


@app.delete("/education/{education_id}")
def create_education(education_id: int) -> Dict[str, str | int]:
    return {"message": f"Education {education_id} deleted successfully", "id": 1}


@app.delete("/certificates/{certificate_id}")
def create_certificate(certificate_id: int) -> Dict[str, str | int]:
    return {"message": f"Certificate {certificate_id} deleted successfully", "id": 1}


@app.delete("/blogs")
def create_blog(blog: Blog) -> Dict[str, str | int]:
    return {"message": f"Blog {blog.title} deleted successfully", "id": 1}


# PUT METHODS
@app.put("/projects/{project_id}")
def update_project(project_id: int, project: Project) -> Dict[str, str | int]:
    return {"message": f"Project {project_id} updated successfully", "id": 1}

@app.put("/skills/{skill_id}")
def update_skill(skill_id: int, skill: Skill) -> Dict[str, str | int]:
    return {"message": f"Skill {skill_id} updated successfully", "id": 1}

@app.put("/social/{social_id}")
def update_social(social_id: int, social: Social) -> Dict[str, str | int]:
    return {"message": f"Social {social_id} updated successfully", "id": 1}

@app.put("/experience/{experience_id}")
def update_experience(experience_id: int, experience: Experience) -> Dict[str, str | int]:
    return {"message": f"Experience {experience_id} updated successfully", "id": 1}

@app.put("/education/{education_id}")
def update_education(education_id: int, education: Education) -> Dict[str, str | int]:
    return {"message": f"Education {education_id} updated successfully", "id": 1}

@app.put("/certificates/{certificate_id}")
def update_certificate(certificate_id: int, certificate: Certificate) -> Dict[str, str | int]:
    return {"message": f"Certificate {certificate_id} updated successfully", "id": 1}

@app.put("/blogs/{blog_id}")
def update_blog(blog_id: int, blog: Blog) -> Dict[str, str | int]:
    return {"message": f"Blog {blog_id} updated successfully", "id": 1}
