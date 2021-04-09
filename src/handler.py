#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_cors import CORS
import model

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app)

@app.route("/ping")
def ping():
    ret, status = model.ping()
    return jsonify(ret), status

@app.route("/user/new")
def user_get():
    ret, status = model.new_user()
    return jsonify(ret), status

@app.route("/user/get")
def sessions_get():
    uid = request.args.get("id", "")
    ret, status = model.get_user(uid)
    return jsonify(ret), status

@app.route("/gacha/draw")
def gacha_draw():
    gachaId = request.args.get("id", "")
    ret, status = model.draw_gacha(gachaId)
    return jsonify(ret), status






if __name__ == "__main__":
    app.run(debug=True, port=5010)
