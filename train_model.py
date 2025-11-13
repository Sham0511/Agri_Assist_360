import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt
import os
import json

# Define paths for dataset, model, and output files
dataset_path = 'dataset'
model_save_path = 'model/fruit_model.h5'
plot_save_path = 'model/training_plot.png'
class_index_path = 'model/class_indices.json'

# Create the model directory if it doesn't exist
os.makedirs(os.path.dirname(model_save_path), exist_ok=True)

# Use ImageDataGenerator for data augmentation and preprocessing
# It will rescale pixel values to a range of 0-1 and split data for validation
datagen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2
)

# Create a training data generator from the dataset directory
train_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(128, 128),  # Resize all images to 128x128
    batch_size=16,           # Load 16 images at a time
    class_mode='categorical',# Use one-hot encoded labels for training
    subset='training'        # Use the training portion of the data
)

# Create a validation data generator
val_generator = datagen.flow_from_directory(
    dataset_path,
    target_size=(128, 128),
    batch_size=16,
    class_mode='categorical',
    subset='validation'      # Use the validation portion of the data
)

# Print the classes detected by the generator
print("✅ Detected Classes:")
for class_name, index in train_generator.class_indices.items():
    print(f"{class_name}: {index}")

# Save the class indices to a JSON file for later use by app.py
with open(class_index_path, 'w') as f:
    json.dump(train_generator.class_indices, f)
print(f"✅ class_indices.json saved at: {class_index_path}")

# Build the Convolutional Neural Network (CNN) model
model = Sequential([
    # First convolutional layer with 32 filters
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    
    # Second convolutional layer with 64 filters
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    # Flatten the 3D output to 1D
    Flatten(),
    
    # Fully connected dense layer
    Dense(128, activation='relu'),
    
    # Output layer with a node for each class
    Dense(train_generator.num_classes, activation='softmax')
])

# Compile the model with Adam optimizer and categorical cross-entropy loss
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10  # Train for 10 epochs
)

# Save the trained model to a file
model.save(model_save_path)
print(f"✅ Model saved to: {model_save_path}")

# Plot the training and validation accuracy and loss
plt.figure(figsize=(12, 5))

# Plot accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy', color='green')
plt.plot(history.history['val_accuracy'], label='Val Accuracy', color='orange')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Plot loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss', color='red')
plt.plot(history.history['val_loss'], label='Val Loss', color='blue')
plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig(plot_save_path)
plt.show()

print(f"📊 Training plot saved at: {plot_save_path}")