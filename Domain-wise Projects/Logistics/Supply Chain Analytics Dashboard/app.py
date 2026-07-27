import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Supply Chain Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Green Theme and Better Design
st.markdown("""
    <style>
    /* Main background */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: transparent;
    }
    
    /* Title styling */
    h1 {
        color: #ffffff !important;
        text-align: center;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        padding: 20px 0;
    }
    
    h2, h3 {
        color: #ffffff !important;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: bold;
        color: #10b981 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
        font-size: 16px;
    }
    
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
    }
    
    /* Selectbox styling */
    .stSelectbox > label {
        color: white !important;
        font-weight: 600;
    }
    
    /* Info box */
    .stAlert {
        background: rgba(16, 185, 129, 0.2);
        border: 1px solid #10b981;
        border-radius: 10px;
        color: white;
    }
    
    /* Divider */
    hr {
        border-color: rgba(255, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Title with icon
st.markdown("""
    <h1>
        📊 Supply Chain Analytics Dashboard
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('DATA/processed/cleaned_data.csv')
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    return df

try:
    df = load_data()
    
    # Sidebar filters
    st.sidebar.markdown("### 🔍 Filters")
    st.sidebar.markdown("")
    
    # Area filter
    areas = ['All'] + sorted(list(df['Area'].unique()))
    selected_area = st.sidebar.selectbox("📍 Select Area", areas)
    
    # Vehicle filter
    vehicles = ['All'] + sorted(list(df['Vehicle'].unique()))
    selected_vehicle = st.sidebar.selectbox("🚗 Select Vehicle", vehicles)
    
    # Weather filter
    weather_conditions = ['All'] + sorted(list(df['Weather'].unique()))
    selected_weather = st.sidebar.selectbox("🌤️ Select Weather", weather_conditions)
    
    # Traffic filter
    traffic_conditions = ['All'] + sorted(list(df['Traffic'].unique()))
    selected_traffic = st.sidebar.selectbox("🚦 Select Traffic", traffic_conditions)
    
    # Apply filters
    filtered_df = df.copy()
    if selected_area != 'All':
        filtered_df = filtered_df[filtered_df['Area'] == selected_area]
    if selected_vehicle != 'All':
        filtered_df = filtered_df[filtered_df['Vehicle'] == selected_vehicle]
    if selected_weather != 'All':
        filtered_df = filtered_df[filtered_df['Weather'] == selected_weather]
    if selected_traffic != 'All':
        filtered_df = filtered_df[filtered_df['Traffic'] == selected_traffic]
    
    # KPI Metrics Row
    st.markdown("### 📈 Key Performance Indicators")
    st.markdown("")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="📦 Total Orders",
            value=f"{len(filtered_df):,}",
            delta=None
        )
    
    with col2:
        avg_delivery = filtered_df['Delivery_Time'].mean()
        st.metric(
            label="⏱️ Avg Delivery",
            value=f"{avg_delivery:.1f} min",
            delta=None
        )
    
    with col3:
        avg_rating = filtered_df['Agent_Rating'].mean()
        st.metric(
            label="⭐ Avg Rating",
            value=f"{avg_rating:.2f}",
            delta=None
        )
    
    with col4:
        total_areas = filtered_df['Area'].nunique()
        st.metric(
            label="🗺️ Areas",
            value=total_areas,
            delta=None
        )
    
    with col5:
        total_categories = filtered_df['Category'].nunique()
        st.metric(
            label="📋 Categories",
            value=total_categories,
            delta=None
        )
    
    st.markdown("---")
    
    # Set green color palette for charts
    green_palette = ['#10b981', '#059669', '#047857', '#065f46', '#064e3b']
    sns.set_palette(green_palette)
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📦 Delivery Performance", 
        "👥 Agent Analytics", 
        "🗺️ Geographic Analysis", 
        "📊 All Visualizations"
    ])
    
    # Tab 1: Delivery Performance
    with tab1:
        st.markdown("## Delivery Performance Analysis")
        st.markdown("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🚗 Delivery Time by Vehicle")
            vehicle_avg = filtered_df.groupby('Vehicle')['Delivery_Time'].mean().sort_values()
            
            fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
            ax.set_facecolor('none')
            bars = ax.barh(vehicle_avg.index, vehicle_avg.values, color='#10b981', edgecolor='white', linewidth=2)
            ax.set_xlabel('Average Delivery Time (min)', fontsize=12, color='white', fontweight='bold')
            ax.set_ylabel('Vehicle Type', fontsize=12, color='white', fontweight='bold')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            for bar in bars:
                width = bar.get_width()
                ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                       f'{width:.1f}', ha='left', va='center', 
                       color='white', fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        with col2:
            st.markdown("#### 🌤️ Weather Impact on Delivery")
            weather_avg = filtered_df.groupby('Weather')['Delivery_Time'].mean().sort_values(ascending=False)
            
            fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
            ax.set_facecolor('none')
            bars = ax.bar(weather_avg.index, weather_avg.values, color='#10b981', edgecolor='white', linewidth=2)
            ax.set_xlabel('Weather Condition', fontsize=12, color='white', fontweight='bold')
            ax.set_ylabel('Average Delivery Time (min)', fontsize=12, color='white', fontweight='bold')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.xticks(rotation=45, ha='right')
            
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, height + 1,
                       f'{height:.1f}', ha='center', va='bottom',
                       color='white', fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        st.markdown("")
        st.markdown("#### 📊 Delivery Time Distribution")
        
        fig, ax = plt.subplots(figsize=(14, 6), facecolor='none')
        ax.set_facecolor('none')
        ax.hist(filtered_df['Delivery_Time'], bins=30, color='#10b981', alpha=0.8, edgecolor='white', linewidth=1.5)
        ax.set_xlabel('Delivery Time (minutes)', fontsize=12, color='white', fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=12, color='white', fontweight='bold')
        ax.tick_params(colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        mean_val = filtered_df['Delivery_Time'].mean()
        ax.axvline(mean_val, color='#ef4444', linestyle='--', linewidth=2,
                  label=f'Mean: {mean_val:.1f} min')
        ax.legend(facecolor='none', edgecolor='white', labelcolor='white', fontsize=11)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        # Additional metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            fastest = filtered_df['Delivery_Time'].min()
            st.metric("⚡ Fastest Delivery", f"{fastest} min")
        with col2:
            slowest = filtered_df['Delivery_Time'].max()
            st.metric("🐌 Slowest Delivery", f"{slowest} min")
        with col3:
            median = filtered_df['Delivery_Time'].median()
            st.metric("📊 Median Time", f"{median:.0f} min")
    
    # Tab 2: Agent Analytics
    with tab2:
        st.markdown("## Agent Performance Analysis")
        st.markdown("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### ⭐ Agent Rating Distribution")
            fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
            ax.set_facecolor('none')
            ax.hist(filtered_df['Agent_Rating'], bins=20, color='#10b981', alpha=0.8, edgecolor='white', linewidth=1.5)
            ax.set_xlabel('Agent Rating', fontsize=12, color='white', fontweight='bold')
            ax.set_ylabel('Frequency', fontsize=12, color='white', fontweight='bold')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            mean_rating = filtered_df['Agent_Rating'].mean()
            ax.axvline(mean_rating, color='#ef4444', linestyle='--', linewidth=2,
                      label=f'Mean: {mean_rating:.2f}')
            ax.legend(facecolor='none', edgecolor='white', labelcolor='white', fontsize=11)
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        with col2:
            st.markdown("#### 👤 Agent Age Distribution")
            fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
            ax.set_facecolor('none')
            ax.hist(filtered_df['Agent_Age'], bins=20, color='#10b981', alpha=0.8, edgecolor='white', linewidth=1.5)
            ax.set_xlabel('Agent Age (years)', fontsize=12, color='white', fontweight='bold')
            ax.set_ylabel('Frequency', fontsize=12, color='white', fontweight='bold')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            mean_age = filtered_df['Agent_Age'].mean()
            ax.axvline(mean_age, color='#ef4444', linestyle='--', linewidth=2,
                      label=f'Mean: {mean_age:.1f}')
            ax.legend(facecolor='none', edgecolor='white', labelcolor='white', fontsize=11)
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        st.markdown("")
        st.markdown("#### 📈 Rating vs Delivery Performance")
        
        rating_delivery = filtered_df.groupby('Agent_Rating')['Delivery_Time'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(14, 6), facecolor='none')
        ax.set_facecolor('none')
        ax.plot(rating_delivery['Agent_Rating'], rating_delivery['Delivery_Time'], 
                marker='o', linewidth=3, markersize=10, color='#10b981', 
                markeredgecolor='white', markeredgewidth=2)
        ax.set_xlabel('Agent Rating', fontsize=12, color='white', fontweight='bold')
        ax.set_ylabel('Average Delivery Time (min)', fontsize=12, color='white', fontweight='bold')
        ax.tick_params(colors='white')
        ax.grid(True, alpha=0.2, color='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        # Agent performance metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            high_rated = len(filtered_df[filtered_df['Agent_Rating'] >= 4.5])
            st.metric("🌟 High Rated Agents", f"{high_rated:,}")
        with col2:
            avg_age = filtered_df['Agent_Age'].mean()
            st.metric("👤 Average Age", f"{avg_age:.1f} years")
        with col3:
            low_rated = len(filtered_df[filtered_df['Agent_Rating'] < 4.0])
            st.metric("⚠️ Low Rated Agents", f"{low_rated:,}")
    
    # Tab 3: Geographic Analysis
    with tab3:
        st.markdown("## Geographic & Time Analysis")
        st.markdown("")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📍 Orders by Area")
            area_counts = filtered_df['Area'].value_counts()
            
            fig, ax = plt.subplots(figsize=(10, 10), facecolor='none')
            ax.set_facecolor('none')
            colors = ['#10b981', '#059669', '#047857', '#065f46']
            wedges, texts, autotexts = ax.pie(area_counts.values, labels=area_counts.index, 
                   autopct='%1.1f%%', startangle=90, colors=colors,
                   textprops={'color': 'white', 'fontweight': 'bold', 'fontsize': 12},
                   wedgeprops={'edgecolor': 'white', 'linewidth': 2})
            
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        with col2:
            st.markdown("#### 📦 Top 10 Categories")
            category_counts = filtered_df['Category'].value_counts().head(10)
            
            fig, ax = plt.subplots(figsize=(10, 10), facecolor='none')
            ax.set_facecolor('none')
            bars = ax.barh(category_counts.index, category_counts.values, color='#10b981', 
                          edgecolor='white', linewidth=2)
            ax.set_xlabel('Number of Orders', fontsize=12, color='white', fontweight='bold')
            ax.set_ylabel('Category', fontsize=12, color='white', fontweight='bold')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            for bar in bars:
                width = bar.get_width()
                ax.text(width + 20, bar.get_y() + bar.get_height()/2, 
                       f'{int(width)}', ha='left', va='center',
                       color='white', fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        
        st.markdown("")
        st.markdown("#### ⏰ Hourly Order Pattern")
        
        hourly_orders = filtered_df.groupby('Order_Hour')['Order_ID'].count()
        fig, ax = plt.subplots(figsize=(14, 6), facecolor='none')
        ax.set_facecolor('none')
        ax.plot(hourly_orders.index, hourly_orders.values, marker='o', 
                linewidth=3, markersize=10, color='#10b981',
                markeredgecolor='white', markeredgewidth=2)
        ax.fill_between(hourly_orders.index, hourly_orders.values, alpha=0.3, color='#10b981')
        ax.set_xlabel('Hour of Day', fontsize=12, color='white', fontweight='bold')
        ax.set_ylabel('Number of Orders', fontsize=12, color='white', fontweight='bold')
        ax.tick_params(colors='white')
        ax.grid(True, alpha=0.2, color='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()
        
        # Geographic metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            busiest_area = area_counts.idxmax()
            st.metric("🏆 Busiest Area", busiest_area)
        with col2:
            peak_hour = hourly_orders.idxmax()
            st.metric("⏰ Peak Hour", f"{peak_hour}:00")
        with col3:
            top_category = filtered_df['Category'].value_counts().idxmax()
            st.metric("📦 Top Category", top_category)
    
    # Tab 4: All Visualizations
    with tab4:
        st.markdown("## 📊 Pre-Generated Visualizations")
        st.markdown("View all detailed analysis charts created during the analytics phase")
        st.markdown("")
        
        # Create three columns for categories
        viz_tab1, viz_tab2, viz_tab3 = st.tabs([
            "📦 Delivery Performance",
            "👥 Agent Performance", 
            "🗺️ Geographic Analysis"
        ])
        
        with viz_tab1:
            delivery_path = 'reports/visualizations/delivery_performance'
            if os.path.exists(delivery_path):
                delivery_files = sorted([f for f in os.listdir(delivery_path) if f.endswith('.png')])
                
                for i in range(0, len(delivery_files), 2):
                    cols = st.columns(2)
                    for j, col in enumerate(cols):
                        if i + j < len(delivery_files):
                            img_file = delivery_files[i + j]
                            with col:
                                img = Image.open(os.path.join(delivery_path, img_file))
                                st.image(img, use_container_width=True)
                                st.caption(img_file.replace('_', ' ').replace('.png', '').title())
            else:
                st.warning("⚠️ Delivery performance visualizations not found!")
        
        with viz_tab2:
            agent_path = 'reports/visualizations/agent_performance'
            if os.path.exists(agent_path):
                agent_files = sorted([f for f in os.listdir(agent_path) if f.endswith('.png')])
                
                for i in range(0, len(agent_files), 2):
                    cols = st.columns(2)
                    for j, col in enumerate(cols):
                        if i + j < len(agent_files):
                            img_file = agent_files[i + j]
                            with col:
                                img = Image.open(os.path.join(agent_path, img_file))
                                st.image(img, use_container_width=True)
                                st.caption(img_file.replace('_', ' ').replace('.png', '').title())
            else:
                st.warning("⚠️ Agent performance visualizations not found!")
        
        with viz_tab3:
            geo_path = 'reports/visualizations/geographic_time_analysis'
            if os.path.exists(geo_path):
                geo_files = sorted([f for f in os.listdir(geo_path) if f.endswith('.png')])
                
                for i in range(0, len(geo_files), 2):
                    cols = st.columns(2)
                    for j, col in enumerate(cols):
                        if i + j < len(geo_files):
                            img_file = geo_files[i + j]
                            with col:
                                img = Image.open(os.path.join(geo_path, img_file))
                                st.image(img, use_container_width=True)
                                st.caption(img_file.replace('_', ' ').replace('.png', '').title())
            else:
                st.warning("⚠️ Geographic visualizations not found!")
    
    # Footer in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        <div style='text-align: center; color: white;'>
            <h3>📊 Supply Chain Analytics System</h3>
            <p style='font-size: 12px; color: #10b981;'>
                Built with Python, Streamlit,<br>
                Pandas, Matplotlib & Seaborn
            </p>
        </div>
    """, unsafe_allow_html=True)
    
except FileNotFoundError:
    st.error("❌ Data file not found! Please ensure 'data/processed/cleaned_data.csv' exists.")
except Exception as e:
    st.error(f"❌ An error occurred: {str(e)}")
