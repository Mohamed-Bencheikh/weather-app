import requests
import streamlit as st
from PIL import Image
import time

api_key = st.secrets['OPEN_WEATHER_API']


def getWeather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
    response = requests.get(url).json()
    return response


st.title('Welcome to :blue[NICY]')
st.subheader('Your Weather App')
loc = st.text_input(label='location', placeholder='search for location')
if st.button('show', type='primary') and loc != '':
    with st.spinner('getting '+loc+' weather ...'):
        time.sleep(3)
    res = getWeather(loc)
    data = {}
    data['country'] = res['sys']['country']
    data['city'] = res['name']
    data['lon'] = res['coord']['lon']
    data['lat'] = res['coord']['lat']
    data['desc'] = res['weather'][0]['description']
    data['curr temp'] = res['main']['temp']
    data['temp min'] = res['main']['temp_min']
    data['temp max'] = res['main']['temp_max']
    data['pressure'] = res['main']['pressure']
    data['humidity'] = res['main']['humidity']
    data['wind speed'] = res['wind']['speed']
    c1, c2 = st.columns(2)
    with c1:
        st.dataframe(data, width=300)
    with c2:
        icon = res['weather'][0]['icon']
        img = Image.open('./icons/'+icon+'.png')
        st.image(image=img)
