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
