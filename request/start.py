from flask import Flask, request

app = Flask(__name__)

@app.route('/method', method=['GET', 'POST'])
def echo_method():
    return request.method, 200

if __name__ == "__main__":
    app.run(port=5555, debug=True)
