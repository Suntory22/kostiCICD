import os
import signal
from flask import Flask, request, render_template
from kostiP.kosti import *

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))


@app.route("/")
def indexkos():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def contact():
    images = os.listdir(os.path.join(app.static_folder, "images"))
    dices = ('')
    if "1" in request.form:
        dices = solo1(3)
    elif "2" in request.form:
        dices = solo2(3)
    elif "3" in request.form:
        dices = solo3(3)
    elif "4" in request.form: 
        dices = solo4(3)
    return render_template('index.html', dices=dices, images=images)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
