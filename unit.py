import streamlit as st;
st.title("Unit Converter")
st.markdown('## Convert Weight ,Lenght , Time instantly')
st.write("### Simplify your unit conversions in just a click!")
category=st.selectbox("Choose the category to convert",["Length","Weight","Time"])
def convert(category, value , unit):
    if category == "Length":
        if unit == "Kilometters to  Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometters":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462    
    elif category == "Time":
        if unit== "Seconds to minutes":
            return value / 60
        elif unit == "Mnutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24  
if category == "Length":
    unit=st.selectbox("Select the conversation",["Miles to Kilometters","Kilometters to  Miles"])
elif category == "Weight":
    unit=st.selectbox("Select the conversatin",["Kilograms to Pounds","Pounds to Kilograms"])
elif category == "Time":
    unit=st.selectbox("Select the conversation",["Seconds to minutes","Miutes to seconds","Minutes to hours","Hours to minutes","Hours to days","Days to hours"])    
value = st.number_input("Enter  the value of the conversation")
if st.button("convert"):
    result=convert(category,value , unit)
    st.success(f"the result is {result:.2f}")