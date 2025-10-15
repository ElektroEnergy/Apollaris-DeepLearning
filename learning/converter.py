import joblib, json

# Command for converting the model
# tensorflowjs_converter --input_format keras decisionmaking.keras trainer/web_model/

scaler_x = joblib.load('learning/output/scaler_x.pkl')
scalers_y = joblib.load('learning/output/scalers_y.pkl')

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

with open("learning/output/web_model/scalers.json", "w") as f:
    json.dump(scalers_data, f)

encoder_module = joblib.load('learning/output/encoder_module.pkl')
encoder_inverter = joblib.load('learning/output/encoder_inverter.pkl')

encoders_data = {
    "module": encoder_module.classes_.tolist(),
    "inverter": encoder_inverter.classes_.tolist()
}

with open("learning/output/web_model/encoders.json", "w") as f:
    json.dump(encoders_data, f)