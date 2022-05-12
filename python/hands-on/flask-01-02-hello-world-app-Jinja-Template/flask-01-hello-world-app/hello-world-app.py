from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Hello World from Flask!</h1>"


@app.route("/second")
def second():
    return "This is my second page"
    # You can see this localhost:2000/second

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"
    # you can see above h2 in web page 'localhost:2000/third/subthird

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'
    # it returns what you write in {...}, it is changeable.


if __name__ == "__main__":
    app.run(debug=True, port=2000) 
    # if you don't write anything for port, it accept automatically 5000
    