# 🌦️ Weather Trends Analyzer - Web App

A modern, interactive web application built with Streamlit that analyzes and visualizes 5-day weather forecast data. Get instant weather insights with a beautiful, user-friendly interface.

## ✨ Features

- **🌐 Web-Based Interface**: No command line needed - runs in your browser
- **📈 Interactive Charts**: Beautiful matplotlib visualizations embedded in the app
- **⚡ Real-Time Data**: Fetches live 5-day weather forecasts from OpenWeatherMap
- **📊 Statistical Analysis**: Displays average, maximum, and minimum temperatures
- **📱 Responsive Design**: Works on desktop, tablet, and mobile devices
- **💾 Data Export**: Automatically saves forecast data to CSV files
- **🎯 User-Friendly**: Clean, intuitive interface with instant feedback

## 📋 Requirements

- Python 3.7+
- OpenWeatherMap API key (free registration required)

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/streamlit-weather-app.git
   cd streamlit-weather-app
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv weather_env
   source weather_env/bin/activate  # On Windows: weather_env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your API key:**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key
   - Replace `"your_api_key_here"` in the script with your actual key

5. **Run the app:**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser:**
   - The app will automatically open at `http://localhost:8501`
   - If not, click the link shown in your terminal

## 🎯 How to Use

1. **Enter a city name** in the text input field (e.g., "Cairo", "London", "Tokyo")
2. **Click "Analyze Weather"** button
3. **View results instantly:**
   - Temperature statistics displayed as colorful metrics
   - Interactive 5-day forecast chart
   - Data automatically saved to CSV

## 📊 What You'll See

### 🌡️ Temperature Metrics
- **Average Temperature**: Mean temperature over 5 days
- **Maximum Temperature**: Highest forecasted temperature
- **Minimum Temperature**: Lowest forecasted temperature

### 📈 Forecast Chart
- **3-hour intervals**: Detailed temperature progression
- **5-day span**: Complete workweek weather outlook
- **Interactive plot**: Hover for exact values

## 🗂️ Project Structure

```
streamlit-weather-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── weather-*.csv         # Generated forecast data files
```

## 🔧 Configuration

### API Key Setup
Edit the API_KEY variable in `app.py`:
```python
API_KEY = "your_actual_openweather_api_key_here"
```

### App Customization
You can modify the app appearance by editing:
- **Page title**: `st.set_page_config(page_title="Your Title")`
- **Default city**: `value="YourCity"` in the text input
- **Chart styling**: Matplotlib parameters in the plotting section

## 🛠️ Dependencies

```txt
streamlit          # Web app framework
requests          # HTTP requests for API calls
pandas           # Data manipulation
dask[complete]   # Distributed computing
matplotlib       # Data visualization
```

## 🌍 Supported Cities

Enter any city name supported by OpenWeatherMap:
- **Major cities**: "New York", "London", "Tokyo", "Cairo"
- **With country**: "Paris,FR" or "London,UK" for specificity
- **International**: Works worldwide with local weather data

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud (Free)
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Your app will be live at `yourapp.streamlit.app`


## ⚠️ Troubleshooting

### Common Issues:

1. **"API Error: Invalid API key"**
   ```
   ❌ Solution: Verify your OpenWeatherMap API key is correct and active
   ```

2. **"City not found"**
   ```
   ❌ Try: Use exact city names or add country code (e.g., "London,UK")
   ```

3. **App won't start**
   ```bash
   # Reinstall Streamlit
   pip uninstall streamlit
   pip install streamlit
   ```

4. **Charts not displaying**
   ```
   ❌ Check: Matplotlib backend issues - restart the app
   ```

## 🔐 Security Best Practices

### Environment Variables (Recommended)
Instead of hardcoding your API key:

1. **Create `.env` file:**
   ```
   OPENWEATHER_API_KEY=your_actual_key_here
   ```

2. **Install python-dotenv:**
   ```bash
   pip install python-dotenv
   ```

3. **Update your code:**
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   API_KEY = os.getenv('OPENWEATHER_API_KEY')
   ```

4. **Add to `.gitignore`:**
   ```
   .env
   ```

## 📈 Example Screenshots

![Alt text](Screenshot%20(137).png)
![Screenshot 138](Screenshot%20(138).png)
![Screenshot 140](Screenshot%20(140).png)
![Screenshot 142](Screenshot%20(142).png)
![Screenshot 143](Screenshot%20(143).png)













---

