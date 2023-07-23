import requests
import streamlit as st

api_key = st.secrets['OPEN_WEATHER_API']


def getWeather(location):
    url = f"http://api.openweathermap.org/res/2.5/weather?q={location}&units=metric&appid={api_key}"
    response = requests.get(url)
    print(response.status_code)


getWeather("Casablanca")
# print(api_key)

# st.title('Welcome to :blue[NICY]')
# st.subheader('Your Weather App')
# loc = st.text_input(label='location', placeholder='search for location')
# if st.button('show', type='primary') and loc != '':
#     res = getWeather(loc)
#     data = {}
#     data['country'] = res['sys']['country']
#     data['city'] = res['sys']['name']
#     data['lon'] = res['coord']['lon']
#     data['lat'] = res['coord']['lat']
#     data['desc'] = res['weather'][0]['description']
#     data['icon'] = res['weather'][0]['icon']
#     data['curr temp'] = res['main']['temp']
#     data['temp min'] = res['main']['temp_min']
#     data['temp max'] = res['main']['temp_max']
#     data['pressure'] = res['main']['pressure']
#     data['humidity'] = res['main']['humidity']
#     data['wind speed'] = res['wind']['speed']
#     st.dataframe(data)
