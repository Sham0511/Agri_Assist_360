
# 🌾 AgriAssist360  
AI-Powered Fruits & Vegetables Ripeness Detection with Multi-Crop Classification

AgriAssist360 is an AI-powered crop analysis system that detects fruit and vegetable ripeness using deep learning. The system identifies crop type (Apple, Banana, Mango, Tomato) and classifies them as **Fresh, Rotten, or Unripe** using a CNN model. It also provides real-time farming recommendations via a Flask-based web interface.

---

## 🚀 Features
- 🔍 Ripeness Detection (Fresh / Rotten / Unripe)
- 🍎 Multi-Crop Support (Apple, Banana, Mango, Tomato)
- 🧠 CNN model trained using TensorFlow & Keras
- 🖼️ Real-time image upload & prediction
- 🧹 Image preprocessing with OpenCV
- 🌐 Clean web UI (HTML, CSS, JS)
- 📊 Training visualization & dataset support

---

## 📂 Project Structure

AgriAssist360/
│
├── data/ # Original dataset folders
│ ├── dataset/
│ │ ├── Apple_Fresh/
│ │ ├── Apple_Rotten/
│ │ ├── Banana_Fresh/
│ │ ├── Mango_Unripe/
│ │ └── etc...
│
├── model/
│ ├── class_indices.json
│ ├── fruit_model.h5
│ ├── tomato_model.h5
│ ├── training_plot.png
│
├── static/
│ ├── css/
│ ├── images/
│ │ ├── apple.jpg
│ │ ├── banana.jpg
│ │ ├── mango.jpg
│ │ ├── tomato.jpg
│ │ └── uploads/
│
├── templates/
│ ├── home.html
│ ├── category.html
│ ├── item_detail.html
│
├── uploads/ # User uploaded images
│
├── app.py # Flask backend
├── train_model.py # CNN model training script
├── create_dataset_structure.py # Dataset utility
├── download_images.py # Image downloader
└── README.md

---

## 🛠️ Installation & Setup


## 1️⃣ Clone the Repository
git clone https://github.com/sham0511/Agri_Assist_360.git
## 2️⃣ Install Dependencies
pip install -r requirements.txt

## 3️⃣ Run the Flask Application
python app.py

## 4️⃣ Open in Browser
http://127.0.0.1:5000

## 🧠 Model Details

CNN architecture trained on multi-class fruit/vegetable dataset

Supports Apple, Banana, Mango, Tomato with 3 ripeness labels

Uses:

Convolution layers

MaxPooling

Dense classifier

Saved models: fruit_model.h5, tomato_model.h5

📸 Screenshot Samples
![Screenshot_2025-10-28-22-41-34-78_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/65c53be3-ab12-4c04-92a7-6d9b4cac99ea)
![Screenshot_2025-10-29-08-32-54-70_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/50819ad3-0073-41cb-95c6-778480de34eb)
![Screenshot_2025-10-28-22-41-39-02_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/6c96205c-60c7-432f-8d75-16a6654e045d)
![Screenshot_2025-10-29-08-34-32-00_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/cd83a3ab-efbd-4a0e-a62a-0ef6955ae5af)
![Screenshot_2025-10-29-08-35-14-93_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/4bd02972-3f99-43f3-8b2d-1e80a07b87a6)
![Screenshot_2025-10-29-08-40-14-01_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/355629ef-1430-4039-9115-77a3ba47a151)
![Screenshot_2025-10-29-08-42-03-76_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/80fccf5e-524e-40c7-96b2-095c488e599d)
![Screenshot_2025-10-29-08-42-03-76_40deb401b9ffe8e1df2f1cc5ba480b12](https://github.com/user-attachments/assets/3ae7f7ea-e319-44c6-aa54-35431d52918b)





🌱 Future Improvements

Add more crop types (Papaya, Citrus, Leaf diseases)

Android mobile app

Cloud deployment (Render / AWS / Railway)

Real-time camera-based detection
