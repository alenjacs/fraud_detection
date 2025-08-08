

# Bank Transaction Fraud Detection

This project applies machine learning to detect fraudulent credit card transactions using a real-world, highly imbalanced dataset.

---

## How to Run

### Option 1: Run in Google Colab 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alenjacs/fraud_detection/blob/main/notebooks/fraud_detection.ipynb)

1. Click the "Open in Colab" badge at the top of this README.
2. The notebook will:
   - Automatically install required packages
   - Automatically download the dataset from Google Drive
3. Run all cells in the notebook.

### Option 2: Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/alenjacs/fraud_detection
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. The dataset will be automatically downloaded by the notebook. No manual download needed.

4. Run the notebook:
   Open `fraud_detection.ipynb` in Jupyter or VS Code and run all cells.


---

## How to Run the App

👉 [Click here to try the app online](https://frauddetection-bwebwb2uffxx2ej6bzzdjk.streamlit.app)

No setup needed — just upload `creditcard.csv` and view results instantly.

---
## How to Run the App (locally)

### 1. Navigate to the project directory:
```bash
cd fraud_detection
```

### 2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit web app:
```bash
streamlit run app.py
```

### 4. In your browser:
- The app will open at `http://localhost:8501`
- Upload your `creditcard.csv` file when prompted
- View predictions, visualizations, and model insights

> ⚠️ This Streamlit app cannot run in Google Colab. It must be executed locally using the above steps.

## Dataset
- Source: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Size: ~284,000 transactions
- Fraud Rate: ~0.17%

**Note**: The dataset (`creditcard.csv`) is not included in this repo because it exceeds GitHub’s 100 MB limit. Download it from Kaggle and place it in your project folder manually.

---

## Model Summary
- Model: Random Forest Classifier
- Balancing: SMOTE (Synthetic Minority Oversampling Technique)
- Training: 80% of the data with SMOTE applied
- Testing: 20% held out for evaluation

---

## Results
- Accuracy: ~99.9%
- Precision (fraud): 86%
- Recall (fraud): 85%
- F1-score (fraud): 86%

Focus was on recall to ensure most fraud cases are detected.

---

## Top Features
- V14, V17, V12, V10, V16  
(Discovered using feature importance from Random Forest)

---

## Tools & Libraries
- Python
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- imbalanced-learn
- Jupyter Notebook

---