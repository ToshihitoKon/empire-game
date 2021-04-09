import uuid

class Sessions:
    sessionList = []

    def new(self):
        uid = str(uuid.uuid4())
        newSession = {
            "key":uid,
            "data":{}
        }
        self.sessionList.append(newSession)

        return uid

    def get(self, key):
        session = [session for session in  self.sessionList if session["key"] == key ]

        if len(session) != 1:
            return None
        return session[0]
