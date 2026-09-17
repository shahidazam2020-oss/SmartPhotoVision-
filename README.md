# 📸 SmartPhotoVision

<p align="center">
  <strong>AI-Powered Photo Management & Face Recognition Desktop Application</strong>
</p>

<p align="center">
  <em>Organize • Detect • Recognize • Cluster • Explore</em>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![AI](https://img.shields.io/badge/AI-Face%20Analysis-8A2BE2?style=for-the-badge)

</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-technology-stack">Technology</a> •
  <a href="#-screenshots">Screenshots</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a>
</p>

---

## 🚀 Overview

**SmartPhotoVision** is an intelligent desktop photo management application designed to make large photo collections easier to organize, analyze, and explore.

The application combines **Artificial Intelligence, Computer Vision, Face Detection, Face Recognition, Face Clustering, and SQLite database management** into a single desktop interface.

Instead of manually searching through hundreds or thousands of images, SmartPhotoVision analyzes photographs and helps organize them according to the people detected in the images.

### 🎯 What SmartPhotoVision Does

- 📂 Scans photo folders recursively
- 👤 Detects human faces using **YuNet**
- 🧠 Generates face embeddings using **SFace**
- 🧩 Groups similar faces into personas
- 🗃️ Stores photo and face information in **SQLite**
- 🖼️ Supports multiple common image formats
- 📍 Handles photo metadata such as date and GPS information
- ⚡ Processes photo collections in the background
- 🖥️ Provides a modern desktop interface using **PySide6**
- 🔄 Supports face reclustering for improved organization

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 📂 **Recursive Scanning** | Automatically searches folders and subfolders for images |
| 👤 **Face Detection** | Detects faces using OpenCV YuNet |
| 🧠 **Face Recognition** | Creates face embeddings using OpenCV SFace |
| 🧩 **Face Clustering** | Groups visually similar faces into personas |
| 🗃️ **SQLite Database** | Stores photos, faces, persons, and tags |
| 🖼️ **Multiple Formats** | Supports JPG, JPEG, PNG, WEBP, BMP, TIFF and more |
| 📍 **Photo Metadata** | Reads available EXIF date and GPS information |
| ⚡ **Background Processing** | Performs analysis without freezing the interface |
| 🎨 **Modern GUI** | Built with PySide6 and a customized application theme |
| 🛡️ **Error Handling** | Logging and exception handling help diagnose application issues |

---

# 🧠 AI & Computer Vision Pipeline

SmartPhotoVision follows a multi-stage analysis pipeline:

```text
                    📁 Photo Folder
                          │
                          ▼
                🔍 Recursive Scanning
                          │
                          ▼
                  🖼️ Image Loading
                          │
                          ▼
                 👤 YuNet Detection
                          │
                          ▼
                 🧠 SFace Embedding
                          │
                          ▼
                 🔎 Face Comparison
                          │
                          ▼
                  🧩 Face Clustering
                          │
                          ▼
                    👥 Personas
                          │
                          ▼
                 🗃️ SQLite Storage
                          │
                          ▼
                   🖥️ Desktop GUI

```

---

# 🔬 AI Models

The project uses two OpenCV ONNX models:

Face Detection

## models/
└── face_detection_yunet_2023mar.onnx

Used to locate faces inside photographs.

## Face Recognition

models/
└── face_recognition_sface_2021dec.onnx

Used to generate face embeddings and compare detected faces.

---

# 🏗️ Application Architecture

```text
SmartPhotoVision/
│
├── 📄 main.py
│
├── 🧠 analyzer.py
│
├── 🗃️ database.py
│
├── 🛠️ paths.py
│
├── 🤖 models/
│   ├── face_detection_yunet_2023mar.onnx
│   └── face_recognition_sface_2021dec.onnx
│
├── 🖥️ gui/
│   ├── window.py
│   └── theme.py
│
└── 📘 README.md

---
```

# 🔹 Core Components

Component	Responsibility
main.py	Application startup and configuration
analyzer.py	Photo scanning, face detection, recognition and clustering
database.py	SQLite database and data persistence
paths.py	Application and resource path management
gui/	Desktop user interface and visual styling
models/	AI models used for face analysis


# 🛠️ Technology Stack
## Programming
🐍 Python
🖥️ PySide6
👁️ OpenCV
🔢 NumPy
🗃️ SQLite
Artificial Intelligence
🤖 YuNet Face Detector
🧠 SFace Face Recognition
🧩 Face Embeddings
🔎 Similarity Matching
📊 Face Clustering

## Development Tools
Visual Studio Code
Git
GitHub
Python Virtual Environment

---
# 📊 Project Dashboard
<p align="center">
🧠 AI	👤 Face Analysis	🗃️ Storage	🖥️ Interface
YuNet + SFace	Detection + Recognition	SQLite	PySide6
</p>

---
# 📌 Application Information
## Property	Value
🏷️ Project	SmartPhotoVision
📦 Application Type	Desktop Application
🐍 Language	Python
🖥️ GUI Framework	PySide6
👁️ Computer Vision	OpenCV
🗃️ Database	SQLite
🤖 AI Models	YuNet + SFace
🔢 Version	1.0.4
📸 Screenshots

Real application screenshots are provided below as proof of the working output.

---

# 🖥️ Main Application
<p align="center"> <img src="https://github.com/shahidazam2020-oss/SmartPhotoVision-/blob/master/screenshots/Persona%203.PNG" width="900"> </p>

Main SmartPhotoVision desktop interface.

## 🔍 Photo Analysis
<p align="center"> <img src="https://github.com/shahidazam2020-oss/SmartPhotoVision-/blob/master/screenshots/persona%201.PNG" width="900"> </p>

Photo scanning and AI-powered face analysis.

## 👤 Face Detection
<p align="center"> <img src="https://github.com/shahidazam2020-oss/SmartPhotoVision-/blob/master/screenshots/Persona%202.PNG" width="900"> </p>

Detected faces within the analyzed photographs.

## 🧩 Face Clustering / Personas
<p align="center"> <img src="https://github.com/shahidazam2020-oss/SmartPhotoVision-/blob/master/screenshots/persona%205.PNG" width="900"> </p>

Detected faces organized into personas based on similarity.

🗃️ Photo Organization
<p align="center"> <img src="https://github.com/shahidazam2020-oss/SmartPhotoVision-/blob/master/screenshots/persona%207.PNG" width="900"> </p>

Organized photo collection inside the application.

---

# 📷 Add Your Screenshots

To display your actual screenshots on GitHub, create:

screenshots/
│
├── main-window.png
├── photo-analysis.png
├── face-detection.png
├── personas.png
└── photo-library.png

Then replace the example images above with your actual screenshots.

# ⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/SmartPhotoVision.git
cd SmartPhotoVision
2️⃣ Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Application

Start SmartPhotoVision with:

python main.py

The application will initialize the database and launch the desktop interface.

---
# 📖 Usage
Step 1 — Launch

Run:

python main.py
Step 2 — Select Photo Folder

Choose the directory containing your photographs.

Step 3 — Analyze

Start the photo analysis process.

SmartPhotoVision will:

📂 Scan Images
      ↓
👤 Detect Faces
      ↓
🧠 Generate Embeddings
      ↓
🔎 Compare Faces
      ↓
🧩 Cluster Similar Faces
      ↓
🗃️ Save Results
Step 4 — Explore

Use the application interface to explore the analyzed photographs and detected personas.

---

# 🗃️ Database Structure

SmartPhotoVision uses SQLite to maintain persistent application data.

Main Tables
photos
│
├── Photo information
├── Filename
├── Dimensions
├── Modification time
├── Taken-at metadata
└── GPS information

persons
│
├── Person ID
└── Person Name

faces
│
├── Photo reference
├── Person reference
├── Bounding box
├── Detection score
├── Face embedding
└── Pin status

tags
│
└── Photo categorization

photo_tags
│
└── Photo ↔ Tag relationships


# 🔐 Data & Privacy

SmartPhotoVision is designed as a local desktop application.

Photo analysis and application data are handled locally through the application's processing and SQLite storage components.

No cloud photo-upload workflow is required for the core analysis pipeline.

Always review the project's actual configuration and dependencies before using it with sensitive photo collections.

⚡ Performance & Processing

The application is designed to process photo collections efficiently by:

🔄 Processing images in the background
📐 Resizing very large images before analysis
🧠 Limiting stored embeddings per persona
🧩 Using similarity-based clustering
💾 Persisting analysis results in SQLite
🛑 Supporting analysis cancellation
📝 Providing logging and error handling
📁 Supported Image Formats

SmartPhotoVision supports:

.jpg
.jpeg
.png
.webp
.bmp
.tif
.tiff
🧪 Project Highlights
🤖 Artificial Intelligence

Face detection and recognition are integrated directly into the application workflow.

👁️ Computer Vision

OpenCV provides the underlying computer-vision capabilities for detecting and analyzing faces.

🗃️ Database Engineering

SQLite provides structured persistence for photographs, detected faces, personas, and tags.

🖥️ Desktop Application Development

PySide6 provides the graphical interface and application experience.

🧩 Intelligent Organization

Face similarity and clustering allow photographs to be organized around detected people.

🗺️ Future Improvements

Potential future development areas include:

🌐 Multi-language interface
📱 Companion mobile application
🔎 Advanced semantic photo search
🏷️ Automatic image tagging
🧠 Improved face clustering
👥 Better person management
📊 Collection analytics dashboard
⚡ GPU acceleration
📤 Export and backup functionality
🎯 Advanced search and filtering
🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Contribution Workflow
Fork
  ↓
Create Branch
  ↓
Make Changes
  ↓
Test
  ↓
Commit
  ↓
Pull Request

Please ensure that proposed changes are tested before submitting a pull request.

📜 License

Add your preferred open-source license here.

For example:

MIT License
⭐ Support the Project

If you find SmartPhotoVision useful or interesting:

⭐ Star the repository

🍴 Fork the project

🐛 Report issues

💡 Suggest improvements

🤝 Contribute

👨‍💻 Author

Shahid Azam

<p align="center">

⭐ <strong>SmartPhotoVision — Intelligent Photo Management with AI</strong> ⭐

</p> ```
📁 Recommended GitHub structure

For the README above, I recommend organizing the repository like this:

SmartPhotoVision/
│
├── 📄 main.py
├── 📄 analyzer.py
├── 📄 database.py
├── 📄 paths.py
├── 📄 requirements.txt
│
├── 🤖 models/
│   ├── face_detection_yunet_2023mar.onnx
│   └── face_recognition_sface_2021dec.onnx
│
├── 🖥️ gui/
│   ├── window.py
│   └── theme.py
│
├── 📸 screenshots/
│   ├── main-window.png
│   ├── photo-analysis.png
│   ├── face-detection.png
│   ├── personas.png
│   └── photo-library.png
│
└── 📘 README.md
