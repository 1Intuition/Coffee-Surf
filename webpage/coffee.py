from flask import Flask, render_template
import pickle
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

data =  pickle.load(open("data.p", 'rb'))

posts = [
    {
        "brand":"ACS",
        "name":"best coffee",
        "description":"The best coffee ever",
        "location":"Kenya",
        "roasted":"Medium-light",
        "rating":"94/100"
    },
    {
        "brand":"LOVE",
        "name":"Decaf",
        "description":"The best coffee but decaf",
        "location":"Ethiopia",
        "roasted":"Medium-light",
        "rating":"94/100"
    },
    {
        "brand":"LOVE",
        "name":"Decaf",
        "description":"The best coffee but decaf",
        "location":"Ethiopia",
        "roasted":"Medium-light",
        "rating":"94/100"
    },
    {
        "brand":"LOVE",
        "name":"Decaf",
        "description":"The best coffee but decaf",
        "location":"Ethiopia",
        "roasted":"Medium-light",
        "rating":"94/100"
    }
]

coffee_info = [
    {
        "brand":"McGill Coffee",
        "name":"best coffee",
        "description":"The best coffee ever",
        "roasted_location":"Montreal, Quebec",
        "coffee_origin":"Costa Rica; Honduras; Indonesia",
        "rating":"94/100",
        "latitude": "-40.2839",
        "roast_level": "Medium-Light",
        "agtron":"57/72",
        "price": "NT 249/8 ounces",
        "review date":"November 2022",
        "Aroma":"9/10",
        "Body":"9/10",
        "Flavor":"9/10",
        "Aftertaste":"9/10",
        "With_Milk":"9/10",
        "Blind_Assessment": "A radiant espresso blend that shines equally in the straight shot and in milk, alive with notes of rich dark chocolate and black cherry. | Guji Zone, Oromia Region, south-central Ethiopia",
        "Rating":"94/100",

    },
    {
        "brand":"ACS",
        "name":"best coffee",
        "description":"The best coffee ever",
        "location":"Kenya",
        "roasted":"Medium-light",
        "rating":"94/100"
    },
    {
        "brand":"LOVE",
        "name":"Decaf",
        "description":"The best coffee but decaf",
        "location":"Ethiopia",
        "roasted":"Medium-light",
        "rating":"94/100"
    },
    {
        "brand":"LOVE",
        "name":"Decaf",
        "description":"The best coffee but decaf",
        "location":"Ethiopia",
        "roasted":"Medium-light",
        "rating":"94/100"
    },
    {
        "brand":"LOVE",
        "name":"Decaf",
        "description":"The best coffee but decaf",
        "location":"Ethiopia",
        "roasted":"Medium-light",
        "rating":"94/100"
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",posts=posts)

@app.route("/product")
def product_page():
    return render_template("product.html",posts=coffee_info)


if __name__ == "main":
    app.run(debug=True)