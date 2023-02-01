import json
import requests
class blooket:
    def getToken(code): 
        return json.loads(requests.post('https://play.blooket.com/api/playersessions/hosted', json={'gameCode': code,}).content)

    def getQuestionSetId(token):
        return json.loads(requests.post('https://play.blooket.com/api/playersessions/landings', json={'t': token,}).content)

    def getInfo(infotoken):
        return json.loads(requests.get("https://play.blooket.com/api/games?gameId="+infotoken).content)

    def make(code):
        return blooket.getInfo(blooket.getQuestionSetId(blooket.getToken(code)['t'])['questionSetId'])

gameinfo = blooket.make('4845481')
print(gameinfo)
