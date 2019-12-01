""" This module makes dir with images, that have been downloaded from user`s URLs"""
from os import getcwd, mkdir, remove
from os.path import isdir
import requests
from PIL import Image
def make_dir():
    """ This func will be called in app """
    urls = []
    while True:
        input_data = input()
        if input_data == " ":
            break
        else:
            urls.append(input_data)
    path = str(getcwd())
    if not isdir(path + "\\base"):
        mkdir("base")
    if not isdir(path + "\\previews"):
        mkdir("previews")
        try:
            i = 0
            # download original images into dir base and resize them in dir previews
            for url in urls:
                with open("base/img" + str(i) + ".jpg", "wb") as file:
                    file.write(requests.get(url).content)
                    original_image = Image.open('base/img' + str(i) + '.jpg')
                    resized_image = original_image.resize((100, 100))
                    resized_image.save('previews/img' + str(i) + '_small.jpg')
                i += 1
        except requests.exceptions.MissingSchema as err_request:
            remove("base/img0.jpg")
            print("error happend : ", err_request)
