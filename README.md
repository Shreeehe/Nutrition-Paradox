# Nutrition Paradox Dashboard 🥗📊

This Streamlit dashboard explores the global paradox of **rising obesity and persistent malnutrition** using WHO public datasets from 2012 to 2022.

## 🌍 Project Summary

Despite modern advancements, the world faces two extreme nutrition challenges:

- **Obesity** is growing rapidly in high- and middle-income countries due to lifestyle changes and unhealthy diets.
- **Malnutrition** still persists, especially in low-income and developing regions, impacting children and vulnerable groups.

This project visualizes and compares these dual health burdens across countries, regions, gender, and age groups.

---

## 🚀 Features

### 1. Obesity Dashboard
- Top regions and countries with highest obesity rates.
- Gender and age-based comparisons.
- Global trend visualization.
- Data reliability insights using confidence intervals.
- Countries with consistent low obesity.

### 2. Malnutrition Dashboard
- Most affected countries and age groups.
- African region focus and country-specific trends.
- Gender disparities and CI width analysis.
- Year-wise comparison of minimum and maximum malnutrition.
- High-risk countries monitoring.

### 3. Combined Insights
- Obesity vs malnutrition side-by-side.
- Gender-based nutrition disparity.
- Region-wise comparison: Africa vs Americas.
- Countries improving in malnutrition but worsening in obesity.
- Adult vs child trend analysis.

---

## 📁 Files

- `final_obesity_data.csv` – Cleaned WHO data on obesity.
- `final_malnutrition_data.csv` – Cleaned WHO data on malnutrition.
- `app.py` – Streamlit code for dashboard.

---

## 📦 How to Run

```bash
git clone https://github.com/your-username/nutrition-paradox-dashboard.git
cd nutrition-paradox-dashboard
pip install -r requirements.txt
streamlit run app.py
