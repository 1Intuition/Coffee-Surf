from flask import Flask, render_template
import pickle
app = Flask(__name__)

data =  pickle.load(open("data.p", 'rb'))

posts = list(data.values())[0:5]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",posts=posts)

@app.route("/product")
def product_page():
    return render_template("product.html",posts=posts)


if __name__ == "main":
    app.run(debug=True)