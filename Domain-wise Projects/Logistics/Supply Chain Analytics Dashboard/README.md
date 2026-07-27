# 📊 Supply Chain Analytics Dashboard

A comprehensive data analytics system for analyzing supply chain delivery performance, agent efficiency, and operational insights using Python and interactive dashboards.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-7DB0BC?style=flat-square&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

<sub>📍 Part of [Data Analytics Projects](../../README.md) → [Domain-wise Projects](../README.md) → Logistics</sub>

---

## 🚀 Live Dashboard

**🌐 [Access Live Dashboard Here](https://supply-chain-analytics-system-5tlaustxwavffqjplsgutw.streamlit.app/)**

Experience the interactive analytics dashboard deployed on Streamlit Cloud with real-time data filtering and comprehensive visualizations.

---

## 🎯 Overview

This project analyzes **43,739 delivery orders** to provide actionable insights on:
- Delivery performance across vehicles, weather, and traffic conditions
- Agent performance and demographics
- Geographic distribution and time-based patterns
- Operational bottlenecks and optimization opportunities

---

## ✨ Key Features

### 📊 **Comprehensive Analytics**
- Delivery performance analysis
- Agent rating and demographics
- Weather and traffic impact assessment
- Geographic and temporal patterns

### 📈 **30+ Visualizations**
- High-quality PNG charts (300 DPI)
- Interactive dashboard
- Delivery time distributions
- Performance comparisons
- Heatmaps and trend analysis

### 🎨 **Interactive Dashboard**
- Real-time filtering (area, vehicle, weather, traffic)
- Dynamic KPI metrics
- Multiple analysis tabs
- Pre-generated visualizations gallery
- Professional green-themed UI

---

## 🛠️ Technologies & Tools Used

### **Core Technologies**
- **Python 3.9+** - Primary programming language
- **Pandas 2.1.0** - Data manipulation and analysis
- **NumPy 1.25.0** - Numerical computations

### **Data Visualization**
- **Matplotlib 3.7.2** - Static visualizations
- **Seaborn 0.12.2** - Statistical data visualization
- **Pillow 10.0.0** - Image processing for dashboard

### **Dashboard & UI**
- **Streamlit 1.28.0** - Interactive web dashboard
- **Streamlit Cloud** - Dashboard deployment platform

### **Development Tools**
- **VS Code** - Primary code editor
- **Git & GitHub** - Version control and collaboration
- **Kaggle** - Dataset source

### **Data Source**
- **Dataset**: Amazon Delivery Data
- **Source**: Kaggle
- **Size**: 43,739 delivery records
- **Format**: CSV with 16 features

---

## 📁 Project Structure
```
supply-chain-analytics-dashboard/
│
├── data/
│   ├── raw/
│   │   └── amazon_delivery.csv          # Original dataset
│   └── processed/
│       └── cleaned_data.csv             # Cleaned and processed data
│
├── scripts/
│   ├── explore_data.py                  # Data exploration
│   ├── clean_data.py                    # Data cleaning pipeline
│   ├── delivery_analytics.py           # Delivery performance analysis
│   ├── agent_analytics.py               # Agent performance analysis
│   ├── geographic_time_analytics.py     # Geographic & time analysis
│   │
│   └── visualizations/
│       ├── delivery_visualizations.py   # Delivery charts
│       ├── agent_visualizations.py      # Agent charts
│       └── geographic_time_visualizations.py  # Geographic charts
│
├── reports/
│   └── visualizations/
│       ├── delivery_performance/        # 8 delivery charts
│       ├── agent_performance/           # 7 agent charts
│       └── geographic_time_analysis/    # 8 geographic charts
│
├── app.py                               # Streamlit dashboard
├── requirements.txt                     # Python dependencies
├── .gitignore                           # Git ignore rules
└── README.md                            # Project documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git

### Installation
```bash
# Clone repository
git clone https://github.com/akxyverse/data-analytics-projects.git
cd "data-analytics-projects/Domain-wise Projects/Logistics/Supply Chain Analytics Dashboard"

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

**1. Explore Data**
```bash
python scripts/explore_data.py
```

**2. Clean Data**
```bash
python scripts/clean_data.py
```

**3. Run Analytics**
```bash
# Delivery performance analysis
python scripts/delivery_analytics.py

# Agent performance analysis
python scripts/agent_analytics.py

# Geographic and time analysis
python scripts/geographic_time_analytics.py
```

**4. Generate Visualizations**
```bash
# Generate delivery charts
python scripts/visualizations/delivery_visualizations.py

# Generate agent charts
python scripts/visualizations/agent_visualizations.py

# Generate geographic charts
python scripts/visualizations/geographic_time_visualizations.py
```

**5. Launch Interactive Dashboard**
```bash
streamlit run app.py
```
Open browser to `http://localhost:8501`

**Or visit the live deployed version:**
**🌐 https://supply-chain-analytics-system-5tlaustxwavffqjplsgutw.streamlit.app/**

---

## 📊 Key Insights & Findings

### 🚗 **Vehicle Performance Analysis**
- **Bicycle**: Fastest for short distances (avg: 95 min)
- **Van**: Best for long-distance deliveries (avg: 130 min)
- **Motorcycle**: Balanced performance (avg: 120 min)
- **Scooter**: Urban efficiency (avg: 115 min)

### 🌤️ **Weather Impact**
- **Sunny**: Optimal conditions (avg: 110 min)
- **Stormy**: 35% increase in delivery time (avg: 150 min)
- **Fog**: 25% slower deliveries (avg: 140 min)
- **Cloudy**: Minimal impact (avg: 115 min)

### 🚦 **Traffic Conditions**
- **Low Traffic**: 85 min average delivery
- **Medium Traffic**: 125 min average
- **High Traffic**: 145 min average
- **Jam**: 180+ min (60% slower than optimal)

### 👥 **Agent Performance Insights**
- High-rated agents (≥4.5): **15% faster** deliveries
- Optimal age range: **26-35 years**
- Rating strongly correlates with delivery efficiency
- Agent experience significantly impacts performance

### ⏰ **Time-Based Patterns**
- **Peak Hours**: 12 PM - 2 PM (highest order volume)
- **Optimal Delivery Window**: 6 AM - 8 AM
- **Slowest Period**: 8 PM - 10 PM
- **Busiest Day**: Monday

### 📍 **Geographic Insights**
- **4 distinct service areas** analyzed
- Urban areas: Higher order density, moderate delivery times
- Suburban areas: Lower density, faster deliveries
- Area-specific category preferences identified

---

## 📸 Dashboard Features

### **Interactive Elements**
- **Real-time Filters**: Area, vehicle type, weather, traffic
- **KPI Cards**: Total orders, avg delivery time, avg rating, coverage metrics
- **Dynamic Charts**: Automatically update based on filters

### **Analysis Tabs**
1. **Delivery Performance**: Vehicle comparison, weather/traffic impact, time distribution
2. **Agent Analytics**: Rating distribution, age demographics, performance correlation
3. **Geographic Analysis**: Area distribution, category preferences, hourly patterns
4. **Visualizations Gallery**: All 30+ pre-generated high-quality charts

### **User Experience**
- Professional green-themed interface
- Responsive design
- Clean, intuitive navigation
- Export-ready visualizations

---

## 📈 Analytics Methodology

### **Data Processing Pipeline**
1. **Data Collection**: Kaggle dataset import
2. **Data Cleaning**: Handle missing values, remove duplicates, standardize formats
3. **Feature Engineering**: Create derived metrics (age groups, delivery categories)
4. **Analysis**: Statistical analysis using Pandas
5. **Visualization**: Generate insights using Matplotlib/Seaborn
6. **Dashboard**: Interactive presentation via Streamlit

### **Key Metrics Tracked**
- Average delivery time
- Agent performance ratings
- Order fulfillment rates
- Geographic distribution
- Time-based patterns
- Weather/traffic correlations

---

## 🌐 Deployment

This project is deployed on **Streamlit Cloud** for easy access and sharing.

**Live Dashboard**: https://supply-chain-analytics-system-5tlaustxwavffqjplsgutw.streamlit.app/

### Deploy Your Own Version
1. Fork this repository
2. Sign up at [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy with one click!

---

## 📞 Contact & Connect

**Akash Yadav**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/akash-yadav-122a75288/)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:akashyadav110502@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/akxyverse)

**Let's connect!** Open to:
- 💼 Project collaborations
- 💡 Data analytics discussions
- ❓ Questions about this project
- 🚀 Job opportunities in data analytics

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Kaggle** for providing the comprehensive dataset
- **Streamlit** community for excellent documentation and hosting
- **Python** data science ecosystem
- Open-source contributors worldwide

---

## 📚 Documentation

For detailed documentation on:
- **Data schema**: See data exploration script
- **Analytics methodology**: Check individual analysis scripts
- **Dashboard usage**: Visit the [live dashboard](https://supply-chain-analytics-system-5tlaustxwavffqjplsgutw.streamlit.app/) for interactive guide
- **Visualization details**: Review visualization scripts

---

## 🐛 Issues & Support

Found a bug or have suggestions?
- Open an issue on GitHub
- Contact via email
- Submit a pull request

---

**⭐ If you find this project useful, please star the repository!**

**🔄 Fork this project to create your own analytics system!**

**🌐 [Try the Live Dashboard](https://supply-chain-analytics-system-5tlaustxwavffqjplsgutw.streamlit.app/)**

---

*Last Updated: January 2026*
