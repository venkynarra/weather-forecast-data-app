import streamlit as st
import plotly.express as px
from backend import get_data
st.title("The weather forecast for Next days")
place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help ="Select the number of forecasted days ")
options = st.selectbox("select data to view",
                       ("Temperature", "sky"))
st.subheader(f"{options} for the next{days} days in {place}")

d, t = get_data(place, days,options)



figure = px.line(x=d, y=t, labels={"x":"Date", "y":"Temperature(c)"})
st.plotly_chart(figure)