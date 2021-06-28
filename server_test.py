from flask import Flask
from map_to_tile import MyServer
from flask import request
import logging
import cv2

app = Flask('app')
app.add_url_rule('/', view_func=MyServer.test_rout, methods=["GET"])
app.add_url_rule('/load_img', view_func=MyServer.load_img, methods=["GET"])
app.add_url_rule('/get_tile', view_func=MyServer.get_tile, methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)
