import requests
import json

class TsunamiDetector:
    def __init__(self, station_id):
        self.station_id = station_id
        self.base_url = "https://api.sealevelsapi.com/v1/stations/"

    def fetch_sea_level_data(self):
        response = requests.get(f"{self.base_url}{self.station_id}")
        data = json.loads(response.content)
        return data

    def detect_tsunami(self, threshold):
        data = self.fetch_sea_level_data()
        sea_level = data['latest_sea_level']
        if sea_level > threshold:
            print("Tsunami detected!")
        else:
            print("No tsunami detected.")

if __name__ == "__main__":
    detector = TsunamiDetector("your_station_id")
    detector.detect_tsunami(threshold=100)
