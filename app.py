""" This is REST API, that upload images from dirs base and previews """
import signal
from flask import Flask, send_from_directory
from flask_restful import Resource, Api
from make_dir import make_dir

APP = Flask(__name__)

class GracefulKiller:
    """ This class for graceful shutdown """
    def __init__(self):
        self.kill_now = True
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        """ Gives to kill_flag the False """
        self.kill_now = False

class ImagesBase(Resource):
    """ Upload images into .../base/img address """
    def get(self, filename):
        """ Get request into .../base/img address """
        return send_from_directory("base", filename)


class ImagesPreviews(Resource):
    """ Upload images into .../previews/img_small address """
    def get(self, filename):
        """ Get request into .../previews/img_small address """
        return send_from_directory("previews", filename)


if __name__ == '__main__':
    KILLER = GracefulKiller()
    while KILLER.kill_now:
        API = Api(APP)
        API.add_resource(ImagesBase, "/base/<filename>")
        API.add_resource(ImagesPreviews, "/previews/<filename>")
        make_dir()
        APP.run(port=8080, debug=True)
print("End of the program")
