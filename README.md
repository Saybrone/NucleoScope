# NucleoScope  
AI-Powered Gamma-Ray Energy Prediction from Nuclear Energy Levels  

## Overview
NucleoScope is an AI-based model designed to predict gamma-ray transition energies in nuclear decay using fundamental nuclear level properties. It leverages deep learning to map relationships between:
- Start Level Energy (in keV)
- Spin (J)
- Parity (π)

and predicts the gamma-ray energy emitted during transitions.

This model is trained on nuclear structure data extracted from International Atomic Energy Agency (IAEA) and processed into a structured format suitable for machine learning.

---

## Key Features
- Predict gamma-ray energies from minimal nuclear parameters.
- Uses TensorFlow deep neural network for regression.
- Supports interactive prediction (GUI or CLI).
- Model and scaler included for easy deployment.
- Trained with normalized data using `StandardScaler`.

---

## Why This Project?
Accurate prediction of gamma-ray transition energies plays a significant role in several critical domains:
- **Nuclear Physics Research** – Facilitates the study of nuclear structure, energy levels, and decay pathways, enabling deeper insights into fundamental interactions.  
- **Nuclear Medicine** – Assists in the selection and optimization of isotopes for diagnostic imaging and targeted radiotherapy, improving patient outcomes.  
- **Nuclear Safety and Non-Proliferation** – Supports monitoring and analysis of radioactive materials for security, safeguards, and forensic investigations.  
- **Education and Training** – Serves as an advanced, interactive tool to demonstrate the application of machine learning in nuclear science, enhancing both academic research and student engagement.  

---

## Tech Stack
- Python 3.12
- TensorFlow / Keras – Neural network modeling
- Pandas & NumPy – Data processing
- Scikit-learn – Data normalization
- Matplotlib – Visualization

---

## Project Structure
```
NucleoScope/
├── U235 Gamma Decay Prediction Model/
│ ├── TrainingPeriodU235.ipynb 
│ ├── U-235_ModelEvaluation.png 
│ ├── U235GammaModel.h5 
│ ├── U235Scaler.pkl
│ ├── U235_NDSData.csv
│ └── README.md                  
├── Model_Software_Integration.py                   
├── requirements.txt                             
├── LICENSE                 
└── README.md             
```

## How It Works
### Input Features
- `start level energy [keV]` – Energy of the initial nuclear state.
- `spin` – Total angular momentum of the state.
- `parity` – Nuclear parity (`+` → `1`, `-` → `-1`).

### Output
- `energy [keV]` – Predicted gamma-ray energy for the transition.

### Model Details
- 3-layer fully connected neural network:
  - Dense(128, relu)
  - Dense(64, relu)
  - Dense(32, relu)
  - Output: Dense(1) – Regression output
- Loss function: Mean Squared Error (MSE)
- Optimizer: Adam

---
## Usage
### 1. Clone Repository
```bash
git clone https://github.com/Saybrone/NucleoScope.git
cd NucleoScope
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### Important Notes
- Tkinter is included with most Python installations. On some Linux systems, you may need to install it separately:
```bash
sudo apt-get install python3-tk
```
### 3. Modify the neural network to match the desired model
```bash
Example: model = tf.keras.models.load_model("Model.h5", compile=False) ---> model = tf.keras.models.load_model("U235 Gamma Decay Prediction Model
/U235GammaModel.h5", compile=False)
```
### 4. Modify the scaler transformation to match the desired model
```bash
Example: scaler = joblib.load("Model.pkl") ---> scaler = joblib.load("/U235 Gamma Decay Prediction Model
/U235Scaler.pkl")
```
