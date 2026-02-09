from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 紅包獎池
prizes = [
    "10 元紅包",
    "20 元紅包",
    "50 元紅包",
    "100 元紅包",
    "糖果一包",
    "小玩具一個"
]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result="尚未抽獎")

@app.route("/draw", methods=["POST"])
def draw():
    result = random.choice(prizes)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

