from flask import Flask, render_template
import pickle
app = Flask(__name__)

data =  pickle.load(open("data.p", 'rb'))
keys = pickle.load(open("keys.p", 'rb'))

posts = list(data.values())[0:5]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",posts=posts)

@app.route("/product")
def product_page():
    return render_template("product.html",posts=posts)

@app.route("/product/<coffee_name>")
def coffee_page(coffee_name):
    index = keys[coffee_name]
    print(index)
    recommendations = [data[index]]
    recommendations.extend([data[i] for i in data[index]["recommendations"]])
    print(recommendations[0])
    return render_template("product.html",coffees=recommendations)

if __name__ == "main":
    app.run(debug=True)