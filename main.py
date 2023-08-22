import requests
import os
from twilio.rest import Client


AMS_LAT = 52.370216
AMS_LONG = 4.895168
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
MY_LAT = -23.5203479
MY_LONG = -47.2575256
API_KEY = os.environ["API_KEY"]
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


def weather():
    params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "exclude": "current,minutely,daily",
        "appid": API_KEY,
    }
    response = requests.get(url=OWM_ENDPOINT, params=params)
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["hourly"][:12]
    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]['id']
        if int(condition_code) < 700:
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body="Bring an umbrella.",
                from_='+18666760288',
                to='+18315661108'
            )
            print(message.status)
            break



# write down what you need to do
####
# responsiveness
# kondo messages
# take 9 and 10th and 14th 6 days
# call ADHD Psychologist
# ADHD strategies for being interrupted
#

weather()