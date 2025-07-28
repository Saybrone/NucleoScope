# NucleoScope  
AI-Powered Gamma-Ray Energy Prediction from Nuclear Energy Levels  

## Overview
NucleoScope is an AI-based model designed to predict gamma-ray transition energies in nuclear decay using fundamental nuclear level properties. It leverages deep learning to map relationships between:
- Start Level Energy (in keV)
- Spin (J)
- Parity (π)

and predicts the gamma-ray energy emitted during transitions.

This model is trained on nuclear structure data extracted from ENSDF (Evaluated Nuclear Structure Data File) and processed into a structured format suitable for machine learning.

---

## Key Features
- Predict gamma-ray energies from minimal nuclear parameters.
- Uses TensorFlow deep neural network for regression.
- Supports interactive prediction (GUI or CLI).
- Model and scaler included for easy deployment.
- Trained with normalized data using `StandardScaler`.

---

## Why This Project?
Predicting gamma-ray energies is crucial in:
- Nuclear Physics Research – Understanding nuclear structure and decay schemes.
- Nuclear Medicine – Designing isotopes for imaging and therapy.
- Nuclear Safety & Forensics – Detecting isotopic signatures for non-proliferation.
- Educational Tools – Demonstrating AI in nuclear science.

---

## Tech Stack
- Python 3.12
- TensorFlow / Keras – Neural network modeling
- Pandas & NumPy – Data processing
- Scikit-learn – Data normalization
- Matplotlib – Visualization

---

## Project Structure
