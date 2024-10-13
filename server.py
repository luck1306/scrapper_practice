from flask import Flask, request, render_template, redirect
from server_util import search_dc, search_namu

app = Flask("Scrapper")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/find")
def find():
    keyword: str = request.args.get("keyword")
    find_type: str = request.args.get("service_type")
    site_info: list = []

    if keyword == None or find_type == None: return redirect("/")

    if find_type == "namu":
        site_info = search_namu()
        site_info.insert(0, ["Title", "Url"]) # head_list
    else:
        site_info = search_dc(keyword)

    return render_template("find.html", service_type=find_type, keyword=keyword, head_list=site_info[0], value_list=site_info[1:])

app.run("localhost", "8080")