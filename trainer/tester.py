import numpy as np
import tensorflow as tf
from tensorflow import keras
import joblib

from utils.io import Console

# Load model, scalers and encoders
Console.send_info("Loading models, scalers and encoders...")

model = keras.models.load_model('decisionmaking.keras')

# Load the scalers and encoders
scaler_x = joblib.load('scaler_x.pkl')
scaler_y = joblib.load('scaler_y.pkl')
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

y_power_decoded = scaler_y.inverse_transform(y_power_pred)
y_nmod_decoded = scaler_y.inverse_transform(y_nmod_pred)
y_ninv_decoded = scaler_y.inverse_transform(y_ninv_pred)
y_total_ipmd_decoded = scaler_y.inverse_transform(y_total_ipmd_pred)
y_total_ipinv_decoded = scaler_y.inverse_transform(y_total_ipinv_pred)
y_ipsys_decoded = scaler_y.inverse_transform(y_ipsys_pred)

# Print results
for i in range(len(X_new)):
    print(f"\nSystem {i+1}")
    print(f"Module: {y_module_decoded[i]}")
    print(f"Inverter: {y_inverter_decoded[i]}")
    print(f"Power: {y_power_decoded[i][0]:.4f}")
    print(f"Number of Modules: {y_nmod_decoded[i][0]:.2f}")
    print(f"Number of Inverters: {y_ninv_decoded[i][0]:.2f}")
    print(f"Module Performance Index: {y_total_ipmd_decoded[i][0]:.4f}")
    print(f"Inverter Performance Index: {y_total_ipinv_decoded[i][0]:.4f}")
    print(f"Total System Index: {y_ipsys_decoded[i][0]:.4f}")

Console.send_success("All predictions realized.")
