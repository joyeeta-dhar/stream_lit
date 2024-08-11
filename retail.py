import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation (replace with a relevant fashion animation URL)
lottie_fashion = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_x62chJ.json")

# App title and description
st.title("Fashion & Retail Showcase")
st.write("Welcome to our fashion and retail app! Explore the latest trends and styles.")

# Display Lottie animation
st_lottie(lottie_fashion, height=300, key="fashion")

# Sample fashion catalog with images
st.header("Our Latest Collection")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://example.com/image1.jpg", caption="Fashion Item 1", use_column_width=True)

with col2:
    st.image("https://example.com/image2.jpg", caption="Fashion Item 2", use_column_width=True)

with col3:
    st.image("https://example.com/image3.jpg", caption="Fashion Item 3", use_column_width=True)

# Additional sections can be added for different categories, new arrivals, etc.
st.header("New Arrivals")
st.image("https://example.com/new_arrival.jpg", caption="Check out the latest styles!", use_column_width=True)

# Footer with contact information or social media links
st.write("---")
st.write("Follow us on social media for the latest updates and exclusive offers!")

# Add a contact form or other interactive elements if needed
