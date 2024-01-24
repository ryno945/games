import requests
import json

def fetch_earthquake_data():
    # Define the API endpoint
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Load the data from the response
        data = json.loads(response.content)
        
        # Print the number of earthquakes that occurred
        print(f"Number of Earthquakes Today: {len(data['features'])}")
        
        # For each earthquake, print the place and magnitude
        for earthquake in data['features']:
            print(f"Place: {earthquake['properties']['place']}")
            print(f"Magnitude: {earthquake['properties']['mag']}")
    else:
        print("Failed to fetch earthquake data")

if __name__ == "__main__":
    fetch_earthquake_data()
