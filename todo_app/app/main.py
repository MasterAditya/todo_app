from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/templates"), name="static")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, filter: str = "all", db: Session = Depends(get_db)):
    if filter == "active":
        todos = db.query(models.Todo).filter(models.Todo.completed == False).all()
    elif filter == "completed":
        todos = db.query(models.Todo).filter(models.Todo.completed == True).all()
    else:
        todos = db.query(models.Todo).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "todos": todos,
        "filter": filter
    })

@app.post("/add")
def add_todo(title: str = Form(...), db: Session = Depends(get_db)):
    todo = models.Todo(title=title)
    db.add(todo)
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.post("/complete/{todo_id}")
def complete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        # Toggle the 'completed' status explicitly
        todo.completed = not todo.completed
        db.commit()
    return RedirectResponse("/", status_code=303)

@app.post("/delete/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")