import streamlit as st

#hello
# set pages configuration
st.set_page_config(
    page_title="FOODEE.com"
)
# Website title 
st.title("FOODEE")

# First question
st.subheader("What kind of food do you want to eat?")
st.write("Please choose one food")

#Food button
selected_cuisine = st.radio("Select Cuisine", ["Western food", "Chinese food", "Korean food"])

# Second question
selected_rating = st.radio("Please select rating level", ["1 star", "2 stars", "3 stars"])
# Third question

selected_difficulty = st.radio("Please select difficulty level", ["Easy", "Medium", "Hard"])

# Recommendation here

st.subheader("Here are the foods:")

ReFood_col1, ReFood_col2, ReFood_col3, ReFood_col4 = st.columns(4)

with ReFood_col1:
    st.button("Food 1")

with ReFood_col2:
    st.button("Food 2")

with ReFood_col3:
    st.button("Food 3")

with ReFood_col4:
    st.button("Food 4")
    
# Fifth question and activities

st.subheader("What do you wish to do?")

Recipe_button, Order_button = st.columns(2)

with Recipe_button:
       if Recipe_button.button("Recipe"):
    # Redirect to Recipe page
         st.markdown("<a href='https://your-recipe-page-url'>Go to Recipe Page</a>", unsafe_allow_html=True)

with Order_button:
       if Order_button.button("Order online"):
    # Redirect to Recipe page
         st.markdown("<a href='https://your-order-page-url'>Go to Recipe Page</a>", unsafe_allow_html=True)
