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

## Files

- `Main.ipynb` – Jupyter Notebook used to extract and preprocess data from WHO API.
- `final_obesity_data.csv` – Cleaned obesity dataset.
- `final_malnutrition_data.csv` – Cleaned malnutrition dataset.
- `app.py` – Streamlit dashboard for visualizing insights.

---

## How to Run

1. (Optional) Run `Main.ipynb` to regenerate or update data from WHO API.
2. Launch the dashboard:

```bash
pip install -r requirements.txt
streamlit run app.py
