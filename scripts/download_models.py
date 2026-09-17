"""Download the ONNX models from the official OpenCV Zoo into models/."""

import os
import urllib.request

BASE_URL = "https://github.com/opencv/opencv_zoo/raw/main/models"
MODELS = {
    "face_detection_yunet_2023mar.onnx": f"{BASE_URL}/face_detection_yunet/face_detection_yunet_2023mar.onnx",
    "face_recognition_sface_2021dec.onnx": f"{BASE_URL}/face_recognition_sface/face_recognition_sface_2021dec.onnx",
}

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "models")


def main():
    os.makedirs(MODELS_DIR, exist_ok=True)
    for name, url in MODELS.items():
        dest = os.path.join(MODELS_DIR, name)
        if os.path.isfile(dest) and os.path.getsize(dest) > 0:
            print(f"{name}: already present")
            continue
        print(f"{name}: downloading…")
        urllib.request.urlretrieve(url, dest)
        print(f"{name}: {os.path.getsize(dest)} bytes")


if __name__ == "__main__":
    main()
