# 🎮 Esports & Gaming Revenue Analytics System

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> A comprehensive data analytics project analyzing global gaming and esports revenue trends from 2010 to 2025, uncovering market dynamics, regional performance, and growth patterns using Python, Julius AI, and Tableau.

<sub>📍 Part of [Data Analytics Projects](../../../README.md) → [Domain-wise Projects](../../README.md) → Others</sub>

---

## 📊 Project Overview

This project analyzes **16 years** of gaming and esports data across **25 countries** and **7 regions**, revealing:

- 📈 **17.7% CAGR** in gaming revenue (2010-2025)
- 🌍 **Europe & Asia** control 65%+ of global market
- 🎯 **$2.46 Trillion** gaming revenue projected for 2025
- 🚀 **18.7% CAGR** in esports (faster than traditional gaming)
- 📱 **Mobile gaming** fastest growing platform segment

---

## 🎯 Key Features

✅ **Complete ETL Pipeline** - Extract, Transform, Load workflow  
✅ **Exploratory Data Analysis** - Statistical insights and trends  
✅ **AI-Powered Analytics** - Julius AI integration for advanced insights  
✅ **Interactive Dashboards** - Tableau visualizations with 8 charts  
✅ **Professional Documentation** - Detailed methodology and findings  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.13** | Data analysis & processing |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computations |
| **Julius AI** | Advanced analytics |
| **Tableau Public** | Interactive visualizations |
| **Git/GitHub** | Version control |

---

## 📁 Project Structure

```
Esports-and-Gaming-Revenue-Analytics-System/
│
├── 📂 Raw_Data/
│   └── global_gaming_esports_2010_2025.csv      # Original dataset (400 rows × 21 cols)
│
├── 📂 Python_Scripts/
│   ├── 01_data_loading.py                       # Load & inspect data
│   ├── 02_data_cleaning.py                      # Clean & validate
│   └── 03_eda_analysis.py                       # Exploratory analysis
│
├── 📂 Processed_Data/
│   ├── cleaned_gaming_data.csv                  # Clean, analysis-ready data
│   └── key_insights.csv                         # Summary metrics
│
├── 📂 Tableau/
│   └── Gaming_Esports_Dashboard.twbx            # Interactive dashboard
│
├── 📂 Documentation/
│   ├── Project_Report.md                        # Complete documentation
│   ├── Julius_AI_Analysis.pdf                   # AI-generated insights
│   └── Screenshots/                             # Dashboard images
│
└── README.md                                     # This file
```

---

## 📊 Dataset Details

**Source:** Kaggle - Global Gaming & Esports Dataset

| Attribute | Value |
|-----------|-------|
| **Records** | 400 |
| **Columns** | 21 |
| **Time Period** | 2010-2025 (16 years) |
| **Countries** | 25 |
| **Regions** | 7 (Asia, Europe, North America, South America, Africa, Middle East, Oceania) |
| **Data Quality** | ✅ No missing values, No duplicates |

### Key Columns:
- 📅 **Temporal:** Year
- 🌍 **Geographic:** Country, Region
- 💰 **Revenue:** Gaming_Revenue_BillionUSD, Esports_Revenue_MillionUSD
- 👥 **Engagement:** Active_Players_Million, Esports_Viewers_Million
- 🎮 **Market:** Top_Genre, Top_Platform
- 📊 **Metrics:** 13+ additional analytical columns

---

## 🚀 Getting Started

### Prerequisites

```bash
# Install Python 3.13+
python --version

# Install required libraries
pip install pandas numpy
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/akxyverse/data-analytics-projects.git
cd "data-analytics-projects/Domain-wise Projects/Others/Esports Gaming Revenue Analytics"
```

2. **Verify data files**
```bash
# Check if CSV exists
ls Raw_Data/global_gaming_esports_2010_2025.csv
```

3. **Run analysis scripts**
```bash
# Step 1: Load data
python Python_Scripts/01_data_loading.py

# Step 2: Clean data
python Python_Scripts/02_data_cleaning.py

# Step 3: Analyze data
python Python_Scripts/03_eda_analysis.py
```

---

## 📈 Analysis Workflow

### Phase 1: Data Preparation
```python
import pandas as pd

# Load data
df = pd.read_csv('Raw_Data/global_gaming_esports_2010_2025.csv')

# Basic info
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
```

### Phase 2: Data Cleaning
- ✅ Removed whitespace from string columns
- ✅ Validated data types
- ✅ Checked for outliers
- ✅ Exported clean dataset

### Phase 3: Exploratory Data Analysis
- 📊 Year-wise revenue trends
- 🌍 Regional market share
- 🏆 Top 10 countries ranking
- 📈 YoY growth calculations
- 🔗 Correlation analysis
- 😷 COVID-19 impact assessment

### Phase 4: Advanced Analytics (Julius AI)
- 🤖 AI-powered insights
- 📊 CAGR calculations (17.7% gaming, 18.7% esports)
- 🎯 Market concentration metrics
- 📉 Growth volatility patterns

### Phase 5: Visualization (Tableau)
Created **8 interactive charts**:
1. Revenue Trend Over Time (Line)
2. Regional Market Share (Pie)
3. Top 10 Countries (Bar)
4. Year-over-Year Growth (Bar)
5. Gaming vs Esports Comparison (Dual Bar)
6. Platform Distribution (Stacked Bar)
7. Genre Popularity (Horizontal Bar)
8. COVID Impact 2019-2022 (Line)

---

## 🔍 Key Findings

### 1️⃣ Explosive Market Growth
- Gaming revenue grew **11.5x** from $214B (2010) to $2,462B (2025)
- Sustained **17.7% annual growth** over 16 years
- Esports growing even faster at **18.7% CAGR**

### 2️⃣ Geographic Dominance
| Region | Gaming Share | Esports Share |
|--------|-------------|---------------|
| **Europe** | 39.5% | 40.7% |
| **Asia** | 26.4% | 25.8% |
| North America | 14.3% | 14.3% |
| South America | 9.5% | 9.5% |
| Others | 10.3% | 9.7% |

### 3️⃣ Top Performers
**Highest Revenue Countries (2025):**
1. 🇧🇷 Brazil - $277B
2. 🇸🇪 Sweden - $259B
3. 🇨🇦 Canada - $225B

### 4️⃣ COVID-19 Impact
- **22.5% revenue spike** in 2020 (lockdown effect)
- Player base permanently elevated post-pandemic
- New baseline established above pre-COVID levels

### 5️⃣ Platform Evolution
- 📱 **Mobile gaming** share: 20% (2010) → 50%+ (2025)
- 💻 **PC gaming** stable with core audience
- 🎮 **Console** declining share but growing absolute revenue

---

## 📊 Sample Outputs

### Python Analysis Output
```
✅ Data loaded successfully!
📊 Total Rows: 400
📊 Total Columns: 21

--- Year-wise Revenue ---
2010: $214.2B gaming, $21.1B esports
2025: $2,462.5B gaming, $278.0B esports

--- Top Countries ---
1. Brazil: $1,362.91B (total)
2. Canada: $1,280.95B
3. Sweden: $1,278.04B
```

### Correlation Insights
```
Gaming_Revenue ↔ Active_Players: 0.85 (Strong positive)
Internet_Penetration ↔ Revenue: 0.72 (Moderate positive)
Esports_Viewers ↔ Prize_Pool: 0.78 (Strong positive)
```

---

## 🎨 Tableau Dashboard

### Interactive Features:
- 🔍 **Filters:** Year range, Region, Country
- 🖱️ **Click-to-filter:** Clicking charts filters others
- 📊 **Hover tooltips:** Detailed metrics on hover
- 📱 **Responsive:** Works on desktop and tablet

### Access Dashboard:
🔗 **[View Live Dashboard on Tableau Public](https://public.tableau.com/views/GamingEsportsSalesAnalyticsDasboard/GamingEsportsRevenueAnalyticsDashboard20102025?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

---

## 💡 Business Insights & Recommendations

### For Gaming Companies:
1. **Geographic Expansion:** Prioritize Africa & Middle East (emerging markets)
2. **Mobile-First Strategy:** Invest in mobile platforms for growth
3. **Esports Investment:** Higher growth than traditional gaming
4. **Localization:** Tailor content for regional preferences

### For Investors:
1. **Market Entry:** Industry in sustained growth phase (17-18% CAGR)
2. **Geographic Allocation:** Europe/Asia for stability, LatAm for growth
3. **Segment Focus:** Esports and mobile gaming highest potential

---

## 🚧 Limitations

- **Aggregation Level:** Country-year data lacks user-level granularity
- **Coverage:** 25 countries don't represent all 195+ nations
- **Projections:** 2024-2025 data may be estimates
- **Scope:** Revenue-focused; profitability not analyzed

---

---

## 📚 Documentation

- 📄 **[Complete Project Report](Documentation/Project_Report.md)** - Detailed methodology & findings
- 🤖 **[Julius AI Analysis](Documentation/Julius_AI_Analysis.pdf)** - AI-generated insights
- 📊 **[Tableau Dashboard Guide](Documentation/Tableau_Guide.md)** - Visualization details

---

## 🤝 Contributing

Contributions welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🎓 Skills Demonstrated

**Technical:**
- Python Programming (Pandas, NumPy)
- Data Cleaning & Transformation
- Statistical Analysis
- Data Visualization (Tableau)
- AI Tool Integration

**Analytical:**
- Business Problem Framing
- Trend Identification
- Insight Generation
- Strategic Recommendations

**Soft Skills:**
- Project Management
- Technical Documentation
- Data Storytelling
- Stakeholder Communication

---

## 📞 Contact

**Author:** Akash Yadav  
**Email:** akashyadav110502@gmail.com  
**LinkedIn:** [linkedin.com/in/akash-yadav-122a75288](https://www.linkedin.com/in/akash-yadav-122a75288/)  

---

## 🙏 Acknowledgments

- **Data Source:** Kaggle Gaming & Esports Dataset
- **Tools:** Tableau Public, Julius AI
- **Inspiration:** Global gaming industry growth & esports emergence

---

## ⭐ Show Your Support

If you found this project helpful, please star [Data Analytics Projects](https://github.com/akxyverse/data-analytics-projects) on GitHub!
