import streamlit as st

# Title of the app
st.title("Simple Input Display App")

# Text input widget
user_input = st.text_input("Enter some text:")

# Button to display the input
if st.button("Show Input"):
    # Display the input text
    st.write("You entered:", user_input)

# Run the app using: streamlit run app.py
