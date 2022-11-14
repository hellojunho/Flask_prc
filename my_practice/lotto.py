from flask import Flask, render_template
from flask import request
import random

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/lotto')
def lotto():
    lotto_list = list(range(1, 46))
    lotto = sorted(random.sample(lotto_list, 6))
    return render_template("lotto.html", variable=lotto)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
