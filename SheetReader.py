from __future__ import print_function
import pickle
import os.path
import re
import configparser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class SheetReader:

    # Initialize SheetReader object
    def __init__(self):
        self.SHEET_CONFIG = dict()
        self.RANGES_CONFIG = dict()
        self.readConfig()
        self.getSpreadsheetID()
        self.setCredentials()

    # Reads config file. User must set 'url' parameter under SHEET section
    def readConfig(self):
        config = configparser.RawConfigParser()
        config.read('./config.properties')
        self.SHEET_CONFIG = dict(config.items('SHEET'))
        self.RANGES_CONFIG = dict(config.items('RANGES'))

    # Parses sheet ID from url
    def getSpreadsheetID(self):
        m = re.search('(?<=/d/)[^/]*', self.SHEET_CONFIG.get('url'))
        self.sheetID = m.group(0)

    # Either reads users credentials from token.pickle or creates new credentials by
    # asking user to log in through Google Sign-In
    def setCredentials(self):
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.creds = creds

    # Reads data from sheet, returns 2d list with dimensions n by 2
    # Left hand side of each entry will be foreign word
    # Right hand side of each entry will be native word
    def readSheet(self):
        service = build('sheets', 'v4', credentials=self.creds)

        sheet = service.spreadsheets()
        values = []
        for range in self.RANGES_CONFIG:
            result = sheet.values().get(spreadsheetId=self.sheetID,
                                    range=self.RANGES_CONFIG.get(range)).execute()
            values.extend(result.get('values', []))
        if not values:
            print('No data found.')
        else:
            print('German, English:')
            for row in values:
                # Print columns A and B, which correspond to indices 0 and 1.
                print(row)
                #print('%s, %s' % (row[0], row[1]))
        return values

if __name__ == '__main__':
    exit()