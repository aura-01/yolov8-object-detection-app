import streamlit as st
import cv2
import numpy as np
import tempfile
import datetime
from PIL import Image

from detector import detect_objects
from db import save_detection
from utils.image_utils import image_bytes_to_numpy

st.set_page_config(page_title="Object Detection App", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #dfe9f3, #ffffff, #e1f5fe);
            font-family: 'Poppins', sans-serif;
            min-height: 100vh;
        }

        /* Sidebar container gradient & padding */
        section[data-testid="stSidebar"] .block-container {
            padding: 2rem 1rem;
            background: linear-gradient(180deg, #4facfe, #00f2fe);
            border-radius: 20px;
        }

        /* Sidebar text & radio buttons */
        section[data-testid="stSidebar"] .block-container * {
            font-size: 22px !important;
            color: #fff !important;
            font-weight: 600 !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="radio"] label {
            font-size: 22px !important;
            color: #ffe082 !important;
            font-weight: 700 !important;
        }

        /* Stylish Main Heading with gradient text */
        .main-title {
            font-size: 60px;
            font-weight: 900;
            text-align: center;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #4facfe, #00f2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .subtitle {
            font-size: 26px;
            text-align: center;
            color: #555;
            margin-bottom: 30px;
        }

        .section-header {
            font-size: 32px;
            color: #333;
            margin-top: 30px;
            margin-bottom: 10px;
        }

        /* Button Styling */
        .stButton>button {
            font-size: 20px;
            background-color: #4B8BBE;
            color: white;
            border-radius: 12px;
            padding: 12px 24px;
            margin-top: 15px;
            font-weight: bold;
        }

        /* Upload drag/drop area font */
        .css-1v0mbdj.edgvbvh3, .css-1cpxqw2.edgvbvh3 {
            font-size: 20px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## Select Input Type")
input_type = st.sidebar.radio("", ["Image", "Video", "Webcam"], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("<large> Built By Amrutha Challagulla using Streamlit</large>", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Object Detection Application</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload an image, video or use your webcam to detect objects using YOLO or any custom model.</div>", unsafe_allow_html=True)
st.markdown("---")

def process_and_display(frame, save=False):
    annotated_img, detected_classes = detect_objects(frame)
    st.image(annotated_img, channels="BGR", caption=" Detected Output", use_container_width=True)
    
    if save:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"detection_{timestamp}.jpg"
        save_detection(annotated_img, detected_classes, filename)
        st.success("✔ Detection result saved to MongoDB!")

if input_type == "Image":
    st.markdown("<div class='section-header'>📷 Upload an Image</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = image_bytes_to_numpy(uploaded_file.read())
        image = cv2.imdecode(file_bytes, 1)
        
        col1, col2 = st.columns([3, 1])
        with col1:
            process_and_display(image)
        with col2:
            if st.button("💾 Save Detection"):
                process_and_display(image, save=True)

# --- Video Upload ---
elif input_type == "Video":
    st.markdown("<div class='section-header'>🎞️ Upload a Video</div>", unsafe_allow_html=True)
    uploaded_video = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        st.info("📽️ Processing video...")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            annotated_frame, _ = detect_objects(frame)
            stframe.image(annotated_frame, channels="BGR", use_container_width=True)
        cap.release()
        st.success("✔ Finished processing video")

# --- Webcam Input ---
elif input_type == "Webcam":
    st.markdown("<div class='section-header'>📹 Live Webcam Detection</div>", unsafe_allow_html=True)
    st.info(" Webcam stream will open below...")

    from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
    import av

    class YOLOTransformer(VideoTransformerBase):
        def transform(self, frame):
            img = frame.to_ndarray(format="bgr24")
            annotated_frame, _ = detect_objects(img)
            return annotated_frame

    webrtc_streamer(key="live", video_transformer_factory=YOLOTransformer)
