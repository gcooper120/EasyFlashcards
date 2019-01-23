import SheetReader
import json
import requests
import configparser

def main():
    cg = CardGenerator()
    cg.getDeckConfig()
    cg.createNewDeck()
    cg.addNote("front", "back")

class CardGenerator:

    def __init__(self):
        self.DECK_CONFIG = dict()
        self.ANKI_CONFIG = dict()
        self.getConfig()

    def getConfig(self):
        config = configparser.RawConfigParser()
        config.read('./config.properties')
        self.DECK_CONFIG = dict(config.items('DECK'))
        self.ANKI_CONFIG = dict(config.items('ANKI'))

    def getDeckConfig(self):
        val = {"action": "getDeckConfig","version": 6,"params": {"deck": "Default"}}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(self.ANKI_CONFIG.get('location'), json=val, headers=headers)

    def createNewDeck(self):
        val = {"action": "createDeck","version": 6,"params": {"deck": "Vocab"}}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(self.ANKI_CONFIG.get('location'), json=val, headers=headers)

    def addNote(self, front, back):
        val = {"action": "addNote","version": 6,"params": {"note": {"deckName": "Vocab","modelName": "Basic","fields": {"Front": front,"Back": back},"options": {"allowDuplicate": False},"tags": ["German"]}}}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(self.ANKI_CONFIG.get('location'), json=val, headers=headers)
        print(r.json())

if __name__ == '__main__':
    main()