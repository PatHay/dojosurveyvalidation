from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if len(request.form['name']) < 1 or len(request.form['comment']) < 1:
        flash("Name and/or Comments cannot be blank!")
        return redirect('/')
    if len(request.form["comment"]) > 121:
        flash("Comment field cannot be longer than 120 characters")
        return redirect('/')
    name = request.form["name"]
    location = request.form["location"]
    food = request.form["food"]
    comment = request.form["comment"]
    return render_template("results.html", name = name, location = location, food = food, comment = comment)

app.run(debug=True)