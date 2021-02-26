import streamlit as st
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
date_choice = st.date_input(
    "When",
    datetime.date(2019, 7, 6))
st.write("Your taxi comes on:", date_choice)
# time

time_choice = st.time_input("At what time?:", datetime.datetime(1,1,1))

st.write("Come down at", time_choice)

pickup_datetime = datetime.datetime.combine(date_choice, time_choice)
pick_long = st.number_input("Pick longitude")
pick_lat = st.number_input("Pick a latitude")
dropoff_long = st.number_input("Pick a dropff longitude")
dropoff_lat = st.number_input("Pick a dropff latitude")
passenger_count = st.number_input("How many passengers?")

url = 'http://taxifare.lewagon.ai/predict_fare/'
params = {'key': 0,
          'pickup_datetime': time_choice,
          'pick_long': pick_long,
          'pick_lat': pick_lat,
          'dropoff_long': dropoff_long,
          'dropoff_lat': dropoff_lat,
          'passenger_count': passenger_count
          }

if url == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
