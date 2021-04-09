from sessions import Sessions
from gacha import Gacha

ses = Sessions()
gch = Gacha()

def ping():
    return {
        "response": "pong"
    }, 200


def new_user():
    uid = ses.new()
    return {
        "response": {
            "id": uid
        }
    }, 200

def get_user(uid):
    user_session = ses.get(uid)
    if user_session == None:
        return {
            "response": "error: user not found"
        }, 400
    return {
        "response": user_session["data"]
    }, 200

def draw_gacha(gachaId):
    result = gch.draw(gachaId)
    if result == None:
        return {
            "response": "error: gacha not found"
        }, 400

    return {
        "response": result
    }, 200
