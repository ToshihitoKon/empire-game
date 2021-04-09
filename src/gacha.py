import random

class Gacha:
    gachaList = [
        {
            "id": "100",
            "name": "ジョワユーズガチャ",
            "candidates": [
                {
                    "name":"ジョワユーズ(C)",
                },
                {
                    "name":"ジョワユーズ(UC)",
                },
                {
                    "name":"ジョワユーズ(R)",
                },
                {
                    "name":"ジョワユーズ(SR)",
                },
                {
                    "name":"ジョワユーズ(SECRET)",
                },
            ]
        }
    ]

    def draw(self, gachaId):
        gacha = [ gacha for gacha in self.gachaList if gacha["id"] == gachaId ]
        if len(gacha) != 1:
            return None

        candidates = gacha[0]["candidates"]
        resultNum = random.randint(0,len(candidates)-1)
        result = candidates[resultNum]

        return result
