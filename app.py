from flask import Flask, render_template, request, redirect, send_file
import model
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    print(request.form)
    print(request.files)
    buf = model.super_resolution(
        bytearray(request.files["image"].stream.read()))

    return send_file(io.BytesIO(buf),
                     mimetype='image/png',
                     as_attachment=True,
                     attachment_filename='tmp.png')


if __name__ == "__main__":
    app.run(host='0.0.0.0')