import streamlit as st
import requests
import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt

# ----------- API Configuration ------------
API_KEY = "your_api_key_here"  # ← Replace with your real OpenWeather key

# ----------- Page Layout ------------
st.set_page_config(page_title="Weather Trends Analyzer", layout="centered")
st.title("🌦️ Weather Trends Analyzer")
st.write("Analyze and visualize 5-day weather forecast data by city.")

# ----------- City Input ------------
city = st.text_input("Enter city name:", value="Cairo")

if st.button("Analyze Weather"):
    with st.spinner("Fetching weather data..."):

        # ---- 1. Fetch weather data from API ----
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if "list" not in data:
            st.error(f"❌ API Error: {data.get('message', 'Unknown error')}")
        else:
            # ---- 2. Save to a temporary DataFrame ----
            records = []
            for entry in data['list']:
                records.append({
                    "Datetime": entry['dt_txt'],
                    "Temperature": entry['main']['temp']
                })

            df = pd.DataFrame(records)
            df.to_csv(f"weather-{city.lower()}.csv", index=False)

            # ---- 3. Load with Dask and Analyze ----
            ddf = dd.read_csv(
                f"weather-{city.lower()}.csv",
                dtype={"Temperature": "float64"},
                assume_missing=True
            )

            avg_temp = ddf["Temperature"].mean().compute()
            max_temp = ddf["Temperature"].max().compute()
            min_temp = ddf["Temperature"].min().compute()

            st.success(f"✅ Data fetched successfully for {city}")

            # ---- 4. Display Stats ----
            st.metric("🌡️ Average Temp (°C)", f"{avg_temp:.2f}")
            st.metric("🔥 Max Temp (°C)", f"{max_temp:.2f}")
            st.metric("❄️ Min Temp (°C)", f"{min_temp:.2f}")

            # ---- 5. Show Plot ----
            st.write("### 📈 Temperature Trend (3-hour intervals)")
            fig, ax = plt.subplots()
            ax.plot(df["Datetime"], df["Temperature"], marker='o', linestyle='-')
            ax.set_xticks(df["Datetime"][::8])  # Show one tick per day
            ax.set_xticklabels(df["Datetime"][::8], rotation=45)
            ax.set_ylabel("Temperature (°C)")
            ax.set_xlabel("Datetime")
            ax.set_title(f"5-Day Temperature Forecast – {city}")
            ax.grid(True)
            st.pyplot(fig)
