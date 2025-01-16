from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://username:password@cluster0.tfiqy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.task_manager  # Use the task_manager database
tasks_collection = db.tasks  # Use the tasks collection

@app.route("/")
def index():
    tasks = list(tasks_collection.find())
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task_name = request.form.get("task_name")
        task_description = request.form.get("task_description")
        tasks_collection.insert_one({"name": task_name, "description": task_description, "completed": False})
        return redirect(url_for("index"))
    return render_template("add_task.html")

@app.route("/edit/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if request.method == "POST":
        task_name = request.form.get("task_name")
        task_description = request.form.get("task_description")
        completed = request.form.get("completed") == "on"
        tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"name": task_name, "description": task_description, "completed": completed}})
        return redirect(url_for("index"))
    return render_template("edit_task.html", task=task)

@app.route("/delete/<task_id>")
def delete_task(task_id):
    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
