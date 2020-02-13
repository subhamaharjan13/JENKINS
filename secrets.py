import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery

# Connecting to Google sheets

scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file','https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)

# sheet = gc.open_by_key('1k0nu7umn1yqmnFOkXfJCX2jEqTZu3XT3a1fxpc9XZE4') # personal drive
sheet = gc.open_by_key('1jbhuF3gyLs7NLrRZRLprzm52Aa68FiYZ3cC3BuKHldU').worksheet('jenkins') # datopian drive

# Jenkins API
token = '112d509f354e3090a07044b72bb96bdf9e'