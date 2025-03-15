import streamlit as st # streamlit is a library for building web apps

# Functions to convert units from the predefined factors or formulas
def convert_units(value, unit_from, unit_to):

    convertions = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer 
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001, # 1 grams = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilograms = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" # Generate a key based on the input and output units

    # logic to convert units 
    if key in convertions:
        conversion = convertions[key]
        return value * conversion
    else: 
        return "Conversion Not Supported" # return a message if the conversion is not supported
    
st.title("Unit Converter") # Set the title of the web app

# user input: numerical value to convert
value = st.number_input("Enter the value: ", min_value=1) 


# dropdown to select the unit to convert from 
unit_from = st.selectbox("Convert from: ", ["meters", "kilometers", "grams", "kilograms"])

# dropdown to select the unit to convert to 
unit_to = st.selectbox("Convert to: ", ["meters", "kilometesr", "grams", "kilograms"])

# button that trigger the conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to) # call the conversion function
    st.write(f"Converted Value: {result}") # displaying the result