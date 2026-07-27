import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from supabase import create_client
from datetime import datetime
import pickle

# Page configuration
st.set_page_config(
    page_title="ThunderCast - Storm Prediction Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
/* Main app background */
.stApp {
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.65),
        rgba(0, 0, 0, 0.65)
    ),
    url("https://media.13newsnow.com/assets/WVEC/images/e23dc125-7f4c-4783-8b28-925ec0d61d6f/e23dc125-7f4c-4783-8b28-925ec0d61d6f_750x422.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Make text readable */
h1, h2, h3, h4, h5, h6, p, span, label {
    color: #ffffff !important;
}

/* Metric cards */
[data-testid="metric-container"] {
    background: rgba(0, 0, 0, 0.55);
    border-radius: 12px;
    padding: 12px;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# Supabase connection
SUPABASE_URL = "https://bbiphtlpmlieprivkxba.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJiaXBodGxwbWxpZXByaXZreGJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzAxOTY3OTEsImV4cCI6MjA4NTc3Mjc5MX0.r5-fcB1urDsthv66dZ8h3LRiksr4fe84ScpszkDfLPM"

try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    st.error(f"❌ Database connection failed: {e}")
    st.stop()

# Title
st.markdown('<p class="main-header">⚡ ThunderCast: Smart Storm Prediction Engine</p>', unsafe_allow_html=True)
st.markdown("**Real-time Thunderstorm Prediction System for Pimpri-Chinchwad, Pune**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("📍 Location Settings")
    st.info("**Pimpri-Chinchwad, Pune, India**")
    st.markdown("**Coordinates:**")
    st.text("Latitude: 18.6298°N")
    st.text("Longitude: 73.7997°E")
    
    st.markdown("---")
    st.header("⚙️ System Info")
    st.text("Model: Facebook Prophet")
    st.text("Version: 1.0")
    st.text("Last Updated: " + datetime.now().strftime("%Y-%m-%d"))
    
    st.markdown("---")
    if st.button("🔄 Refresh Data"):
        st.rerun()

# Main content
try:
    # Fetch latest weather data
    weather_response = supabase.table('weather_data').select('*').order('timestamp', desc=True).limit(1).execute()
    
    if not weather_response.data:
        st.warning("⚠️ No weather data available. Please run data_collection.py first!")
        st.stop()
    
    latest = weather_response.data[0]
    
    # === SECTION 1: CURRENT CONDITIONS ===
    st.header("🌤️ Current Weather Conditions")
    st.caption(f"Last updated: {latest['timestamp']}")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="🌡️ Temperature",
            value=f"{latest['temperature']}°C",
            delta=None
        )
    
    with col2:
        st.metric(
            label="💧 Humidity",
            value=f"{latest['humidity']}%",
            delta=None
        )
    
    with col3:
        st.metric(
            label="🎈 Pressure",
            value=f"{latest['pressure']} hPa",
            delta=None
        )
    
    with col4:
        st.metric(
            label="💨 Wind Speed",
            value=f"{latest['wind_speed']} m/s",
            delta=None
        )
    
    with col5:
        st.metric(
            label="☁️ Cloud Cover",
            value=f"{latest['cloud_cover']}%",
            delta=None
        )
    
    st.markdown("---")
    
    # === SECTION 2: THUNDERSTORM PREDICTIONS ===
    st.header("⚡ Thunderstorm Predictions")
    
    predictions_response = supabase.table('predictions').select('*').order('forecast_time', desc=False).limit(24).execute()
    
    if predictions_response.data:
        pred_df = pd.DataFrame(predictions_response.data)
        pred_df['forecast_time'] = pd.to_datetime(pred_df['forecast_time'])
        pred_df = pred_df.sort_values('forecast_time')
        
        # Prediction Chart
        st.subheader("📊 Probability Forecast (Next 24 Hours)")
        
        fig_pred = go.Figure()
        
        fig_pred.add_trace(go.Scatter(
            x=pred_df['forecast_time'],
            y=pred_df['thunderstorm_probability'],
            mode='lines+markers',
            name='Storm Probability',
            line=dict(color='#FF4500', width=3),
            marker=dict(size=8, color='#FF6B6B'),
            fill='tozeroy',
            fillcolor='rgba(255, 69, 0, 0.2)'
        ))
        
        # Add threshold lines
        fig_pred.add_hline(y=70, line_dash="dash", line_color="red", 
                          annotation_text="High Risk (70%)", annotation_position="right")
        fig_pred.add_hline(y=40, line_dash="dash", line_color="orange",
                          annotation_text="Moderate Risk (40%)", annotation_position="right")
        
        fig_pred.update_layout(
            xaxis_title="Time",
            yaxis_title="Thunderstorm Probability (%)",
            hovermode='x unified',
            height=450,
            showlegend=True
        )
        
        st.plotly_chart(fig_pred, use_container_width=True)
        
        # Risk Assessment
        max_prob = pred_df['thunderstorm_probability'].max()
        
        col1, col2 = st.columns(2)
        
        with col1:
            if max_prob > 70:
                st.error(f"🔴 **HIGH RISK**: Maximum probability {max_prob:.1f}%")
            elif max_prob > 40:
                st.warning(f"🟡 **MODERATE RISK**: Maximum probability {max_prob:.1f}%")
            else:
                st.success(f"🟢 **LOW RISK**: Maximum probability {max_prob:.1f}%")
        
        with col2:
            st.info(f"**Next 6 hours average:** {pred_df.head(6)['thunderstorm_probability'].mean():.1f}%")
        
        # Detailed Predictions Table
        st.subheader("📋 Detailed Forecast")
        
        display_df = pred_df.head(12)[['forecast_time', 'thunderstorm_probability']].copy()
        display_df['forecast_time'] = display_df['forecast_time'].dt.strftime('%I:%M %p, %d %b')
        display_df['thunderstorm_probability'] = display_df['thunderstorm_probability'].apply(lambda x: f"{x:.2f}%")
        display_df['risk_level'] = pred_df.head(12)['thunderstorm_probability'].apply(
            lambda x: "🔴 High" if x > 70 else ("🟡 Moderate" if x > 40 else "🟢 Low")
        )
        display_df.columns = ['Time', 'Probability', 'Risk Level']
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    else:
        st.warning("⚠️ No predictions available. Run prediction.py to generate forecasts!")
    
    st.markdown("---")
    
    # === SECTION 3: HISTORICAL TRENDS ===
    st.header("📈 Historical Weather Trends")
    
    # Time range selector
    time_range = st.selectbox(
        "Select time range:",
        ["Last 6 Hours", "Last 12 Hours", "Last 24 Hours", "Last 7 Days"],
        index=2
    )
    
    range_map = {
        "Last 6 Hours": 6,
        "Last 12 Hours": 12,
        "Last 24 Hours": 24,
        "Last 7 Days": 168
    }
    
    limit = range_map[time_range]
    
    history_response = supabase.table('weather_data').select('*').order('timestamp', desc=True).limit(limit).execute()
    
    if history_response.data:
        history_df = pd.DataFrame(history_response.data)
        history_df['timestamp'] = pd.to_datetime(history_df['timestamp'])
        history_df = history_df.sort_values('timestamp')
        
        # Multi-parameter chart
        fig_multi = make_subplots(
            rows=2, cols=2,
            subplot_titles=('🌡️ Temperature', '💧 Humidity', '🎈 Pressure', '💨 Wind Speed'),
            vertical_spacing=0.12,
            horizontal_spacing=0.1
        )
        
        fig_multi.add_trace(
            go.Scatter(x=history_df['timestamp'], y=history_df['temperature'],
                      name='Temperature', line=dict(color='#FF6B6B', width=2)),
            row=1, col=1
        )
        
        fig_multi.add_trace(
            go.Scatter(x=history_df['timestamp'], y=history_df['humidity'],
                      name='Humidity', line=dict(color='#4ECDC4', width=2)),
            row=1, col=2
        )
        
        fig_multi.add_trace(
            go.Scatter(x=history_df['timestamp'], y=history_df['pressure'],
                      name='Pressure', line=dict(color='#45B7D1', width=2)),
            row=2, col=1
        )
        
        fig_multi.add_trace(
            go.Scatter(x=history_df['timestamp'], y=history_df['wind_speed'],
                      name='Wind Speed', line=dict(color='#FFA07A', width=2)),
            row=2, col=2
        )
        
        fig_multi.update_xaxes(title_text="Time", row=2, col=1)
        fig_multi.update_xaxes(title_text="Time", row=2, col=2)
        
        fig_multi.update_yaxes(title_text="°C", row=1, col=1)
        fig_multi.update_yaxes(title_text="%", row=1, col=2)
        fig_multi.update_yaxes(title_text="hPa", row=2, col=1)
        fig_multi.update_yaxes(title_text="m/s", row=2, col=2)
        
        fig_multi.update_layout(height=600, showlegend=False, hovermode='x unified')
        
        st.plotly_chart(fig_multi, use_container_width=True)
        
        # Statistics
        st.subheader("📊 Statistical Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Avg Temperature", f"{history_df['temperature'].mean():.1f}°C")
            st.caption(f"Min: {history_df['temperature'].min():.1f}°C | Max: {history_df['temperature'].max():.1f}°C")
        
        with col2:
            st.metric("Avg Humidity", f"{history_df['humidity'].mean():.1f}%")
            st.caption(f"Min: {history_df['humidity'].min():.0f}% | Max: {history_df['humidity'].max():.0f}%")
        
        with col3:
            st.metric("Avg Pressure", f"{history_df['pressure'].mean():.0f} hPa")
            st.caption(f"Min: {history_df['pressure'].min():.0f} | Max: {history_df['pressure'].max():.0f}")
        
        with col4:
            st.metric("Avg Wind Speed", f"{history_df['wind_speed'].mean():.1f} m/s")
            st.caption(f"Min: {history_df['wind_speed'].min():.1f} | Max: {history_df['wind_speed'].max():.1f}")
    
    else:
        st.info("No historical data available for selected time range.")

except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p><strong>ThunderCast</strong> - Automated Thunderstorm Prediction System</p>
        <p>Built with Facebook Prophet, Python, Plotly & Streamlit | Data Source: OpenWeatherMap API</p>
        <p>© 2026 ThunderCast Project</p>
    </div>
""", unsafe_allow_html=True)

st.image(
    "https://media.13newsnow.com/assets/WVEC/images/e23dc125-7f4c-4783-8b28-925ec0d61d6f/"
    "e23dc125-7f4c-4783-8b28-925ec0d61d6f_750x422.jpg",
    caption="🌩️ Live Thunderstorm Visual",
    use_container_width=True  # ✅ Fixed
)