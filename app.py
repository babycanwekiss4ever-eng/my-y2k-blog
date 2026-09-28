from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "秘密のチャットルーム正在启动 ♡"

if __name__ == "__main__":
    app.run(debug=True)