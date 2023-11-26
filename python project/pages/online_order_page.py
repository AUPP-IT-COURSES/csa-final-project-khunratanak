import streamlit as st

# Page title
st.title("Online Ordering")
st.subheader("Please select which company you want to choose")

# Load images
food_panda_image = "/Users/rathanak/Desktop/python project/pages/picture/foodpanda.png"  # Replace with the path to your image
wownow_image = "/Users/rathanak/Desktop/python project/pages/picture/wownow.png"  # Replace with the path to your image
grab_image = "/Users/rathanak/Desktop/python project/pages/picture/Grabfood.png"  # Replace with the path to your image

# Function to create a clickable image
def clickable_image(image_path, url):
    image = f'<a href="{url}" target="_blank"><img src="{image_path}" width="100"></a>'
    st.markdown(image, unsafe_allow_html=True)

# Create clickable image as a button

food_panda, wownow, grab = st.columns(3)
with food_panda:
     food_panda =clickable_image(food_panda_image, "https://www.foodpanda.com.kh/") 
with wownow:
     wownow = clickable_image(wownow_image, "https://www.wownow-kh.com/")
with grab:
     grabfood = clickable_image(grab_image, "https://transport.grab.com/kh/en/?gad_source=1&gclid=CjwKCAiA04arBhAkEiwAuNOsIlO6imRep7SAE3V5VGMqRLn5EGc6vWfN80MZlf6JIDSUR9UJmsI6MhoCPioQAvD_BwE")
 
