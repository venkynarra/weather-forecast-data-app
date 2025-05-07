import streamlit as st
import plotly.express as px
from backend import get_data
# adding title , text input, slider, select box, sub header
st.title("The weather forecast for Next days")
place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help ="Select the number of forecasted days ")
options = st.selectbox("select data to view",
                       ("Temperature", "sky"))
st.subheader(f"{options} for the next{days} days in {place}")

if place:
    # getting the sky and temperature data
    filtered_data = get_data(place, days)



    if options == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature(c)"})
        st.plotly_chart(figure)
    if options == "sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)

        st.image(image_paths, width=115)