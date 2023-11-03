import langchain_helper as lch
import streamlit as st

st.title('Pet Name Generator')

animal_type = st.sidebar.selectbox("What is your pet type?", ('', 'Cat', 'Dog', 'Hamster', 'Macaw', 'Cow'))\

pet_colour = st.sidebar.selectbox(f"What is your {animal_type} Colour?", ('White', 'Black', 'Blue', 'Yellow'))

generate = st.sidebar.button('Generate')

if generate:
    if animal_type!= '':
        response = lch.generate_pet_name(animal_type, pet_colour)
        st.text(f"Here are some names you can use: \n{response['pet_name']}")
