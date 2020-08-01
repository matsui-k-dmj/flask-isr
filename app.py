from flask import Flask, render_template, request, redirect, send_file
import model
import io
import numpy as np
import cv2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    print(request.form)
    print(request.files)

    img = model.super_resolution(
        bytes2image(request.files["image"].stream.read()),
        request.form['algo'])

    retval, buf = cv2.imencode('.png', img)

    return send_file(io.BytesIO(buf),
                     mimetype='image/png',
                     as_attachment=True,
                     attachment_filename='tmp.png')


def bytes2image(buf: bytes) -> np.ndarray:
    return cv2.imdecode(np.frombuffer(buf, dtype=np.uint8), 1)


if __name__ == "__main__":
    app.run(host='0.0.0.0')