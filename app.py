import streamlit as st
import numpy as np
from PIL import Image
from deepface import DeepFace
import google.generativeai as genai
import json
from pyyoutube import Api

# ------------------- CONFIG -------------------
st.set_page_config(page_title="Mood-Based Music Player 🎵", layout="centered")
st.title("🎭 MoodTune: Music for Your Mood")
st.markdown("Upload a photo or take a selfie, and we'll detect your emotion and recommend matching music!")

# ------------------- API KEYS -------------------
YOUTUBE_API_KEY = "AIzaSyB9q58JJo9VjsObZo0KeNSaeKdfP3RKa88"
GEMINI_API_KEY = "AIzaSyDAFhChMDsqnAwfh9frrLJJwYA2yMYPl-4"

# ------------------- INITIALIZATIONS -------------------
@st.cache_resource
def get_gemini_model():
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel("gemini-1.5-pro")

model = get_gemini_model()
youtube_api = Api(api_key=YOUTUBE_API_KEY)

# ------------------- EMOTION DETECTION -------------------
def detect_emotion(image):
    try:
        img_array = np.array(image.convert("RGB"))
        result = DeepFace.analyze(img_array, actions=['emotion'], enforce_detection=False)
        if result and isinstance(result, list):
            return result[0]['dominant_emotion'], result[0]['emotion'][result[0]['dominant_emotion']]
        return "neutral", 0.0
    except Exception as e:
        st.error(f"Emotion detection error: {str(e)}")
        return "neutral", 0.0

# ------------------- MUSIC RECOMMENDATION -------------------
def get_music_recommendations(emotion):
    prompt = f"""
    Recommend 3 popular Indian songs that match the emotion '{emotion}'.
    Format as JSON with: title, artist, year, and reason.
    Example: {{"recommendations": [{{"title": "Happy", "artist": "Arijit Singh", "year": 2015, "reason": "Uplifting romantic ballad"}}]}}
    """
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        if '```json' in response_text:
            response_text = response_text.split('```json')[1].split('```')[0]
        return json.loads(response_text)['recommendations']
    except Exception as e:
        st.error(f"Recommendation error: {str(e)}")
        return []

# ------------------- YOUTUBE SEARCH -------------------
def get_youtube_link(query):
    try:
        # Modify the query to include "Indian" for relevant music
        search_query = f"{query} Indian music"
        
        search_response = youtube_api.search(
            q=search_query,
            search_type="video",
            count=1,
            parts="snippet",
            order="relevance"
        )
        
        if search_response.items:
            video_id = search_response.items[0].id.videoId
            return f"https://www.youtube.com/embed/{video_id}"
        return None
        
    except Exception as e:
        st.error(f"YouTube search error: {str(e)}")
        return None

# ------------------- MAIN UI -------------------
st.subheader("📸 Upload or Take a Photo")
img_file = st.camera_input("Take a selfie") or st.file_uploader("Or upload an image", type=["jpg", "jpeg", "png"])

if img_file:
    image = Image.open(img_file)
    st.image(image, caption="Your Image", use_container_width=True)

    with st.spinner("Analyzing your mood..."):
        emotion, confidence = detect_emotion(image)
        
    if confidence > 0.4:
        st.success(f"Detected Emotion: **{emotion.capitalize()}** (Confidence: {confidence:2%})")
        
        with st.spinner(f"Finding perfect music for {emotion}..."):
            recommendations = get_music_recommendations(emotion)
            
            if recommendations:
                st.subheader("🎵 Recommended Songs")
                for song in recommendations:
                    with st.expander(f"{song['title']} by {song['artist']}"):
                        st.write(f"**Released:** {song.get('year', 'N/A')}")
                        st.write(f"**Why this song:** {song['reason']}")
                        
                        video_url = get_youtube_link(f"{song['title']} {song['artist']}")
                        if video_url:
                            st.video(video_url)
                            st.markdown(f"[Watch on YouTube](https://www.youtube.com/watch?v={video_url.split('/')[-1]})")
                        else:
                            st.warning("Video not found")
            else:
                st.warning("No recommendations found. Please try again.")
    else:
        st.warning("Couldn't detect a clear emotion. Please try with a different photo.")   