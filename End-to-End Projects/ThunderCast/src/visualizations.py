import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from supabase import create_client
import os

# Supabase connection
SUPABASE_URL = "https://bbiphtlpmlieprivkxba.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJiaXBodGxwbWxpZXByaXZreGJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzAxOTY3OTEsImV4cCI6MjA4NTc3Mjc5MX0.r5-fcB1urDsthv66dZ8h3LRiksr4fe84ScpszkDfLPM"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("📊 Creating Plotly Visualizations...")

# Create visualizations directory
os.makedirs('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/visualizations', exist_ok=True)

# 1. FETCH DATA
print("\n1️⃣ Fetching data from database...")
weather_response = supabase.table('weather_data').select('*').order('timestamp', desc=True).limit(168).execute()  # Last 7 days
predictions_response = supabase.table('predictions').select('*').order('forecast_time', desc=True).limit(24).execute()

weather_df = pd.DataFrame(weather_response.data)
predictions_df = pd.DataFrame(predictions_response.data)

weather_df['timestamp'] = pd.to_datetime(weather_df['timestamp'])
predictions_df['forecast_time'] = pd.to_datetime(predictions_df['forecast_time'])

print(f"✅ Weather records: {len(weather_df)}")
print(f"✅ Prediction records: {len(predictions_df)}")

# 2. TEMPERATURE TREND
print("\n2️⃣ Creating temperature trend chart...")
fig1 = px.line(weather_df.sort_values('timestamp'), 
               x='timestamp', 
               y='temperature',
               title='Temperature Trend (Last 7 Days)',
               labels={'temperature': 'Temperature (°C)', 'timestamp': 'Date & Time'},
               color_discrete_sequence=['#FF6B6B'])
fig1.update_layout(hovermode='x unified', height=500)
fig1.write_html('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/visualizations/temperature_trend.html')
print("✅ Saved: temperature_trend.html")

# 3. MULTI-PARAMETER CHART
print("\n3️⃣ Creating multi-parameter chart...")
fig2 = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Temperature', 'Humidity', 'Pressure', 'Wind Speed')
)

weather_sorted = weather_df.sort_values('timestamp')

fig2.add_trace(go.Scatter(x=weather_sorted['timestamp'], y=weather_sorted['temperature'], 
                          name='Temperature', line=dict(color='#FF6B6B')), row=1, col=1)
fig2.add_trace(go.Scatter(x=weather_sorted['timestamp'], y=weather_sorted['humidity'], 
                          name='Humidity', line=dict(color='#4ECDC4')), row=1, col=2)
fig2.add_trace(go.Scatter(x=weather_sorted['timestamp'], y=weather_sorted['pressure'], 
                          name='Pressure', line=dict(color='#45B7D1')), row=2, col=1)
fig2.add_trace(go.Scatter(x=weather_sorted['timestamp'], y=weather_sorted['wind_speed'], 
                          name='Wind Speed', line=dict(color='#FFA07A')), row=2, col=2)

fig2.update_layout(height=700, title_text="Weather Parameters Dashboard", showlegend=False)
fig2.write_html('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/visualizations/weather_dashboard.html')
print("✅ Saved: weather_dashboard.html")

# 4. THUNDERSTORM PREDICTIONS
print("\n4️⃣ Creating thunderstorm predictions chart...")
fig3 = go.Figure()

predictions_sorted = predictions_df.sort_values('forecast_time')

fig3.add_trace(go.Scatter(
    x=predictions_sorted['forecast_time'],
    y=predictions_sorted['thunderstorm_probability'],
    mode='lines+markers',
    name='Probability',
    line=dict(color='#8B0000', width=3),
    marker=dict(size=10, color='#FF4500'),
    fill='tozeroy',
    fillcolor='rgba(255, 69, 0, 0.2)'
))

fig3.add_hline(y=70, line_dash="dash", line_color="red", 
               annotation_text="High Risk Threshold (70%)")
fig3.add_hline(y=40, line_dash="dash", line_color="orange",
               annotation_text="Moderate Risk Threshold (40%)")

fig3.update_layout(
    title='Thunderstorm Probability Forecast',
    xaxis_title='Forecast Time',
    yaxis_title='Probability (%)',
    hovermode='x unified',
    height=500
)

fig3.write_html('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/visualizations/thunderstorm_forecast.html')
print("✅ Saved: thunderstorm_forecast.html")

# 5. CURRENT CONDITIONS GAUGE
print("\n5️⃣ Creating current conditions gauge...")
latest = weather_df.sort_values('timestamp', ascending=False).iloc[0]

fig4 = go.Figure()

fig4.add_trace(go.Indicator(
    mode="gauge+number",
    value=latest['humidity'],
    title={'text': "Current Humidity (%)"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "#4ECDC4"},
        'steps': [
            {'range': [0, 30], 'color': "#FFE5E5"},
            {'range': [30, 70], 'color': "#FFF4E5"},
            {'range': [70, 100], 'color': "#E5F4FF"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 70
        }
    }
))

fig4.update_layout(height=400)
fig4.write_html('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/visualizations/humidity_gauge.html')
print("✅ Saved: humidity_gauge.html")

# 6. EXPORT DATA FOR TABLEAU
print("\n6️⃣ Exporting data for Tableau...")
weather_df.to_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/visualizations/weather_data_tableau.csv', index=False)
predictions_df.to_csv('D:/Project-02-ThunderCast Smart Storm Prediction Engine/data/visualizations/predictions_tableau.csv', index=False)
print("✅ Saved: weather_data_tableau.csv")
print("✅ Saved: predictions_tableau.csv")

print("\n" + "="*80)
print("✅ ALL VISUALIZATIONS CREATED!")
print("="*80)
print("\n📁 Files created in: data/visualizations/")
print("  - temperature_trend.html")
print("  - weather_dashboard.html")
print("  - thunderstorm_forecast.html")
print("  - humidity_gauge.html")
print("  - weather_data_tableau.csv (for Tableau)")
print("  - predictions_tableau.csv (for Tableau)")