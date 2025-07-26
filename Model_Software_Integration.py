import tkinter as tk
from tkinter import messagebox
import numpy as np
import tensorflow as tf
import joblib

# Load the trained model and scaler
model = tf.keras.models.load_model("SelectedModel.h5", compile=False)
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
scaler = joblib.load("SelectedModel.pkl")

def predict_gamma():
    try:
        energy = float(entry_energy.get())
        spin = float(entry_spin.get())
        parity = int(entry_parity.get())
        
        # Prepare input
        input_data = np.array([[energy, spin, parity]])
        input_scaled = scaler.transform(input_data)
        
        # Predict
        prediction = model.predict(input_scaled)[0][0]
        messagebox.showinfo("Prediction", f"Predicted Gamma Energy: {prediction:.2f} keV")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create GUI
root = tk.Tk()
root.title("Gamma Energy Predictor")

tk.Label(root, text="Start Level Energy [keV]:").grid(row=0, column=0, padx=10, pady=5)
entry_energy = tk.Entry(root)
entry_energy.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Spin:").grid(row=1, column=0, padx=10, pady=5)
entry_spin = tk.Entry(root)
entry_spin.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Parity (+1 or -1):").grid(row=2, column=0, padx=10, pady=5)
entry_parity = tk.Entry(root)
entry_parity.grid(row=2, column=1, padx=10, pady=5)

predict_button = tk.Button(root, text="Predict", command=predict_gamma)
predict_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()