from flask import Flask, request, render_template, redirect
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# ✅ Load model 
try:
    model = tf.keras.models.load_model('model/fruit_model.h5')
    print("✅ Model loaded successfully.")
except Exception as e:
    print("❌ Failed to load model:", e)
    model = None

# ✅ Load class indices
try:
    with open('model/class_indices.json', 'r') as f:
        class_indices = json.load(f)
        class_names = [None] * len(class_indices)
        for label, index in class_indices.items():
            class_names[index] = label
    print("✅ Class indices loaded.")
except Exception as e:
    print("❌ Failed to load class_indices.json:", e)
    class_names = []

# ✅ Tamil translation
tamil_labels = {
    "Fresh": "புதியது",
    "Rotten": "அழுகியது",
    "Unripe": "பச்சை"
}

# ✅ Load crop info
crop_data = {}
try:
    with open('data/crop_info.json', encoding='utf-8') as f:
        crop_data = json.load(f)
        print("✅ Crop info loaded.")
except Exception as e:
    print("❌ crop_info.json loading failed:", e)

# ✅ Fruits and vegetables
fruits = [
    {"name_en": "Banana", "name_ta": "வாழைப்பழம்", "image": "banana.jpg"},
    {"name_en": "Apple", "name_ta": "ஆப்பிள்", "image": "apple.jpg"},
    {"name_en": "Mango", "name_ta": "மாம்பழம்", "image": "mango.jpg"}
]
vegetables = [
    {"name_en": "Tomato", "name_ta": "தக்காளி", "image": "tomato.jpg"}
]

@app.route('/')
def home():
    lang = request.args.get('lang', 'en')
    return render_template('home.html', lang=lang)

@app.route('/category/<type>')
def category(type):
    lang = request.args.get('lang', 'en')
    items = fruits if type == 'fruits' else vegetables
    return render_template('category.html', lang=lang, items=items, type=type)

@app.route('/item/<crop_name>')
def item_detail(crop_name):
    lang = request.args.get('lang', 'en')
    info = crop_data.get(crop_name, {})
    return render_template('item_detail.html', lang=lang, crop_name=crop_name, info=info)

@app.route('/predict', methods=['POST'])
def predict():
    lang = request.args.get("lang", "en")
    crop_name = request.args.get("crop", "")
    file = request.files.get('file')

    if not model or not file or file.filename == '':
        return redirect(request.url)

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    base, ext = os.path.splitext(file.filename)
    counter = 1
    while os.path.exists(filepath):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{base}_{counter}{ext}")
        counter += 1
    file.save(filepath)

    # 🔍 Preprocess
    img = image.load_img(filepath, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]

    # 🔎 Filter classes related only to the selected crop
    related_classes = [cls for cls in class_names if cls.startswith(crop_name)]
    related_indices = [class_names.index(cls) for cls in related_classes]

    filtered_probs = prediction[related_indices]
    best_index_in_filtered = np.argmax(filtered_probs)
    predicted_label = related_classes[best_index_in_filtered]

    print("🎯 Filtered Prediction:", predicted_label)

    fruit, stage = predicted_label.split("_", 1)
    predicted_display = f"{fruit} - {tamil_labels.get(stage, stage)}" if lang == "ta" else f"{fruit} - {stage}"

    # 📊 RGB Graph
    img_data = image.img_to_array(image.load_img(filepath)) / 255.0
    plt.figure(figsize=(6, 4))
    for i, color in enumerate(['red', 'green', 'blue']):
        plt.plot(img_data[:, :, i].mean(axis=0), color=color, label=color.upper())
    plt.legend()
    plt.title('RGB Color Spread')
    hist_path = os.path.join(app.config['UPLOAD_FOLDER'], 'color_graph.png')
    plt.savefig(hist_path)
    plt.close()

    # 📅 Harvest Alert
    current_month = datetime.datetime.now().strftime("%B")
    season = crop_data.get(fruit, {}).get('season', [])
    is_season = "All" in season or current_month in season
    alert_msg = "✅ இது அறுவடை பருவம்!" if (is_season and lang == "ta") else ("✅ Harvest season is active!" if is_season else "")

    return render_template('item_detail.html',
                           lang=lang,
                           crop_name=crop_name,
                           prediction=predicted_display,
                           img_path=f'uploads/{os.path.basename(filepath)}',
                           hist_path='uploads/color_graph.png',
                           alert_msg=alert_msg,
                           info=crop_data.get(crop_name, {}))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)