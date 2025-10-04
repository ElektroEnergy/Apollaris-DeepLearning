from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow import keras, layers
import numpy as np
import pandas as pd

from factory import factory
from factory import seeds

x_values = seeds(100)

X = [x_values[:, 0], x_values[:, 1], x_values[:, 2], x_values[:, 3], x_values[:, 4]]

y_values = factory(x_values, 100)

y_module =  y_values[:, 0]
y_inverter = y_values[:, 1]
y_power_required = y_values[:, 2]
y_nmod = y_values[:, 3]
y_ninv = y_values[:, 4]
y_total_ipmd = y_values[:, 5]
y_total_ipinv = y_values[:, 6]
y_ipsys = y_values[:, 7]

# Data Normalization
enconder = LabelEncoder()
y_module = enconder.fit_transform(y_module)
y_inverter = enconder.fit_transform(y_inverter)

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_module_train, y_module_test, y_inverter_train, y_inverter_test, = train_test_split(
    X, y_nmod, y_selection, y_power, y_sysindex, test_size=0.2, random_state=42
)

# Defining Model
inputs = keras.Input(shape=(X_train.shape[1],))

# Shared layers
x = layers.Dense(128, activation="relu")(inputs)
x = layers.Dropout(0.3)(x)
x = layers.Dense(64, activation="relu")(x)

# Output layers
out_nmod = layers.Dense(1, name="nmod")(x)
out_selection = layers.Dense(len(np.unique(y_selection)), activation="softmax", name="selection")(x)
out_power = layers.Dense(1, name="power")(x)
out_sysindex = layers.Dense(1, name="sysindex")(x)

# Compile Model
model = keras.Model(inputs=inputs, outputs=[out_nmod, out_selection, out_power, out_sysindex])
model.compile(
    optimizer="adam",
    loss={
        "nmod": "mse",
        "selection": "sparse_categorical_crossentropy",
        "power": "mse",
        "sysindex": "mse",
    },
    metrics={
        "nmod": ["mae"],
        "selection": ["accuracy"],
        "power": ["mae"],
        "sysindex": ["mae"],
    },
)

# Train Model
history = model.fit(
    X_train,
    {
        "nmod": y_nmod_train,
        "selection": y_selection_train,
        "power": y_power_train,
        "sysindex": y_sysindex_train,
    },
    validation_split=0.2,
    epochs=100,
    batch_size=32,
)

# Save the model to a file
model.save('decisionmaking.h5')