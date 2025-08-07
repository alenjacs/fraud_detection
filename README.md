# Bank Transaction Fraud Detection

This project applies machine learning to detect fraudulent credit card transactions using a real-world, highly imbalanced dataset.

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/alenjacs/fraud_detection
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download the dataset from Kaggle and place `creditcard.csv` in the root folder. (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

4. Run the notebook:
Open `fraud_detection.ipynb` in Jupyter or VS Code and run all cells.

---

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