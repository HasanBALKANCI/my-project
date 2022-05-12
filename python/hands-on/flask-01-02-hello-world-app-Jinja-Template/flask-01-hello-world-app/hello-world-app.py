from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Hello World from Flasak!</h1>"


@app.route("/second")
def second():
    return "This is my second page"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
    app.run(debug=True, port=2000) 
    # if you don't write anything for port, it accept automatically 5000
    