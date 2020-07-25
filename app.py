from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    print(request.form)
    print(request.files)
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0')