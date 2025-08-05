````markdown
# 🧠 YOLOv8 Object Detection Web App

This is a basic object detection application built using **YOLOv8**, **Streamlit**, and **MongoDB**. The app allows you to perform real-time object detection on images, videos, and webcam streams, with an option to save the results to a MongoDB database.

---

## 🚀 Features

- 📂 **Image Upload Detection**  
  Upload an image and get real-time object detection results.

- 🎥 **Video File Detection**  
  Upload a video file and see frame-wise object detection.

- 📸 **Live Webcam Detection**  
  Use your device's webcam for real-time detection in the browser.

- 💾 **Save to MongoDB**  
  After performing detection, you can save the results to a connected MongoDB database with a single click.

---

## 🛠️ Tech Stack

| Component      | Technology Used         |
|----------------|--------------------------|
| Object Detection | [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics) |
| Web UI         | [Streamlit](https://streamlit.io/)           |
| Database       | [MongoDB](https://www.mongodb.com/)          |
| Backend        | Python, OpenCV, PIL                          |

---
### MongoDB Document Schema

**Collection:** `detections`

Each document contains:
- `filename`: `string` – name of the saved image
- `timestamp`: `datetime` – time when detection was made
- `detections`: `array[string]` – list of detected classes
- `image`: `binary` – image data in JPEG format
---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/aura-01/yolov8-object-detection-app.git
cd yolov8-object-detection-app
````

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up MongoDB**

* You can use MongoDB Atlas (cloud) or run it locally.
* Make sure to update your MongoDB connection string in the code (typically in `db.py` or `main.py`).

5. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 🗃️ Project Structure

```bash
📁 yolov8-object-detection-app/
│
├── app.py                # Main Streamlit app
├── detector.py           # YOLOv8 detection logic
├── db.py                 # MongoDB interaction functions
├── image_utils.py        # Helper functions for image processing
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── ...                   # Other supporting files
```

---

## 📸 Screen
<img width="1919" height="964" alt="Screenshot 2025-08-05 221843" src="https://github.com/user-attachments/assets/eeaffff5-5b78-429c-aa14-54bbb36b17ba" />

<img width="1919" height="871" alt="Screenshot 2025-08-05 221910" src="https://github.com/user-attachments/assets/5896ba72-c7bc-4834-a07f-8af5f6b1355c" />

<img width="1919" height="953" alt="Screenshot 2025-08-05 222249" src="https://github.com/user-attachments/assets/20348c2c-47ad-4d54-b126-1fc35ce1541e" />

<img width="1918" height="965" alt="Screenshot 2025-08-05 214749" src="https://github.com/user-attachments/assets/882452e0-65f9-4fc1-9bb6-a825c0e40894" />

<img width="1769" height="1005" alt="Screenshot 2025-08-05 214525" src="https://github.com/user-attachments/assets/f4635250-f740-4164-a2e2-6929f2dcc2e5" />



---

## 🧠 Future Improvements

* Add support for custom YOLOv8 models
* Improve UI/UX with styled components
* Add pagination/search in MongoDB viewer
* Deploy on cloud (e.g., Streamlit Cloud, AWS, Heroku)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---



## 📬 Contact

* **Author**: aura-01
* **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/teja-amrutha-sai-challagulla-60b421270/)
* **GitHub**: [github.com/aura-01](https://github.com/aura-01)

---

```

---





