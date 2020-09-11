import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

Essence = client.open("CardsDesign").worksheet("Essences")
Path = client.open("CardsDesign").worksheet("Paths")
Miracle = client.open("CardsDesign").worksheet("Miracles")
data = Miracle.get_all_records()

print(data)