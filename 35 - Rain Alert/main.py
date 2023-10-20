import requests
from twilio.rest import Client

account_sid = 'YOUR_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR_API_KEY"

parameters = {
    "lat": "39.901920",
    "lon": "-8.274960",
    "appid": api_key
}


response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

going_to_rain = False

for i in range(0, 5):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        going_to_rain = True

if going_to_rain:
    message = client.messages.create(
        from_='FROM_PHONE_NUMBER',
        body='It\'s going to rain! Bring an umbrella! ☂️',
        to='YOUR_PHONE_NUMBER'
    )
    print(message.status)