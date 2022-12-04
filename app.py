from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["get"])

def homepage():
    with open("score.txt", "r") as my_text_file:
        list = []
        for line in my_text_file:
            list.append(line)
        return render_template("index.html", list=list)