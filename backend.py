import requests
API_KEY = "98dc2d43bc0c7d771951cad828a45c0d"


def get_data(place, forecast_days=None , kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    responses = requests.get(url)
    data = responses.json()
    return data

if __name__ == "__main__":
    print(get_data(place= "Tokyo"))