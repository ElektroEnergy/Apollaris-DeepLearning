import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_USE_LEGACY_KERAS'] = '1'

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import tensorflow as tf
from tf_keras import layers, Model, Input
import numpy as np
import joblib
import json

from learning.factory import factory
from learning.factory import seeds
from utils.io import Console

# Disable annoying Tensorflow warnings in a production env
tf.get_logger().setLevel('ERROR')

# Send header
Console.send_header("Trainer")

# Generation of data to training
Console.send_info('Begin generating the data. This can take a while depending on your computer and the size of the seeds, go get some coffee for you.')
x_values = np.array(seeds(100000))
X = np.column_stack([x_values[:, 0], x_values[:, 1], x_values[:, 2], x_values[:, 3]])

y_values = np.array(factory(x_values, 100000))
y_module = y_values[:, 0]
y_inverter = y_values[:, 1]
y_power = y_values[:, 2]
y_nmod = y_values[:, 3]
y_ninv = y_values[:, 4]
y_total_ipmd = y_values[:, 5]
y_total_ipinv = y_values[:, 6]
y_ipsys = y_values[:, 7]

# Normalization
encoder_module = LabelEncoder()
y_module = encoder_module.fit_transform(y_module)

encoder_inverter = LabelEncoder()
y_inverter = encoder_inverter.fit_transform(y_inverter)

# Saving encoders
joblib.dump(encoder_module, 'learning/output/encoder_module.pkl')
joblib.dump(encoder_inverter, 'learning/output/encoder_inverter.pkl')

# Normalization of X
scaler_x = StandardScaler()
X = scaler_x.fit_transform(X)

# Save X encoder
joblib.dump(scaler_x, 'learning/output/scaler_x.pkl')

# Normalization of numerics Y
scalers_y = {}
def scale_target(name, arr):
    arr = arr.reshape(-1, 1)
    scaler = MinMaxScaler()
    arr_scaled = scaler.fit_transform(arr)
    scalers_y[name] = scaler
    return arr_scaled

y_power = scale_target("power", y_power)
y_nmod = scale_target("nmod", y_nmod)
y_ninv = scale_target("ninv", y_ninv)
y_total_ipmd = scale_target("total_ipmd", y_total_ipmd)
y_total_ipinv = scale_target("total_ipinv", y_total_ipinv)
y_ipsys = scale_target("ipsys", y_ipsys)

# Save Y scaler
joblib.dump(scalers_y, 'learning/output/scalers_y.pkl')

Console.send_success('All scalers and encoders saved.')

# Data splitting
arrays = [X, y_module, y_inverter, y_power, y_nmod, y_ninv, y_total_ipmd, y_total_ipinv, y_ipsys]
splits = train_test_split(*arrays, test_size=0.2, random_state=42)

(
    X_train, X_test,
    y_module_train, y_module_test,
    y_inverter_train, y_inverter_test,
    y_power_train, y_power_test,
    y_nmod_train, y_nmod_test,
    y_ninv_train, y_ninv_test,
    y_total_ipmd_train, y_total_ipmd_test,
    y_total_ipinv_train, y_total_ipinv_test,
    y_ipsys_train, y_ipsys_test
) = splits

# Defining the inputs and the model
inputs = Input(shape=(X_train.shape[1],))
x = layers.Dense(128, activation="relu")(inputs)
x = layers.Dense(64, activation="relu")(x)

out_module = layers.Dense(len(np.unique(y_module)), activation="softmax", name="module")(x)
out_inverter = layers.Dense(len(np.unique(y_inverter)), activation="softmax", name="inverter")(x)
out_power = layers.Dense(1, name="power")(x)
out_nmod = layers.Dense(1, name="nmod")(x)
out_ninv = layers.Dense(1, name="ninv")(x)
out_total_ipmd = layers.Dense(1, name="total_ipmd")(x)
out_total_ipinv = layers.Dense(1, name="total_ipinv")(x)
out_ipsys = layers.Dense(1, name="ipsys")(x)

model = Model(
    inputs=inputs,
    outputs=[out_module, out_inverter, out_power, out_nmod, out_ninv, out_total_ipmd, out_total_ipinv, out_ipsys]
)

# Compile the model
model.compile(
    optimizer="adam",
    loss={
        "module": "sparse_categorical_crossentropy",
        "inverter": "sparse_categorical_crossentropy",
        "power": "mse",
        "nmod": "mse",
        "ninv": "mse",
        "total_ipmd": "mse",
        "total_ipinv": "mse",
        "ipsys": "mse",
    },
    loss_weights={
        "module": 3.0,
        "inverter": 3.0,
        "power": 2.0,
        "nmod": 1.0,
        "ninv": 1.0,
        "total_ipmd": 1.0,
        "total_ipinv": 1.0,
        "ipsys": 1.5,
    },
    metrics={
        "module": ["accuracy"],
        "inverter": ["accuracy"],
        "power": ["mae"],
        "nmod": ["mae"],
        "ninv": ["mae"],
        "total_ipmd": ["mae"],
        "total_ipinv": ["mae"],
        "ipsys": ["mae"],
    },
)

# Train the model
Console.send_info('Begin training...')
history = model.fit(
    X_train,
    {
        "module": y_module_train,
        "inverter": y_inverter_train,
        "power": y_power_train,
        "nmod": y_nmod_train,
        "ninv": y_ninv_train,
        "total_ipmd": y_total_ipmd_train,
        "total_ipinv": y_total_ipinv_train,
        "ipsys": y_ipsys_train,
    },
    validation_split=0.2,
    epochs=500,
    batch_size=32,
)

# Save the model in the default Keras format
model.save('learning/output/decisionmaking.keras')

# Save the model for Tensorflow.JS

# Numpy retrocompatibility
np.object = object
np.bool = bool
import tensorflowjs as tfjs

tfjs.converters.save_keras_model(model, "learning/output/web_model")

# Convert the scalers and encoders
scalers_data = {
    "x": {"mean": scaler_x.mean_.tolist(), "scale": scaler_x.scale_.tolist()},
    "y": {k: {
            "min": v.data_min_.tolist(),
            "max": v.data_max_.tolist(),
            "range": v.data_range_.tolist(),
            "scale": v.data_range_.tolist(),
            "feature_range": v.feature_range,
        } for k, v in scalers_y.items()}
}

with open('learning/output/web_model/scalers.json', 'w') as file:
    json.dump(scalers_data, file)

encoders_data = {
    "module": encoder_module.classes_.tolist(),
    "inverter": encoder_inverter.classes_.tolist()
}

with open('learning/output/web_model/encoders.json', 'w') as file:
    json.dump(encoders_data, file)

Console.send_success('Model saved to learning/output')