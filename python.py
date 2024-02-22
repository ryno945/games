# Import the necessary packages
import config as cfg
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Define the scopes for the Google APIs
SCOPES = ['[13](https://www.googleapis.com/auth/calendar)' , '[14](https://www.googleapis.com/auth/spreadsheets)']

# Define the spreadsheet ID and range for the recipes
SPREADSHEET_ID = <Your Google sheet ID>
RANGE = 'recipes!A:G'

# Define the calendar ID and time range for the meal plan
CALENDAR_ID = <Your Google calendar ID>
TIME_MIN = datetime.now().isoformat() + 'Z' # Start from today
TIME_MAX = (datetime.now() + timedelta(days=14)).isoformat() + 'Z' # End after two weeks

# Define the API key for the Spoonacular API
API_KEY = <Your Spoonacular API key>

# Create a service account credential for the Google APIs
creds = service_account.Credentials.from_service_account_file(cfg.SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Google Calendar and Sheets services
calendar_service = build('calendar', 'v3', credentials=creds)
sheets_service = build('sheets', 'v4', credentials=creds)

# Get the recipes from the Google sheet
sheet = sheets_service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
values = result.get('values', [])
recipes = pd.DataFrame(values[1:], columns=values[0])

# Get the work events from the Google calendar
calendar = calendar_service.calendars().get(calendarId=CALENDAR_ID).execute()
events_result = calendar_service.events().list(calendarId=CALENDAR_ID, timeMin=TIME_MIN, timeMax=TIME_MAX, singleEvents=True, orderBy='startTime').execute()
events = events_result.get('items', [])

# Create a list of dates for the meal plan
dates = pd.date_range(start=datetime.now().date(), end=datetime.now().date() + timedelta(days=13))

# Create a list of available time slots for cooking based on the work events
time_slots = []
for date in dates:
  start_time = datetime.combine(date, datetime.min.time())
  end_time = datetime.combine(date, datetime.max.time())
  busy_times = []
  for event in events:
    if date == datetime.fromisoformat(event['start']['date']).date():
      busy_times.append((datetime.fromisoformat(event['start']['dateTime']), datetime.fromisoformat(event['end']['dateTime'])))
  free_times = []
  for busy_time in busy_times:
    free_times.append((start_time, busy_time[0]))
    start_time = busy_time[1]
  free_times.append((start_time, end_time))
  time_slots.append(free_times)

# Create a list of preferred recipes based on the available time slots and the recipe duration
preferred_recipes = []
for time_slot in time_slots:
  max_duration = min([slot[1] - slot[0] for slot in time_slot])
  preferred_recipes.append(recipes[recipes['Duration'] <= max_duration])

# Create a list of selected recipes by randomly choosing one from the preferred recipes for each date
selected_recipes = []
for preferred_recipe in preferred_recipes:
  selected_recipes.append(preferred_recipe.sample())

# Create a list of events for the meal plan based on the selected recipes and the dates
events = []
for i in range(len(dates)):
  event = {
    'summary': 'Meal: ' + selected_recipes[i]['Name'].iloc[0],
    'description': 'Ingredients: ' + selected_recipes[i]['Ingredients'].iloc[0] + '\nInstructions: ' + selected_recipes[i]['Instructions'].iloc[0],
    'start': {
      'date': dates[i].strftime('%Y-%m-%d'),
    },
    'end': {
      'date': dates[i].strftime('%Y-%m-%d'),
    },
  }
  events.append(event)

# Insert the events to the Google calendar
for event in events:
  calendar_service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

# Create a list of ingredients for the shopping list based on the selected recipes
ingredients = []
for selected_recipe in selected_recipes:
  ingredients += selected_recipe['Ingredients'].iloc[0].split(', ')

# Remove the duplicates and sort the ingredients
ingredients = sorted(list(set(ingredients)))

# Print the meal plan and the shopping list
print('Meal Plan:')
for i in range(len(dates)):
  print(dates[i].strftime('%A, %B %d:'), selected_recipes[i]['Name'].iloc[0])

print('\nShopping List:')
for ingredient in ingredients:
  print('-', ingredient)
