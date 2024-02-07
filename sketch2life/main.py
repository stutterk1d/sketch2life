# Copyright 2015 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
# [imports]
from flask import Flask, request, jsonify, render_template, send_file
from io import BytesIO
from tensorflow import keras
from keras.models import load_model
from PIL import Image
import os
import numpy as np
import tensorflow as tf
import base64
import logging

logging.basicConfig(level=logging.DEBUG)

print("Current Working Directory:", os.getcwd())
print("Files in models directory:", os.listdir('./models'))

app = Flask(__name__)

# Load the models
generator = tf.keras.models.load_model('models/generator.h5')  # Consistent import

def preprocess(image):
    img = Image.open(image)
    img = img.resize((256, 256))  # Match dimensions used during training
    img_array = np.array(img)[:,:,:3]  # Take only the first 3 channels
    img_array = (img_array / 127.5) - 1  # Normalize to [-1, 1]
    logging.info(f"Shape of processed_image: {img_array.shape}")
    return np.expand_dims(img_array, axis=0)  # Make batch-sized

def postprocess(tensor):
    tensor = np.squeeze(tensor, axis=0)  # Remove batch dimension
    tensor = (tensor + 1) * 127.5  # Denormalize to [0, 255]
    img = Image.fromarray(tensor.astype('uint8'))
    return img

@app.route('/predict', methods=['POST'])
def predict():
    try:
        logging.info("Received a request for prediction.")
        
        if request.json is None:
            return jsonify({'error': 'Invalid JSON'}), 400
            
        payload = request.json
        
        if "image" not in payload:
            return jsonify({'error': 'Missing image data'}), 400

        data_url = payload["image"]
        logging.debug(f"Data URL received: {data_url[:30]}...")
        
        _, encoded = data_url.split(",", 1)
        binary_data = base64.b64decode(encoded)
        
        logging.info("Successfully decoded base64 image.")
        
        processed_image = preprocess(BytesIO(binary_data))
        
        logging.info("Image preprocessed.")
        
        output = generator.predict(processed_image)
        
        logging.info("Prediction generated.")
        
        result_image = postprocess(output)
        
        logging.info("Postprocessed the result.")
        
        byte_io = BytesIO()
        result_image.save(byte_io, 'PNG')
        byte_io.seek(0)
        
        logging.info("Sending image as response.")
        
        return send_file(byte_io, mimetype='image/png')
        
    except Exception as e:
        print(e)
        logging.error("Exception occurred", exc_info=True)
        return jsonify({'error': 'An error occurred during processing'}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    logging.info("Starting the application.")
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    logging.info("Application terminated.")


