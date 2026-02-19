import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(page_title="AutoSage App")
st.header("🚗 AutoSage App Using Gemini Flash")

# File uploader for vehicle image
uploaded_image = st.file_uploader(
    "Upload a vehicle image",
    type=["jpg", "jpeg", "png"]
)

# Mock Gemini response function
# (Used due to Gemini API access restrictions)
def get_gemini_response(prompt):
    return """
Brand: Honda
Model: Activa 6G
Mileage: 50 km/l

Key Features:
- Silent start
- Digital instrument cluster
- External fuel fill

Approximate Price: ₹75,000 – ₹85,000
"""

# Prompt for Gemini model (conceptual)
input_prompt = """
You are an automobile expert.
Analyze the vehicle image and provide:
- Brand
- Model
- Key features
- Mileage
- Approximate price in INR
"""

# Display image and output
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Vehicle Image", use_column_width=True)

    if st.button("Submit"):
        with st.spinner("Analyzing vehicle..."):
            result = get_gemini_response(input_prompt)
            st.subheader("Vehicle Details")
            st.write(result)
