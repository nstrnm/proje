from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, datavalidation
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/createcou/", response_model=schemas.course)
def create_course(course: schemas.course, db: Session = Depends(get_db)):
    db_course = crud.get_course(course_id = course.cid , db = db)
    if db_course:
        raise HTTPException(status_code=400, detail="course already existed")
    return crud.create_course(db=db, course = course)

@app.get("/getcou/{course_id}", response_model=schemas.course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(course_id = course_id , db = db)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course
 
@app.delete("/delcou/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(course_id = course_id , db = db)
    return db_course






@app.post("/createstu/" , response_model=schemas.student)
def create_student(student: schemas.student , db : Session = Depends(get_db)):
    db_student = crud.get_student(student_id = student.stid , db = db)
    if db_student:
        raise HTTPException(status_code=400 , detail="student already existed")
    return crud.create_student(db=db , student = student)


@app.get("/getstu/{student_id}")
def read_student(student_id : int , db : Session = Depends(get_db)):
    db_student = crud.get_student(student_id = student_id , db = db)
    if db_student is None:
        raise HTTPException(status_code=404 , detail="student not found")
    return db_student

@app.delete("/delstu/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(student_id = student_id , db = db)
    return db_student




@app.post("/createlec/" , response_model=schemas.lecturer)
def create_lecturer(lecturer : schemas.lecturer , db : Session = Depends(get_db)):
    db_lecturer = crud.get_lecturer(lecturer_id = lecturer.lid , db = db)
    if db_lecturer:
        raise HTTPException(status_code=400 , detail="lecturer already existed")
    return crud.create_lecturer(db=db , lecturer = lecturer)



@app.get("/getlec/{lecturer_id}" , response_model=schemas.lecturer)
def read_lecturer(lecturer_id : int , db : Session = Depends(get_db)):
    db_lecturer = crud.get_lecturer(lecturer_id = lecturer_id , db = db)
    if db_lecturer is None:
        raise HTTPException(status_code=404 , detail="lecturer not found")
    return db_lecturer

@app.delete("/dellec/{lecturer_id}")
def delete_lecturer(lecturer_id: int, db: Session = Depends(get_db)):
    db_lecturer = crud.get_lecturer(lecturer_id = lecturer_id , db = db)
    return db_lecturer