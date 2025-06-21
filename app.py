import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
pickup_date=st.date_input("Date", datetime.date(2012, 1, 1))
pickup_time=st.time_input("time", step=datetime.timedelta(minutes=1))
pickup_longitude=st.number_input("Pickup Longitude")
pickup_latitude=st.number_input("Pickup Latitude")
dropoff_longitude=st.number_input("Dropoff Longitude")
dropoff_latitude=st.number_input("Dropoff Latitude")
passenger_count=st.number_input("Passenger Count", step=1)

params_in = {
    "pickup_datetime": f"{pickup_date} {pickup_time}",  # 2014-07-06 19:18:00
    "pickup_longitude": pickup_longitude,    # -73.950655
    "pickup_latitude": pickup_latitude,     # 40.783282
    "dropoff_longitude": pickup_latitude,   # -73.984365
    "dropoff_latitude": dropoff_latitude,    # 40.769802
    "passenger_count": int(passenger_count)
}

url = "https://taxifare-203759208586.europe-west1.run.app/predict"

if st.button("Fare prediction"):
    response = requests.get(url, params=params_in)
    if response.status_code == 200:
        prediction = response.json().get("fare")
        st.success(f"Predicted fare: {prediction}")
    else:
        st.error(f"API error: {response.status_code}")
