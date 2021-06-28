from flask import Flask
from test import MyServer
from flask import request
import logging
import cv2

app = Flask('app')
app.add_url_rule('/load_image', view_func=MyServer.load_img, methods=["GET"])

if __name__ == "__main__":
    my_server = MyServer(__name__)
    my_server.run(host="0.0.0.0", port=8080)
