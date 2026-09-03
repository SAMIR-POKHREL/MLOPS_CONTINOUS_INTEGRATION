import streamlit as st


# streamlit UI
st.title('Power calculator')

st.write("enter a number to calculate its square cube and fifth power")

# get the number from user 
n=st.number_input('enter an integer:',value=1,step=1)


# calculate the square cube and fith power
square=n**2
cube=n**3
fifth_power=n**5

# display the results
st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is {cube}")
st.write(f"The fifth_power of {n} is {fifth_power}")