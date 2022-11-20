from flask import Flask, request, redirect, render_template
import pickle
import pandas as pd

app = Flask(__name__, template_folder="templates", static_folder="static")

DISPLAY_MAX_RESULTS = 50


data = pickle.load(open("data.p", "rb"))

@app.route("/")
def route_search():
    search_query = request.args.get("q", type=str)
    query_page = request.args.get("page", type=int)  # starts from 1

    # get result data with function:...
    result_data = data

    num_pages = ((len(result_data) - 1) // DISPLAY_MAX_RESULTS) + 1  # 0 if 0 data else 1, 2, etc
    if query_page <= 0 or query_page > num_pages:  # invalid page arg set to None
        query_page = None

    if query_page is None:
        result_data[0:DISPLAY_MAX_RESULTS]
    else:
        result_data[DISPLAY_MAX_RESULTS*(query_page-1):DISPLAY_MAX_RESULTS*query_page]

    if search_query is None:
        return render_template("index.html",
                               is_product_page=False,
                               search_results=len(cropped_result_data),
                               data=cropped_result_data,
                               this_page=3,  # integer denoting the page number, starting at 1!!!
                               num_pages=6,  # integer denoting the number of total pages
                               next_page_link=None   # None if there are no more pages, string of next page otherwise
                               )

    return render_template("index.html", is_product_page=False, search_results=8, data=data,
                           PRODUCT_LINK="google.ro",
                           COFFEE_BRAND=search_query,
                           COFFEE_NAME=search_query,
                           COFFEE_LOCATION="asdfsd",
                           COFFEE_ORIGIN="asdfsd",
                           LATITUDE="asdfsd",
                           ROASTED_LEVEL="asdfsd",
                           AGTRON="asdfsd",
                           PRICE="asdfsd",
                           REVIEW_DATE="asdfsd",
                           AROMA="asdfsd",
                           BODY="asdfsd",
                           FLAVOR="asdfsd",
                           AFTERTASTE="asdfsd",
                           WITH_MILK="asdfsd",
                           DESC_1="asdfsd",
                           DESC_2="asdfsd",
                           DESC_3="asdfsd",
                           COFFEE_RATING="asdfsd"
                           )

@app.route("/product")
def route_product():
    product_id = request.args.get("id", type=int)
    if product_id is None or product_id < 0:
        return redirect("/")
    print(product_id)
    # get product info info the template variables
    return render_template("index.html", is_product_page=True,
                           PRODUCT_LINK="google.ro",
                           COFFEE_BRAND=product_id,
                           COFFEE_NAME=product_id,
                           COFFEE_LOCATION="asdfsd",
                           COFFEE_ORIGIN="asdfsd",
                           LATITUDE="asdfsd",
                           ROASTED_LEVEL="asdfsd",
                           AGTRON="asdfsd",
                           PRICE="asdfsd",
                           REVIEW_DATE="asdfsd",
                           AROMA="asdfsd",
                           BODY="asdfsd",
                           FLAVOR="asdfsd",
                           AFTERTASTE="asdfsd",
                           WITH_MILK="asdfsd",
                           DESC_1="asdfsd",
                           DESC_2="asdfsd",
                           DESC_3="asdfsd",
                           COFFEE_RATING="asdfsd"
                           )



if __name__ == "__main__":
    app.run(debug=True)