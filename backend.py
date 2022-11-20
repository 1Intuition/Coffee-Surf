from flask import Flask, request, redirect, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder="templates", static_folder="static")

DISPLAY_MAX_RESULTS = 50


data = pickle.load(open("df.p", "rb"))
# data = pd.read_csv("df2.csv")

@app.route("/")
def route_search():
    search_query = request.args.get("q", type=str)
    query_page = request.args.get("page", type=int)  # starts from 1

    # get result data with function:...
    result_data = data

    num_pages = ((len(result_data) - 1) // DISPLAY_MAX_RESULTS) + 1  # 0 if 0 data else 1, 2, etc
    if query_page is not None and (query_page <= 0 or query_page > num_pages):  # invalid page arg set to None
        query_page = None

    this_page = 1 if query_page is None else query_page

    cropped_result_data = result_data[DISPLAY_MAX_RESULTS*(this_page-1):DISPLAY_MAX_RESULTS*this_page]

    # print(cropped_result_data["roaster"][])

    if this_page == num_pages:
        next_page_link = None
    else:
        next_page_link = "/?" + (f"q={search_query}&" if search_query else "") + f"page={this_page+1}"

    return render_template("index.html",
                           is_product_page=False,
                           num_results=len(cropped_result_data),
                           data=cropped_result_data,
                           this_page=this_page,  # integer denoting the page number, starting at 1!!!
                           num_pages=num_pages,  # integer denoting the number of total pages
                           next_page_link=next_page_link   # None if there are no more pages, string of next page otherwise
                           )


@app.route("/product")
def route_product():
    product_id = request.args.get("id", type=int)
    if product_id is None or product_id < 0:
        return redirect("/")
    print(product_id)
    # get product info info the template variables

    rec_ids = data["recommendations"][product_id]

    return render_template("index.html",
                           is_product_page=True,
                           product_row=data.iloc[product_id],
                           recommendations=data.iloc[rec_ids]
                           )



if __name__ == "__main__":
    app.run(debug=True)