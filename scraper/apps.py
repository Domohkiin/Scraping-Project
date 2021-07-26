import os
import os.path
import pickle
from google.auth.transport.requests import Request as GoogleRequest
#print("What the heck 34")
from google_auth_oauthlib.flow import InstalledAppFlow
#print("What the heck 32")
from googleapiclient.discovery import build


# Read from sheets
#   Remember https://console.developers.google.com/?authuser=0&project=checkauthorizeds-1597348139916
def read_apps_sheet():
    apps = {}

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


    # Not sure what the spreadsheet ID should be yet, just need to make sure it's not hardcoded
    APPS_SPREADSHEET_ID = ''
    # Need to make range_name outputs as a hash table
    # Not sure what range_name needs to be set as here, I'm sure the syntax needs to be similar
    # to the one used in vulnerability check but I haven't quite gotten it
    RANGE_NAME = 'Software!A1:P'

    # Probably need a for loop (or something similar) here

    # Not sure what parts of this I need, I would think all or at least most of it
    # However its not recognizing a credentials.json file
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    # Not sure if I need to have this block of code below about pickles and tokens and such
    # Commented it out so hopefully the script will stop erroring
    # This merely caused authorization to fail so I uncommented it

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(GoogleRequest())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # This service stuff looks like it needs to stay
    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)

    # Call the Sheets API
    sheet = service.spreadsheets()  # pylint: disable=maybe-no-member
    result = sheet.values().get(spreadsheetId=APPS_SPREADSHEET_ID,
                                range=RANGE_NAME).execute()

    # Printing result to see what I'm working with
    print(f"Result is {result}")
    # Need to make sure that RANGE_NAME is exported as a hash table
    values = result.get('values', [])
    # Printing values to see what it is turned into
    print(f"Values = {values}")

    if not values:
        print('No data found.')
    else:
        header = True
        index = {}
        for row in values:
            if header:
                # Record the index location for all column names
                for i in range(1, len(row)):
                    if row[i]:
                        index[row[i]] = i
                header = False
            else:
                app = None
                thisrow = {}
                for column_name in index.keys():
                    # Using the names on the index line,
                    # populate thisrow dict with the actual values
                    if len(row) > index[column_name] and row[index[column_name]]:
                        thisrow[column_name] = row[index[column_name]]

                if 'Product' in thisrow:
                    app = thisrow['Product'].lower()
                    apps[app] = thisrow



    return (apps)