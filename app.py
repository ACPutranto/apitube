from pytube import YouTube as yt
from pytube import Search
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def indek():
    return render_template("index.html")

def ss(url):
    yu = Search(url)
    [i.title for i in yu]
