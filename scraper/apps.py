import os
import os.path
import pickle
import importlib
import platform
import chromedriver_binary
from google.auth.transport.requests import Request as GoogleRequest
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Authentication function; This isn't working, I think this is because the project isn't hosted on Google
#def implicit():
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    #storage_client = storage.Client()

    # Make an authenticated API request
    #buckets = list(storage_client.list_buckets())
    #print(buckets)

# Explicit function; Points directly to the json location for authentication
def explicit():
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'service_account.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

GOOGLE_APPLICATION_CREDENTIALS = 'C:\\Users\\dominic_simplerose\\Downloads\\scraping-project-321220-ba12436d461c.json\\'


# Read from sheets
# Remember https://console.developers.google.com/?authuser=0&project=checkauthorizeds-1597348139916
# Passing apps_spreadsheet_id, range_name, and google_sheets_url
def read_apps_sheet(apps_spreadsheet_id, range_name, google_sheets_url):
    apps = {}

    # If modifying these scopes, delete the file token.pickle.
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    apps_spreadsheet_id = []

    print(f"Google Sheets URL is:  {google_sheets_url}")
    print(f"range_name is {range_name}")

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(GoogleRequest())
        elif creds and creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        else:
            # Print errors if the credentials.json file doesn't exist or isn't valid
            print("Error: No credentials.json file detected.")
            print("Please follow Google's documentation to create one: https://developers.google.com/workspace/guides/create-credentials")

    # This service stuff looks like it needs to stay
    service = build('sheets', 'v4', credentials=creds, cache_discovery=False)

    # Call the Sheets API
    sheet = service.spreadsheets()  # pylint: disable=maybe-no-member
    result = sheet.values().get(spreadsheetId=apps_spreadsheet_id,
                                range=range_name).execute()

    # Printing result to see what I'm working with
    print(f"Result is {result}")
    # Need to make sure that range name is exported in a hash table
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
                    else:
                        # Print thisrow for testing
                        print(f"thisrow is: {thisrow}")
            #parser(apps_spreadsheet_id, range_name, google_sheets_url)

    return (apps)
