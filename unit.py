import streamlit as st

# Set a nice background color and font style
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-top: 20px;
    }
    .subtitle {
        font-size: 28px;
        text-align: center;
        color: #333;
    }
    .description {
        font-size: 20px;
        text-align: center;
        color: #777;
    }
    .container {
        background-color: #f1f1f1;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stSelectbox, .stNumberInput, .stButton {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="title">Unit Converter</div>', unsafe_allow_html=True)

# Subtitle and Description
st.markdown('<div class="subtitle">Convert Weight, Length, Time instantly</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Simplify your unit conversions in just a click!</div>', unsafe_allow_html=True)

# Create a container for inputs and results
with st.container():
    category = st.selectbox("Choose the category to convert", ["Length", "Weight", "Time"], key="category", index=0)
    
    # Conversion function
    def convert(category, value, unit):
        if category == "Length":
            if unit == "Kilometers to Miles":
                return value * 0.621371
            elif unit == "Miles to Kilometers":
                return value / 0.621371
        elif category == "Weight":
            if unit == "Kilograms to Pounds":
                return value * 2.20462
            elif unit == "Pounds to Kilograms":
                return value / 2.20462    
        elif category == "Time":
            if unit == "Seconds to Minutes":
                return value / 60
            elif unit == "Minutes to Seconds":
                return value * 60
            elif unit == "Minutes to Hours":
                return value / 60
            elif unit == "Hours to Minutes":
                return value * 60
            elif unit == "Hours to Days":
                return value / 24
            elif unit == "Days to Hours":
                return value * 24

    # Category-specific dropdown for conversion units
    if category == "Length":
        unit = st.selectbox("Select the conversion", ["Miles to Kilometers", "Kilometers to Miles"])
    elif category == "Weight":
        unit = st.selectbox("Select the conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
    elif category == "Time":
        unit = st.selectbox("Select the conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

    # Input field for value
    value = st.number_input("Enter the value for conversion", min_value=0.0, step=0.1)

    # Conversion button
    if st.button("Convert"):
        if value:
            result = convert(category, value, unit)
            st.success(f"The result is: {result:.2f}")
        else:
            st.error("Please enter a valid value.")
            
# Adding a custom background to the entire page
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa;
    }
    </style>
    """, unsafe_allow_html=True
)
