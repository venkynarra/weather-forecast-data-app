import streamlit as st
import plotly.express as px
st.title("The weather forecast for Next days")
place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help ="Select the number of forecasted days ")
options = st.selectbox("select data to view",
                       ("Temperature", "sky"))
st.subheader(f"{options} for the next{days} days in {place}")

def get_data(days):
        dates = ["2022-25-10", "2022-26-10","2022-27-10"]
        temperatures = [10,11,15]
        temperatures = [days * i for i in temperatures]
        return dates, temperatures

d,t = get_data(days)

figure = px.line(x=d, y=t, labels={"x":"Date", "y":"Temperature(c)"})
st.plotly_chart(figure)