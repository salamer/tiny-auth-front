from flask import Flask, render_template

app = Flask(__name__, static_folder="fe/dist/assets",
            template_folder="fe/dist", static_url_path="/assets")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
