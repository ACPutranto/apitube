from pytube import YouTube as yt
i
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def indek():
    return render_template("index.html")

@app.route("")
