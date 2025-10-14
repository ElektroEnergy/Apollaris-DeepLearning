import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import math
import tensorflow as tf
from tensorflow import keras
import joblib
import json

# Disable annoying Tensorflow warnings in a production env
tf.get_logger().setLevel('ERROR')

from utils.io import Console

# Send header
Console.send_header("Prediction Maker")

# Load model, scalers and encoders
Console.send_info("Loading models, scalers and encoders...")

model = keras.models.load_model('decisionmaking.keras')

# Load the scalers and encoders
scaler_x = joblib.load('scaler_x.pkl')
scaler_y = joblib.load('scalers_y.pkl')
encoder_module = joblib.load('encoder_module.pkl')
encoder_inverter = joblib.load('encoder_inverter.pkl')

Console.send_success("Loaded with sucess! Now generating data for prediction")

# Generating test data
X_new = np.array([
    [6000, 1000, 30, 5],
    [30000, 1200, 25, 2],
], dtype=float)

X_new_scaled = scaler_x.transform(X_new)

# Prediction
Console.send_info("Making the prediction")

y_pred = model.predict(X_new_scaled)

# Separando as saídas
y_module_pred = np.argmax(y_pred[0], axis=1)
y_inverter_pred = np.argmax(y_pred[1], axis=1)

y_power_pred = y_pred[2]
y_nmod_pred = y_pred[3]
y_ninv_pred = y_pred[4]
y_total_ipmd_pred = y_pred[5]
y_total_ipinv_pred = y_pred[6]
y_ipsys_pred = y_pred[7]

# Desnormalization 
y_module_decoded = encoder_module.inverse_transform(y_module_pred)
y_inverter_decoded = encoder_inverter.inverse_transform(y_inverter_pred)

y_power_decoded = scaler_y['power'].inverse_transform(y_power_pred)
y_nmod_decoded = scaler_y['nmod'].inverse_transform(y_nmod_pred)
y_ninv_decoded = scaler_y['ninv'].inverse_transform(y_ninv_pred)
y_total_ipmd_decoded = scaler_y['total_ipmd'].inverse_transform(y_total_ipmd_pred)
y_total_ipinv_decoded = scaler_y['total_ipinv'].inverse_transform(y_total_ipinv_pred)
y_ipsys_decoded = scaler_y['ipsys'].inverse_transform(y_ipsys_pred)

# Output results
for i in range(len(X_new)):
    with open("data/modules.json", "r", encoding="utf-8") as f:
        modules = json.load(f)['modules']
    
    with open("data/inverters.json", "r", encoding="utf-8") as f:
        inverters = json.load(f)['inverters']
    
    module = next((m for m in modules if m["id"] == int(y_module_decoded[i])), None)['name']
    inverter = next((m for m in inverters if m["id"] == int(y_inverter_decoded[i])), None)['name']
    
    print(f"\nSystem {i+1}")
    print(f"Module: {module}")
    print(f"Inverter: {inverter}")
    print(f"Installed Power: {y_power_decoded[i][0]:.0f}")
    print(f"Number of Modules: {y_nmod_decoded[i][0]:.0f}")
    print(f"Number of Inverters: {y_ninv_decoded[i][0]:.0f}")
    print(f"Module Performance Index: {y_total_ipmd_decoded[i][0]:.6f}")
    print(f"Inverter Performance Index: {y_total_ipinv_decoded[i][0]:.6f}")
    print(f"Total System Index: {y_ipsys_decoded[i][0]:.6f}")

Console.send_success("All predictions realized.")
