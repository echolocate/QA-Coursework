from application import app, db
from application.models import Tasks
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    return render_template('index.html', title="Home", all_tasks=all_tasks)

@app.route('/create/task')
def create_task():
    new_task = Tasks(description="New new new Task")
    db.session.add(new_task)
    db.session.commit()
    return f"Task with id {new_task.id} added to database."

@app.route('/read/alltasks')
def read_tasks():
    all_tasks = Tasks.query.all()
    tasks_dict = {"tasks":[]}
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

@app.route('/delete/task/<int:id>')
def delete(id):
    id_to_delete = Tasks.query.get(id)
    db.session.delete(id_to_delete)
    db.session.commit()
    return f"Deleted {id}"

@app.route('/completed/<int:id>')
def completed(id):
    task = Tasks.query.get(id)
    task.completed = True
    db.session.commit()
    return f"Task {id} marked as completed"

@app.route('/incomplete/<id>')
def incomplete(id):
    task = Tasks.query.get(id)
    task.completed = False
    db.session.commit()
    return f"Task {id} marked as incomplete"