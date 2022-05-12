from flask import Flask, render_template
# it means take render_temlate, rent it.

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=7000, number2=9000)

@app.route("/sum")
def number():
    num1 = 23
    num2 = 54
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)



if __name__== "__main__":
    app.run(debug=True, port=4000)
    # i use macos and default port 5000 is busy, so i use port 2000