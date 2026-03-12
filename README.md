# AtmosIntel – Hyper‑Local AQI Intelligence Platform

## Overview
**AtmosIntel** is a hyper‑local air quality intelligence system designed to convert sparse monitoring station data into **ward‑level pollution insights**. The platform uses spatial interpolation and environmental analytics to generate **real‑time pollution heatmaps**, identify high‑risk zones, and produce automated advisories for citizens and government authorities.

The goal is to enable **data‑driven urban pollution management** by transforming raw air quality data into actionable intelligence.

---

**--> Problem Statement**

Urban air quality monitoring relies on a **limited number of monitoring stations**, which often represent large geographic regions. This creates blind spots where localized pollution sources remain undetected.

For example:

- Delhi has **~47 monitoring stations**
- But contains **250+ administrative wards**

This makes it difficult for authorities to:

- Detect pollution hotspots early  
- Identify pollution sources  
- Issue localized health advisories  
- Deploy mitigation resources efficiently  

---

**--> Proposed Solution**

AtmosIntel addresses this problem by generating a **continuous air‑quality surface across the city** using spatial interpolation techniques.

The system:

1. Collects real‑time AQI data from monitoring stations  
2. Uses **Inverse Distance Weighting (IDW) interpolation with KDTree optimization**  
3. Estimates pollution levels across the city  
4. Aggregates AQI values at the **ward level**  
5. Generates **citizen advisories and government mitigation recommendations**  
6. Produces an **interactive geospatial dashboard**

---

**--> Key Features**

### 1. Hyper‑Local AQI Mapping
Transforms sparse station data into a **continuous pollution heatmap** across the city.

### 2. Ward‑Level Air Quality Intelligence
Estimates AQI values for **every administrative ward**.

### 3. Pollution Hotspot Detection
Identifies the **most polluted wards requiring immediate action**.

### 4. Automated Citizen Advisories
Generates health guidance such as:

- Wear masks  
- Avoid outdoor activity  
- Limit exposure for sensitive groups  

### 5. Government Mitigation Recommendations
Provides suggested actions such as:

- Deploy dust suppression vehicles  
- Investigate pollution sources  
- Increase environmental monitoring  

### 6. Priority Action List
Automatically ranks the **top polluted wards requiring intervention**.

---

**--> System Architecture**

```
AQI Monitoring Stations
        ↓
Real‑Time Data Collection (GitHub Dataset)
        ↓
Spatial Interpolation Model (IDW + KDTree)
        ↓
City‑Wide Pollution Surface
        ↓
Ward‑Level AQI Aggregation
        ↓
Advisory & Decision Engine
        ↓
Interactive Monitoring Dashboard
```

---

**--> Technology Stack**

| Component | Technology |
|--------|--------|
| Data Processing | Python, Pandas, NumPy |
| Geospatial Analysis | GeoPandas, Shapely |
| Spatial Modeling | SciPy KDTree, IDW Interpolation |
| Visualization | Folium |
| Data Pipeline | GitHub Actions |
| Development | Google Colab |

---

** --> Repository Structure**

```
delhi-aqi-dataset
│
├── aqi_data.csv
├── delhi_wards.geojson
├── AtmosIntel_MVP.ipynb
├── AtmosIntel_dashboard.html
├── priority_wards.csv(created in the colab notebook)
├── aqi_collector.py
└── .github/workflows/
```

---

**How to Run the Project**

### 1️⃣ Open the Notebook

Open **AtmosIntel_MVP.ipynb** in **Google Colab**.

### 2️⃣ Run All Cells

The notebook will:

- Load AQI data from GitHub  
- Display monitoring stations  
- Perform spatial interpolation  
- Estimate ward‑level AQI  
- Generate advisories  

### 3️⃣ Generate Dashboard

The notebook exports an interactive dashboard:

```
AtmosIntel_dashboard.html
```

---

**Dashboard Capabilities**

The generated dashboard allows users to:

- View **real‑time AQI distribution**
- Identify **high‑risk wards**
- Inspect monitoring stations
- Monitor pollution hotspots
- Access automated advisories

---

**Future Improvements**

Potential future enhancements include:

- Real‑time pollutant monitoring (PM2.5, PM10, NO₂, SO₂)
- Machine learning based **pollution source detection**
- Wind‑driven pollution trajectory analysis
- Automated alert notification systems
- Smart city command center integration

---

**Impact**

AtmosIntel demonstrates how environmental data can be transformed into **actionable intelligence for urban governance**.

Potential benefits include:

- Early detection of pollution hotspots  
- Targeted mitigation strategies  
- Improved public health awareness  
- Data‑driven environmental policy  

---

## 👨‍💻 Authors

Developed by:

- **Durlabh Biswas**
- **Ayush Kumar**
- **Shreyan Porel**
- **Vivyaan Ojha**
---

Explore the notebook and dashboard to see how AtmosIntel converts raw AQI data into hyper‑local pollution intelligence.
