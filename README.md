# AI-Powered Cooking Assistant 🍽️

## Overview
This AI-powered cooking assistant helps users identify ingredients from images and suggests creative recipes based on them. The application utilizes **Google Gemini AI** (`gemini-1.5-flash`) for both image analysis and text-based recipe generation.

## Features
- 🖼️ **Ingredient Identification**: Upload an image, and AI extracts a list of ingredients.
- 🍽️ **Recipe Suggestions**: Based on detected ingredients, AI generates a creative recipe.
- 🌐 **Web App Interface**: Built using **Streamlit** for easy interaction.

## Technologies Used
- **Python** 🐍
- **Google Gemini AI (`gemini-1.5-flash`)** 🤖
- **Streamlit** 🌐 (for UI)
- **PIL (Pillow)** 🖼️ (for image processing)
- **dotenv** 🔐 (for API key management)

## Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/cooking-assistant.git
cd cooking-assistant
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key
Get your **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file and add:
```ini
GEMINI_API_KEY=your_google_api_key_here
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

## Usage
1️⃣ **Upload images** of ingredients. 📸
2️⃣ AI extracts ingredient names. 📝
3️⃣ AI suggests a recipe using the detected ingredients. 🍳

## Example
**Input:** 🖼️ Upload an image of tomatoes, onions, and garlic.

**Output:** 📝 Suggested Recipe - "Tomato Garlic Pasta with Caramelized Onions."

## License
This project is licensed under the **MIT License**.
