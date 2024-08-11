import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation for fashion
fashion_animation = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_c2gxrdxl.json")

# Title and Description
st.title("Fashion and Retail Showcase")
st.write("Welcome to the fashion and retail app! Explore the latest trends, collections, and more.")

# Display Lottie Animation
st_lottie(fashion_animation, height=300, key="fashion")

# Interactive Section for Showing Fashion Collections
st.header("Explore Our Latest Collections")
collection = st.selectbox(
    "Select a collection to view:",
    ("Summer Collection", "Winter Collection", "Spring Collection")
)

# Display images based on user selection
if collection == "Summer Collection":
    st.image("https://via.placeholder.com/400x300?text=Summer+Collection+1", caption="Summer Dress")
    st.image("https://via.placeholder.com/400x300?text=Summer+Collection+2", caption="Casual Summer Outfit")
elif collection == "Winter Collection":
    st.image("https://via.placeholder.com/400x300?text=Winter+Collection+1", caption="Winter Coat")
    st.image("https://via.placeholder.com/400x300?text=Winter+Collection+2", caption="Warm Sweater")
else:
    st.image("https://via.placeholder.com/400x300?text=Spring+Collection+1", caption="Spring Dress")
    st.image("https://via.placeholder.com/400x300?text=Spring+Collection+2", caption="Light Jacket")

# Add a section for featured products
st.header("Featured Products")
st.image("https://via.placeholder.com/400x300?text=Featured+Product", caption="Fashionable Handbag")
st.image("https://via.placeholder.com/400x300?text=Featured+Product", caption="Stylish Shoes")

# Footer
st.write("Thank you for visiting our fashion showcase! Stay tuned for more updates.")

