from flask import Flask, request ,render_template

app = Flask(__name__)

#TODO make the README.md for this exercise for better explanation

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        # grab A and B from the page
        a = int(request.form.get("a"))
        b = int(request.form.get("b"))
        #Make C equal to the result of the equation
        c = a + b  
        # With post we render the page and also send variable C to the page
        return render_template("index.html", c = c)
    else:
        # if no POST method is requested render only the page.
        return render_template("index.html")

if __name__=='__main__':
    app.run()