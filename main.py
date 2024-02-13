import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place=st.text_input("Place:")
days=st.slider("Forecast Days",min_value=1,max_value=5,
               help="select the number of forecast days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates=["2024-02-13","2024-02-12","2024-02-11"]
    temperature=[10,11,15]
    temperature=[days * i for i in temperature]
    return dates,temperature


d, t = get_data(days)

figure=px.line(x=d,y=t,labels={"x":"Date","y":"Temperature (c)"})
st.plotly_chart(figure)