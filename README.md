<div align="center">
  <img src="app/ecoshare_logo.png" alt="EcoShare Logo" width="150">
  <br/>
  <h1><b>EcoShare</b></h1>
  <p><i>Give waste a new life.</i></p>

  <!-- Badges -->
  <p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
    <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
    <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  </p>
</div>

---

## 🌐 Project Overview

**EcoShare** is a web platform that bridges the gap between those with excess food and those in need, especially plant caretakers. It promotes sustainability and community cooperation by providing a simple, intuitive interface for donations and requests.

---

## 🧩 Features

- ⚡ **Real-time Listings**
- 💬 **Integrated Messaging**
- 🗺️ **Interactive Map Listings**
- 🤖 **Chatbot Assistant**
- 🧪 **Plant Nutrient Diagnostics**
- 🧱 **Plant Nutrient Builder**

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager
- ngrok account (for public URL tunneling)

### 1. Clone the Repository

```bash
git clone https://github.com/kkreiju/EcosharePython.git
cd EcosharePython
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup ngrok

1. **Download ngrok**: Place the `ngrok.exe` file in the `ngrok/` directory
2. **Authenticate ngrok**: 
   ```bash
   ./ngrok/ngrok.exe authtoken YOUR_NGROK_AUTH_TOKEN
   ```

### 4. Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
NGROK_ID=your-unique-ngrok-id
```

Replace `your-unique-ngrok-id` with your specific identifier for the backend API.

### 5. Train the Model (Optional)

If you want to retrain the plant disease detection model:

```bash
python train/train_model.py
```

This will:
- Use the plant disease images from the `dataset/` directory
- Train a TensorFlow/Keras model
- Save the trained model to `model_files/plant_model.keras`

**Dataset Structure:**
```
dataset/
├── Bell Pepper Healthy/
├── Bell Pepper Unhealthy/
├── Bitter Gourd Healthy/
├── Bitter Gourd Unhealthy/
├── Cabbage Healthy/
├── Cabbage Unhealthy/
└── ... (other plant categories)
```

### 6. Run the Server

Start the Flask application with ngrok tunnel:

```bash
python app.py
```

This will:
- 🚀 Start the ngrok tunnel automatically
- 🌐 Display your public URL in the console
- ✅ Notify the backend API with your ngrok URL
- 🖥️ Start the Flask server on `http://localhost:5000`

The application will be accessible via:
- **Local**: `http://localhost:5000`
- **Public**: The ngrok URL displayed in the console

---

## 📁 Project Structure

```
EcosharePython/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── app/                  # Flask application modules
│   ├── __init__.py
│   ├── routes.py
│   └── model/            # ML model components
├── dataset/              # Training dataset
├── model_files/          # Trained model files
├── ngrok/               # ngrok executable
└── train/               # Model training scripts
    └── train_model.py
```