from flask import *
import requests,pathlib
import xml.dom.minidom
from xml.dom.minidom import parseString
import sqlite3

app = Flask(__name__)
@app.route("/")
def index():

    try:
        # print("kk"+6)
        s = parseString(requests.get("https://www.irna.ir/rss").text)
        r = s.documentElement
        it =  r.getElementsByTagName('item')
        y = []
        for i in it:
            y.append([i.getElementsByTagName("title")[0].childNodes[0].data,i.getElementsByTagName("link")[0].childNodes[0].data])
        return render_template("index.html",y=y,ty=1)
        
    except:
        return render_template("index.html",y=[],ty=0)
# @app.route("/img/2.ico")

# def icon():
#     return pathlib.Path("2.ico").read_bytes()
# @app.route("/img/header-background.jpg")
# def bg():
#     return pathlib.Path("header-background.jpg").read_bytes()
# @app.route("/particles.js")
# def particles():
#     return render_template("particles.js")
# @app.route("/app.js")
# def app_js():
#     return render_template("app.js")
@app.route("/about")
def ab():
    return render_template("i.html")

app.run(host="0.0.0.0",port="80",debug=1)
