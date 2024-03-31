import streamlit as st

def multiplication(a,b):
   return(a*b)

st.title("Little Calculator")
a = st.number_input("Input first number")
b = st.number_input("Input second number")

answer = multiplication(a,b)
st.write(answer)



