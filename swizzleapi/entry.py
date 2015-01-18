import os, sys, hashlib
# hack because relative import in python is hard to work around
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "swizzlescrape"))

import uuid
from flask import Flask, jsonify, request
import tswizzler as T

app = Flask(__name__, static_folder='../tempstore/', static_url_path='/static')

# entry point into this very simple swizzleapi
@app.route("/")
def splash():
    return "Welcome to the T-Swizzle API. Well shit."

# call api/swizzle?txt=incredible%20things
# gets us an actual video file...
@app.route("/swizzle", methods=['GET'])
def get_swizzle():
    inputString = request.args['txt']
    fileName = hashlib.md5(inputString.encode()).hexdigest() + '.mp4'
    newSwizzleURL = '../tempstore/' + fileName
    if os.path.isfile(newSwizzleURL) is False:
        T.swizzle(inputString, output=newSwizzleURL, hasText=True)
    return app.send_static_file(fileName)

# start it all
if __name__ == "__main__":
    app.run(debug=True)