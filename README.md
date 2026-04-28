# Workforce Demand Forecasting for Transportation Operations

## 1. Project Title and Description
This project develops a machine learning model to forecast **station-level ridership** as a proxy for **workforce demand** in transportation operations.  
Using historical scheduling records, weather data, and operational context, the model predicts expected ridership per shift to support more accurate staffing decisions and reduce scheduling mismatches.

---

## 2. Problem Statement
Transportation companies rely on accurate workforce scheduling to maintain operational efficiency, avoid delays, and control labor costs.  
However, staffing needs fluctuate daily due to:

- Weather conditions  
- Station-level demand differences  
- Shift patterns  
- Seasonal variations  
- Special events  

When forecasts are inaccurate, organizations risk:

- **Understaffing** → delays, safety risks, service degradation  
- **Overstaffing** → unnecessary labor costs  

This project builds a regression model to predict ridership per shift/day, enabling a **10–15% improvement in scheduling accuracy**.

---

## 3. Dataset Source and Description

### **Internal Data (Primary Source)**
Workforce scheduling records containing:
- `date`
- `employee_name`
- `station_id`
- `shift_start`, `shift_end`
- `ridership`

### **External Data (Supporting Features)**
- Philippine holiday calendar  
- Historical weather information  
- Public ridership indicators  

### **Final Dataset Summary**
- **430 cleaned records**  
- **5 stations**  
- **3 shift types**  
- **4 weather categories**  
- Missing values handled, duplicates removed, outliers capped

---

## 4. Installation Instructions

### **Clone the repository**
```bash
git clone https://github.com/<your-username>/workforce-demand-forecasting.git
cd workforce-demand-forecasting
```

### **Create a virtual environment (optional)**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 5. How to Run the Code

### **Option A — Run the Jupyter Notebook**
1. Open the notebook:
   ```bash
   jupyter notebook notebooks/Tacason_Raymond_Pillar5_Capstone.ipynb
   ```
2. Run all cells
3. Outputs include:
   - Data cleaning  
   - EDA  
   - Feature engineering  
   - PCA  
   - Model training  
   - Feature importance  
   - SHAP explainability  

### **Option B — Run the Python scripts (if using src/ folder)**
```bash
python src/data_preprocessing.py
python src/feature_engineering.py
python src/model_training.py
```

---

## 6. Results Summary

### **Key Findings**
- **Station-level features** (especially `station_mean_ridership`) are the strongest predictors.  
- **Weather conditions** (Rain, Storm) significantly influence ridership.  
- **Shift patterns** show expected operational differences (afternoon > morning > night).  

### **Model Performance**  
*(Insert your actual metrics once computed)*

| Model | RMSE | MAE | R² | Notes |
|-------|------|------|------|--------|
| Random Forest | 64.65 | 39.95 | 0.9983 | best model, lowest RMSE, Highest R2, Good training time  |
| Decision Tree | 73.93 | 31.39 | 0.9978 | second best, slighly worse than RF |
| XGBoost | 96.30 | 49.55 | 0.9963 | third best, good but not better than RF |
| Linear Regression | 156.05 | 121.03 | 0.9903 | weakest, too simple for dataset |

### **Explainability**
- Random Forest feature importance confirms strong spatial and weather effects.  
- SHAP visualizations provide global and local interpretability.

---

## 7. Author Information

**Author:** Raymond Tacason  
**Location:** Pasig, Metro Manila, Philippines  
**Role:** SAP WFS Analyst & Data Science Capstone Student  
**Date Completed:** April 2026  

---
