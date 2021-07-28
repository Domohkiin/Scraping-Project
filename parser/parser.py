import feedparser

def parser(apps_spreadsheet_id, range_name, google_sheets_url):

    d = feedparser.parse(google_sheets_url)

    print(f"d is: {d}")
