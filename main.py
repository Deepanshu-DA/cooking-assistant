import google.generativeai as genai
import base64
import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import io

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use the latest Gemini models
VISION_MODEL = "gemini-1.5-flash"  # Supports both text and vision
TEXT_MODEL = "gemini-1.5-flash"    # Use the same model for text-based tasks

def analyze_ingredient(image_bytes):
    """Analyze the image and extract ingredients using Gemini AI."""
    model = genai.GenerativeModel(VISION_MODEL)

    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))

    # Send image to Gemini for processing
    response = model.generate_content(
        [
            "Identify the food ingredients in this image. List only the ingredients, comma-separated.",
            image
        ]
    )

    return response.text.strip()

def suggest_recipe(ingredients):
    """Generate a recipe suggestion based on ingredients using Gemini AI."""
    model = genai.GenerativeModel(TEXT_MODEL)

    response = model.generate_content(
        f"Suggest a creative recipe using these ingredients: {ingredients}. Keep it short and clear."
    )

    return response.text.strip()

# Streamlit UI
st.title("AI-Powered Cooking Assistant 🍽️")

uploaded_files = st.file_uploader("Upload ingredient images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_files:
    ingredients_list = []

    for uploaded_file in uploaded_files:
        image_bytes = uploaded_file.read()
        ingredients = analyze_ingredient(image_bytes)
        ingredients_list.append(ingredients)
        st.write(f"Identified Ingredients in {uploaded_file.name}: **{ingredients}**")

    if ingredients_list:
        all_ingredients = ", ".join(ingredients_list)
        st.write(f"**All identified ingredients:** {all_ingredients}")
        recipe = suggest_recipe(all_ingredients)
        st.subheader("Suggested Recipe 🍳")
        st.write(recipe)
