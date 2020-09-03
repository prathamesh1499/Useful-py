import gspread # pip install gspread

'''SETUP
- google developer console: https://console.developers.google.com
- new project -> activate drive and sheets api
- credentials -> service account -> name + role=editor
  ->create key and download json
- share client_email fom json in your sheets
'''

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key("xxxx") # or by sheet name: gc.open("TestList")
worksheet = sh.sheet1

### retrieve data ###
res = worksheet.get_all_records() # list of dictionaries
res = worksheet.get_all_values() # list of lists

values_list = worksheet.row_values(1) # to get row vals
values_list = worksheet.col_values(1) # to get col vals


print(worksheet.row_count, worksheet.col_count)

# INSERT UPDATE

user = ["Cristiano", "35", "Lisbon"]
#worksheet.insert_row(user, 3)  #same with column
#worksheet.append_row(user)
#worksheet.update_cell(1,2, value)

# DELETE
#worksheet.delete_rows(1)
#worksheet.delete_columns(1)

'''
USE THE FOLLOWING IF YOU HAVE THE CREDENTIALS ALREADY LOADED
AND IN JSON FORMAT
import json
from google.oauth2.service_account import (
    Credentials as ServiceAccountCredentials,
)
DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]
with open('credentials.json', 'r') as f:
    credentials = json.load(f)
creds = ServiceAccountCredentials.from_service_account_info(credentials, scopes=DEFAULT_SCOPES)
gc = gspread.Client(auth=creds)
'''
