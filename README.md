# Nutrition-Paradox
A Global View on Obesity and Malnutrition.
🧾 Project Summary: Nutrition Paradox – A Global View on Obesity and Malnutrition

🌍 Overview:
This project explores the global nutrition paradox — where obesity and malnutrition coexist across regions and populations. Using data from WHO APIs (2012–2022), the project focuses on trends by region, gender, age group, and year.

📦 Data Sources:
WHO Global Health Observatory APIs

Four datasets:

Adult Obesity (BMI ≥ 30)

Child Obesity (BMI ≥ 2 SD)

Adult Underweight (BMI < 18.5)

Child Thinness (BMI < -2 SD)

Cleaned, merged, and enriched using Python and MySQL

Exported to Power BI for interactive visualizations

🔍 Key Transformations:
Added Age, CI_Width, Obesity_Level, and Malnutrition_Level

Mapped missing Region using Country

Cleaned gender codes (SEX_MLE → Male, etc.)

Removed records with incomplete values

📊 Dashboard Features:
📈 Trends: Obesity & Malnutrition over time

🌍 Map: Country-wise comparison

🧍‍♀️🧍 Gender-based breakdown

📊 Top 10 countries (both obesity & malnutrition)

✅ Confidence Interval width check for data reliability

💡 Key Insights:
Africa & South-East Asia show high malnutrition, especially among children

Europe & Americas lead in adult obesity, especially among females

Some countries (like India) show dual burden: low BMI in kids, rising obesity in adults

Gender-based trends show females often have higher obesity, males slightly higher malnutrition in some regions

CI width suggests some low-income nations have less consistent data, needing cautious interpretation

🛠️ Tools Used:
Python (Pandas, PyCountry)

MySQL (Data Storage)

Power BI (Dashboard)

WHO API (Real-time Data Source)

📁 Deliverables:
final_obesity_data.csv

final_malnutrition_data.csv

nutrition_paradox_dashboard.pbix
