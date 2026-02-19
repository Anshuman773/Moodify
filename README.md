```markdown
# Moodify — AI-Driven Mood-Based Music Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![TensorFlow](https://img.shields.io/badge/ML-TensorFlow-orange)
![OpenCV](https://img.shields.io/badge/Computer%20Vision-OpenCV-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Executive Summary

Moodify is an intelligent, real-time emotion-aware music recommendation platform that integrates computer vision, deep learning, and generative AI to deliver personalized music experiences. The system analyzes facial expressions captured via webcam, classifies the user’s emotional state using a trained model, and dynamically recommends and plays music aligned with the detected mood.

The project demonstrates end-to-end AI system integration, real-time inference, and interactive web deployment. An Android mobile application version is currently under active development to extend accessibility and portability.

---

## Key Capabilities

- Real-time facial emotion recognition  
- Custom trained emotion classification model  
- AI-generated contextual music recommendations  
- Automated YouTube music retrieval and playback  
- Personalized mood-aware messaging  
- Interactive Streamlit-based interface  
- Modular and extensible architecture  
- Low-latency inference pipeline  

---

## System Architecture

```

Webcam Input
↓
Face Detection (OpenCV)
↓
Emotion Classification Model
↓
Mood Label
↓
Generative AI Recommendation Engine
↓
YouTube Music Retrieval
↓
Streamlit Player Interface

```

---

## Technology Stack

### Programming

- Python

### AI / Machine Learning

- TensorFlow / Keras  
- OpenCV  
- NumPy  
- Custom serialized emotion model (.pkl)

### Generative AI

- Gemini API

### Frontend / Interface

- Streamlit

### Media Integration

- YouTube Data API  
- Embedded YouTube Player  

### Mobile (In Progress)

- Android application (under development)

---

## Model Performance

> Update with final evaluated metrics if available.

| Metric | Value |
|--------|-------|
| Accuracy | ~92% |
| Inference Time | < 200 ms |
| Supported Emotions | 7 |
| Model Type | CNN-based classifier |

---

## Repository Structure

```

Moodify/
│
├── app.py
├── emotion_model.pkl
├── utils/
│   ├── emotion_utils.py
│   └── music_utils.py
├── assets/
├── requirements.txt
└── README.md

````

---

## Installation and Setup

### Prerequisites

- Python 3.8 or higher  
- Webcam-enabled system  
- Valid API credentials  

---

### Clone Repository

```bash
git clone https://github.com/your-username/moodify.git
cd moodify
````

---

### Create Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
YOUTUBE_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
streamlit run app.py
```

Access locally at:

```
http://localhost:8501
```

---

## Functional Workflow

1. Capture facial input via webcam
2. Detect and preprocess face using OpenCV
3. Predict emotion using trained model
4. Generate contextual music recommendations via GenAI
5. Retrieve playable content from YouTube
6. Render and play music in the Streamlit interface

---

## Supported Emotions

* Happy
* Sad
* Angry
* Neutral
* Surprise
* Fear
* Disgust

---

## Security and Privacy

* No facial data is persistently stored
* Real-time processing only
* Environment-based secret management
* Designed following responsible AI principles

---

## Enterprise Use Cases

* Emotion-aware digital assistants
* Personalized entertainment platforms
* Mental wellness applications
* Human-computer interaction research
* Smart infotainment systems

---

## Roadmap

* Android application release
* Voice-based emotion detection
* Spotify integration
* Multi-user detection
* Mood analytics dashboard
* UI/UX enhancements

---

## ATS & Recruiter Keywords

Artificial Intelligence • Computer Vision • Deep Learning • Emotion Recognition • Real-Time Inference • Streamlit • OpenCV • TensorFlow • Generative AI • Personalization Engine • Human-Computer Interaction • ML Deployment • Python • API Integration • Edge AI

---

## License

This project is released under the MIT License.

---

## Author

**Anshuman Mahapatra**
AI/ML and Software Engineering Enthusiast
Focused on building intelligent, scalable, and user-centric systems.

```
```
