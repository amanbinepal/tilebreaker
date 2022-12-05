from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["get"])

def homepage():
    with open("score.txt", "r") as my_text_file:
        list = []
        for line in my_text_file:
            list.append(line)
        return render_template("index.html", list=list)

@app.route("/add", methods=["post"])

def add():
    score_value = request.json
    with open("score.txt", "a") as my_text_file:
            my_text_file.write(str(score_value["Score"]))
            my_text_file.write("\n")