# flask를 활용한 간단한 계산기 구현

from flask import Flask, render_template
from flask import request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'
    
@app.route('/calc')
def cal():
    inputdata = request.args.get("inputdata", "")
    if inputdata:
        result = cal(inputdata)
    else:
        result = ""
    return (
        """<form action="" method="get">
                Calc : <input type="text" name="inputdata">
                <input type="submit" value="calc">
            </form>"""
        + "result : " + result
    )

def cal(inputdata):
    return str(eval(inputdata))

if __name__ == "__main__":
    app.run(port=5555, debug=True)
