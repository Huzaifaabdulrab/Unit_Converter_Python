import streamlit as Huzaifa

def convert_unit (value , unit_form , unit_to):
    
    conversion ={
        "meter_kilometer":    0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter":    1000, # 1 kilometer = 1000 meter
        "gram_kilogram":     0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram":     1000 # 1 kilogram = 1000 gram
    }

    key = f"{unit_form}_{unit_to}" # key for the conversion

    if key in conversion :
        conversion = conversion[key]
        return value * conversion 
    else : 
        return "Conversion not available"
    
Huzaifa.title("Unit Converter ")

value = Huzaifa.number_input("Enter the value ")

unit_form = Huzaifa.selectbox("Convert from :" , ["meter", "kilometer","gram","kilogram"] , key="unit_form")
unit_to = Huzaifa.selectbox("Convert from :" , ["meter", "kilometer","gram","kilogram"] , key="unit_to")

if Huzaifa.button("Convert") :
    result = convert_unit(value , unit_form, unit_to)
    Huzaifa.write(f"Converted value : {result}")