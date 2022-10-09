from pytube import YouTube as yt
import random
from flask import Flask, render_template, request, Response
from flask_restful import Resource, Api
from flask_cors import CORS

app= Flask(__name__)
api = Api(app)
CORS(app)

#@app.route("/")
class resour(Resource):
    def get(self):
        return render_template("index.html")


#@app.route("/ytvideo-sound", methods=["GET", "POST"])
class ytvids(Resource):
    def get(self):
        try:
            url = request.args.get("url")
            yu = yt(url)
            res=[]
            name = yu.title.replace(" ", "").replace(",","").replace("'","")
            [res.append(i) for i in yu.streams.get_highest_resolution()]
            if len(res) == 2:
                result = {
                    "status":True,
                    "title":name,
                    "msg":"berhasil",
                    "video-sound": {
                                    "480p":res[0].url+"&title="+name
                                    }
                            }
            else:
                result = {
                    "status":True,
                    "title":name,
                    "msg":"berhasil",
                    "video-sound":{
                        "114p":res[0].url+"&title="+name,
                        "360p":res[1].url+"&title="+name
                    }
                }
                        #"video-no-sound": {
                            #"240p":yu.streams.get_by_itag(133).url+"&title="+name,
                            #"360p":yu.streams.get_by_itag(134).url+"&title="+name,
                            #"480p":yu.streams.get_by_itag(135).url+"&title="+name,
                            #"720p":yu.streams.get_by_itag(136).url+"&title="+name,
                            #"1080p":yu.streams.get_by_itag(137).url+"&title="+name
                            #},
                        #"audio_only": {
                            #"70kbps":yu.streams.get_by_itag(140).url+"&title="+name,
                            #"160kbs":yu.streams.get_by_itag(251).url+"&title="+name
                            #}
                    #}
        
        except Exception as e:
            result = {
                "status":False,
                "msg":"link-undefined",
                "error":str(e),
                "inLine":e.__traceback__.tb_lineno
                }
        return result

class ytvidns(Resource):
    def get(self):
        try:
            url = request.args.get("url")
            yu = yt(url)
            name = yu.title.replace(" ","").replace(",","").replace("''","")
            result ={
                "status":True,
                "title":name,
                "msg":"link-undefined",
                "video-no-sound":{
                    "240p":yu.streams.get_by_itag(133).url+"&title="+name,
                    "360p":yu.streams.get_by_itag(134).url+"&title="+name,
                    "480p":yu.streams.get_by_itag(135).url+"&title="+name,
                    #"720p":yu.streams.get_by_itag(136).url+"&title="+name,
                    #"1080p":yu.streams.get_by_itag(137).url+"&title="+name
                }
            }
        except Exception as e:
            result ={
                "status":False,
                "msg":"link-undefined",
                "error":str(e),
                "inLine":e.__traceback__.tb_lineno
            }
        return result
"""@app.route("/ytvideo-nosound", methods=["GET", "POST"])
def youtubevidnos():"""
    
url = ["https://m.youtube.com/watch?v=5DoCO50PX9w",
        "https://m.youtube.com/watch?v=H-Z2elwvBS8",
        "https://m.youtube.com/watch?v=rjgLhYqzIFo",
        "https://m.youtube.com/watch?v=pPHaV7MiAXM",
        "https://m.youtube.com/watch?v=Yv41FS_MwkI"]
u = random.choice(url)

api.add_resource(resour, "/", methods=["GET"])
api.add_resource(ytvids, "/ytvideo-sound", methods=["GET"])
api.add_resource(ytvidns, "/ytvideo-no-sound", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True, port=3000)
