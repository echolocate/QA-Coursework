from application import app, db
from application.models import Tasks

@app.route('/create/task')
def create_task():
    new_task = Tasks(description="New Task")
    db.session.add(new_task)
    db.session.commit()
    return f"Task with id {new_task.id} added to database."

@app.route('/read/alltasks')
def read_tasks():
    all_tasks = Tasks.query.all()

    tasks_dict = {"tasks": []}

    for task in all_tasks:
        tasks_dict["tasks"].append(
          {
              "description": task.description,
              "completed": task.completed
          }  
        )
    return tasks_dict

@app.route('/update/task/<int:id>/<new_description>')
def update_task(id, new_description):
    task = Tasks.query.get(id)
    task.description = new_description
    db.session.commit()
    return f"Task {id} updated to {new_description}"