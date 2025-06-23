# 🥗 Nutrition Paradox Dashboard (Obesity & Malnutrition Explorer)

This interactive **Streamlit Dashboard** explores the **global paradox** of rising **obesity** and persistent **malnutrition** using WHO datasets (2012–2022). It provides insights by country, gender, region, and age — highlighting the nutritional divide across the world.

---

## 🌍 Project Highlights

- Visualize obesity and malnutrition patterns across **countries, regions, genders, and ages**
- Built-in **BMI calculator** for quick health checks
- Randomized **nutrition and weight-loss tips** to educate and engage users
- Beautiful **global map** overlay to visualize obesity and malnutrition data distribution
- Powered by **real WHO data**, cleaned and structured.

---

## 🚀 Features

### 🏠 Home Page
- **BMI Calculator**: Input height and weight to view health status
- **Nutrition Tip of the Day**: One helpful daily nutrition insight
- **Obesity Tip of the Day**: One daily advice for reducing obesity
- **Nutrition World Map**: Interactive global view with colored dots for Obesity (🔴) and Malnutrition (🔵)

### 🍩 Obesity Dashboard
- Top 5 Regions & Countries by average obesity
- India-specific obesity trend (2012–2022)
- Gender & Age-based Obesity Averages
- Consistently low-obesity countries
- Data reliability analysis (CI Width)
- Female vs Male obesity gap
- Global obesity trend line

### 🍵 Malnutrition Dashboard
- Highest malnutrition countries and age analysis
- African region trend focus
- Gender disparities & CI width analysis
- Countries with increasing malnutrition
- Year-wise min vs max comparison

### 🔗 Combined Insights
- Compare obesity & malnutrition by country, region, gender, and age
- Spot countries improving in malnutrition but worsening in obesity

---

## 🧾 Files

| File | Description |
|------|-------------|
| `app.py` | Final Streamlit app script |
| `final_obesity_data.csv` | Cleaned obesity dataset |
| `final_malnutrition_data.csv` | Cleaned malnutrition dataset |
| `clean_loca.csv` | Country-wise lat/lon with type (obesity or malnutrition) |
| `Main.ipynb` | Data extraction + preprocessing from WHO API |
| `EDA.ipynb` | Data exploration and analysis |

---

## 💻 How to Run It Locally

```bash
# Step 1: Clone the repository
git clone https://github.com/your-username/nutrition-paradox-dashboard.git
cd nutrition-paradox-dashboard

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Launch Streamlit app
streamlit run app.py
