# 🌱 AgriAssist360

AI-Powered Fruit & Vegetable Ripeness Detection using Deep Learning

AgriAssist360 is a machine learning-based web application designed to analyze fruits and vegetables and classify them based on ripeness and quality. The system uses Convolutional Neural Networks (CNN) to identify crops and predict whether they are **Fresh**, **Rotten**, or **Unripe**.

Built using **Python, TensorFlow, Keras, Flask, OpenCV, HTML, CSS, and JavaScript**, the project provides a simple and interactive web interface where users can upload crop images and receive instant AI-based predictions.

---

## 🚀 Features

- 🍎 Multi-crop classification
- 🥭 Ripeness detection using CNN
- 📷 Real-time image upload and prediction
- 🤖 AI-powered quality analysis
- 🌐 Flask-based web application
- 🧠 Deep Learning model with TensorFlow & Keras
- 🖼️ Image preprocessing using OpenCV
- 📊 Training accuracy/loss visualization
- 💡 Farming recommendations based on predictions

---

## 🧠 Supported Crops

| Crop | Supported Classes |
|------|-------------------|
| Apple | Fresh / Rotten |
| Banana | Fresh / Rotten |
| Mango | Fresh / Unripe |
| Tomato | Fresh / Rotten |

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Flask (Python)

## Machine Learning
- TensorFlow
- Keras
- CNN (Convolutional Neural Network)
- OpenCV
- NumPy

---

# 📂 Project Structure

```bash
Agri_Assist_360/
│
├── data/
├── dataset/
│   ├── Apple_Fresh/
│   ├── Apple_Rotten/
│   ├── Banana_Fresh/
│   ├── Banana_Rotten/
│   ├── Mango_Fresh/
│   ├── Mango_Unripe/
│   └── Tomato_Fresh/
│
├── model/
│   ├── fruit_model.h5
│   ├── tomato_model.h5
│   ├── class_indices.json
│   └── training_plot.png
│
├── static/
│   ├── css/
│   ├── images/
│   └── uploads/
│
├── templates/
│   ├── home.html
│   ├── category.html
│   └── item_detail.html
│
├── uploads/
├── app.py
├── train_model.py
├── create_dataset_structure.py
├── download_images.py
└── README.md
```

# ▶️ Sample Output
<img src="https://github.com/user-attachments/assets/49e8d0ef-147e-4614-b617-1dcf79dc8286" width="300"/>

<img src="https://github.com/user-attachments/assets/920f12a2-4058-4687-ac32-b3e90e0a72f9" width="300"/>

<img src="https://github.com/user-attachments/assets/0c3cbf0c-1b02-4333-b3e8-d89a20228fc4" width="300"/>

<img src="https://github.com/user-attachments/assets/08c54ee6-5d50-4c77-a5a1-8a6e210a77f1" width="300"/>

<img src="https://github.com/user-attachments/assets/193aba13-5b9f-45ae-8cd5-d5454f94582d" width="300"/>

<img src="https://github.com/user-attachments/assets/9ad19e85-3fd0-4366-82de-7380c1f6f24d" width="300"/>


