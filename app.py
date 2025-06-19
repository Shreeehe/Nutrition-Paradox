import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Set page config first
st.set_page_config(page_title="Nutrition Paradox Dashboard", layout="wide")

# 📥 Load data
@st.cache_data
def load_data():
    df_obese = pd.read_csv("final_obesity_data.csv")
    df_mal = pd.read_csv("final_malnutrition_data.csv")
    return df_obese, df_mal

df_obese, df_mal = load_data()

# 🧭 Sidebar navigation
page = st.sidebar.radio("Go to:", ["🍩 Obesity Dashboard", "🍵 Malnutrition Dashboard", "🔗 Combined Insights"])

# 🌟 App Title
st.title("🍽️ Nutrition Paradox: Obesity & Malnutrition (2012–2022)")

# ------------------- 🍩 Obesity Dashboard -------------------
if page == "🍩 Obesity Dashboard":
    st.header("Obesity Insights")
    st.markdown("---")
    
    year_filter = st.slider("Select Year", 2012, 2022, 2022)
    top_regions = df_obese[df_obese["Year"] == year_filter].groupby("Region")["Value"].mean().sort_values(ascending=False).head(5)
    st.write(f"### 🔝 Top 5 Regions by Avg Obesity in {year_filter}")
    st.caption("In 2022, regions like the Americas and Europe show the highest average obesity — highlighting the impact of urban diets and sedentary lifestyles.")
    st.bar_chart(top_regions)

    top_countries = df_obese[df_obese["Year"] == year_filter].groupby("Country")["Value"].mean().sort_values(ascending=False).head(5)
    st.write(f"### 🌍 Top 5 Countries with Highest Obesity in {year_filter}")
    st.caption("Countries such as Nauru, Cook Islands, and Palau top the obesity list — these small island nations face rising health challenges.")
    st.bar_chart(top_countries)

    india_trend = df_obese[df_obese["Country"] == "India"].groupby("Year")["Value"].mean()
    st.write("### 📈 Obesity Trend in India")
    st.caption("India shows a steady upward trend in obesity since 2012 — a sign of changing lifestyles, urban diets, and economic growth.")
    st.line_chart(india_trend)

    st.write("### ⚧️ Average Obesity by Gender")
    gender_avg = df_obese.groupby("Gender")["Value"].mean().sort_values(ascending=False)
    st.caption("Males and females have close obesity averages globally, but patterns differ regionally — gender disparity is context-dependent.")
    st.bar_chart(gender_avg)

    st.write("### 🔢 Country Count by Obesity Level and Age Group")
    level_age = df_obese.groupby(["Obesity_Level", "Age"])["Country"].nunique().unstack().fillna(0)
    st.caption("High obesity is more common among adults, while children fall under moderate or low — emphasizing long-term risk accumulation.")
    st.dataframe(level_age)

    st.write("### 🧍‍♂️ Average Obesity by Age Group")
    age_avg = df_obese.groupby("Age")["Value"].mean()
    st.caption("Adults show much higher average obesity than children — age brings higher risk as habits accumulate.")
    st.bar_chart(age_avg)

    st.write("### 📏 CI Width Extremes (Data Consistency)")
    ci_avg = df_obese.groupby("Country")["CI_Width"].mean()
    st.caption("Wider CI values reflect less reliable data — often from small countries or inconsistent surveys. Narrow CI indicates trustable stats.")
    st.write("#### 🔺 Top 5 Least Reliable Countries")
    st.caption("These countries have the widest confidence intervals, meaning their data varies more — possibly due to small sample sizes.")
    st.dataframe(ci_avg.sort_values(ascending=False).head(5))

    st.write("#### 🔻 Top 5 Most Reliable Countries")
    st.caption("Countries with smallest CI widths — like Chile and the USA — offer stable, highly consistent obesity estimates.")
    st.dataframe(ci_avg.sort_values().head(5))

    st.write("### 🧊 Consistently Low Obesity Countries")
    low_obesity = df_obese.groupby("Country").agg({"Value":"mean", "CI_Width":"mean"})
    low_obesity = low_obesity[(low_obesity["Value"] < 10) & (low_obesity["CI_Width"] < 2)]
    st.caption("Countries like Ethiopia, Bangladesh, and India maintain low obesity with low CI — signs of traditional diets and higher activity.")
    st.dataframe(low_obesity.sort_values(by="Value").head(10))

    st.write("### 👩‍🦱 Female > Male Obesity Gap")
    female = df_obese[df_obese["Gender"] == "Female"]
    male = df_obese[df_obese["Gender"] == "Male"]
    merged = pd.merge(female, male, on=["Country", "Year"], suffixes=("_f", "_m"))
    gap = merged[merged["Value_f"] - merged["Value_m"] > 5]
    st.caption("In some countries, female obesity significantly exceeds male — a reflection of cultural, dietary, and mobility differences.")
    st.dataframe(gap[["Country", "Year", "Value_f", "Value_m"]].drop_duplicates().head(10))

    st.write("### 🌍 Global Average Obesity Over Time")
    global_trend = df_obese.groupby("Year")["Value"].mean()
    st.caption("Global obesity has steadily risen from 2012 to 2022 — signaling a universal shift in lifestyle and food systems.")
    st.line_chart(global_trend)

# ------------------- 🍵 Malnutrition Dashboard -------------------
elif page == "🍵 Malnutrition Dashboard":
    st.header("Malnutrition Insights")
    st.markdown("---")
# Q1
    st.write("### 📊 Avg Malnutrition by Age Group")
    age_avg_mal = df_mal.groupby("Age")["Value"].mean()
    st.caption("Children show consistently higher malnutrition levels than adults — a critical concern for early development.")
    st.bar_chart(age_avg_mal)
# Q2
    st.write("### 🌍 Top 5 Countries with Highest Malnutrition")
    top_countries_mal = df_mal[df_mal["Year"] == 2022].groupby("Country")["Value"].mean().sort_values(ascending=False).head(5)
    st.caption("Highlights countries with the most severe malnutrition in 2022 — often tied to poverty or conflict.")
    st.bar_chart(top_countries_mal)
# Q3
    st.write("### 🌍 Malnutrition Trend in Africa")
    africa_trend = df_mal[df_mal["Region"] == "Africa"].groupby("Year")["Value"].mean()
    st.caption("Africa’s malnutrition trend shows slow improvement — with regional disparities across countries.")
    st.line_chart(africa_trend)
# Q4
    st.write("### ⚧️ Average Malnutrition by Gender")
    gender_avg_mal = df_mal.groupby("Gender")["Value"].mean()
    st.caption("Malnutrition differences between genders can reflect food access inequality or cultural bias.")
    st.bar_chart(gender_avg_mal)
# Q5
    st.write("### 📏 Avg CI Width by Malnutrition Level & Age")
    ci_by_level_age = df_mal.groupby(["Malnutrition_Level", "Age"])["CI_Width"].mean().unstack()
    st.caption("Higher CI widths mean less precise estimates. This helps flag where confidence is lower.")
    st.dataframe(ci_by_level_age)
# Q6
    st.write("### 🌎 Yearly Malnutrition Trend: India, Nigeria, Brazil")
    countries = ["India", "Nigeria", "Brazil"]
    for country in countries:
        trend = df_mal[df_mal["Country"] == country].groupby("Year")["Value"].mean()
        st.caption(f"{country}'s malnutrition trend across years. A useful health progress signal.")
        st.line_chart(trend, use_container_width=True)
# Q7
    st.write("### 🌍 Regions with Lowest Average Malnutrition")
    low_region = df_mal.groupby("Region")["Value"].mean().sort_values().head(5)
    st.caption("Regions with lowest average malnutrition. Typically benefit from stronger food systems and income.")
    st.bar_chart(low_region)
# Q8
    st.write("### 📈 Countries with Increasing Malnutrition")
    mal_trend = df_mal.groupby(["Country"])["Value"].agg(["min", "max"])
    inc_mal = mal_trend[mal_trend["max"] - mal_trend["min"] > 0].sort_values(by="max", ascending=False)
    st.caption("Flags countries where malnutrition increased over time — highlights deteriorating health conditions.")
    st.dataframe(inc_mal.head(10))
# Q9
    st.write("### 📊 Min vs Max Malnutrition Year-wise")
    yearwise = df_mal.groupby("Year")["Value"].agg(["min", "max"])
    st.caption("Shows disparity in lowest vs highest malnutrition levels each year.")
    st.line_chart(yearwise)
# Q10
    st.write("### 🚨 Countries with High CI Width (Monitoring)")
    high_ci = df_mal[df_mal["CI_Width"] > 5][["Country", "Year", "CI_Width"]]
    st.caption("Countries where CI width exceeds 5 — monitor these due to lower estimate reliability.")
    st.dataframe(high_ci.sort_values(by="CI_Width", ascending=False).head(10))

# ------------------- 🔗 Combined Insights -------------------
elif page == "🔗 Combined Insights":
    st.header("Combined Obesity & Malnutrition Insights")
    st.markdown("---")
# Q1
    st.subheader("🆚 [Q1] Obesity vs Malnutrition Comparison (Top 5 Countries)")
    combined_avg = pd.merge(
        df_obese.groupby("Country")["Value"].mean().reset_index(name="Obesity_Avg"),
        df_mal.groupby("Country")["Value"].mean().reset_index(name="Malnutrition_Avg"),
        on="Country"
    ).sort_values(by="Obesity_Avg", ascending=False).head(5)
    st.caption("Side-by-side comparison of top 5 countries by obesity and malnutrition. Highlights the paradox.")
    st.dataframe(combined_avg)
# Q2
    st.subheader("⚧️ [Q2] Gender-Based Disparity in Obesity vs Malnutrition")
    gender_ob = df_obese.groupby("Gender")["Value"].mean().reset_index(name="Obesity")
    gender_mal = df_mal.groupby("Gender")["Value"].mean().reset_index(name="Malnutrition")
    gender_comparison = pd.merge(gender_ob, gender_mal, on="Gender")
    st.caption("Compares gender averages across obesity and malnutrition. Reveals hidden inequality.")
    st.dataframe(gender_comparison)
# Q3
    st.subheader("🌎 [Q3] Region-wise Comparison: Africa vs America")
    region_ob = df_obese[df_obese["Region"].isin(["Africa", "Americas"])].groupby("Region")["Value"].mean()
    region_mal = df_mal[df_mal["Region"].isin(["Africa", "Americas"])].groupby("Region")["Value"].mean()
    st.caption("Africa has lower obesity but higher malnutrition; Americas show the reverse — a strong paradox in nutrition.")
    st.bar_chart(pd.concat([region_ob.rename("Obesity"), region_mal.rename("Malnutrition")], axis=1))
# Q4
    st.subheader("📉 [Q4] Countries with Obesity ↑ and Malnutrition ↓")
    trend_ob = df_obese.groupby("Country")["Value"].agg(["min", "max"])
    trend_mal = df_mal.groupby("Country")["Value"].agg(["min", "max"])
    compare = pd.merge(trend_ob, trend_mal, on="Country", suffixes=("_ob", "_mal"))
    improved = compare[(compare["max_ob"] - compare["min_ob"] > 0) & (compare["min_mal"] - compare["max_mal"] > 0)]
    st.caption("Countries where obesity is rising but malnutrition is falling — double-edged shifts.")
    st.dataframe(improved.head(10))
# Q5
    st.subheader("📊 [Q5] Age-Wise Trend Comparison")
    age_ob = df_obese.groupby("Age")["Value"].mean()
    age_mal = df_mal.groupby("Age")["Value"].mean()
    st.caption("Compares how adults vs children are affected by both malnutrition and obesity.")
    st.bar_chart(pd.concat([age_ob.rename("Obesity"), age_mal.rename("Malnutrition")], axis=1))
