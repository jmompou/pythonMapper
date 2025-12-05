# 🗺️ Ukraine & Border Regions Geo-Strategic Mapper

A Python-based geospatial tool that generates high-resolution, interactive maps focusing on the geopolitical and physical geography of Ukraine and its critical border regions.

This project bridges the gap between political boundaries and terrain analysis by overlaying administrative data onto topographically detailed base maps.

## 🚀 Overview

This tool automatically downloads vector data (Shapefiles) and renders an interactive HTML map. It is designed to visualize the correlation between **political borders** and **physical barriers** (mountains, rivers) in the Eastern European theater.

### Key Features

  * **🇺🇦 Ukraine Focus:** High-precision boundary visualization.
  * **🇷🇺 Critical Border Oblasts:** Specifically filters and highlights key Russian logistical and border regions: **Rostov, Voronezh, Kursk, and Belgorod**.
  * **🇲🇩 Transnistria Highlight:** Distinct visualization for the breakaway region of Transnistria (Stînga Nistrului).
  * **🏔️ Physical Geography:** Uses **OpenTopoMap** tiles to render real-time topography, including:
      * **Mountain Ranges** (elevation and relief shading).
      * **River Systems** (Dnieper, Don, etc.).
      * **Settlements** (Dynamic zooming from oblast level down to street level).
  * **interactive UI:** Zoomable and pannable interface powered by Leaflet.js (via Folium).

## 🛠️ Tech Stack

  * **Python 3.x**
  * **[GeoPandas](https://geopandas.org/):** For handling spatial data, coordinate reference systems, and filtering attributes.
  * **[Folium](https://python-visualization.github.io/folium/):** For generating the interactive Leaflet map.
  * **Matplotlib:** (Optional/Backend) For geometry handling.

## 📦 Data Sources

The project dynamically fetches data from **Natural Earth** (1:10m High-Resolution scale):

  * `ne_10m_admin_0_countries`: International borders.
  * `ne_10m_admin_1_states_provinces`: Internal administrative divisions (Oblasts).

## 📥 Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ukraine-geo-mapper.git
    cd ukraine-geo-mapper
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.

    ```bash
    pip install geopandas folium mapclassify
    ```

## 💻 Usage

1.  Run the main script:

    ```bash
    python main.py
    ```

    *(Note: The first run may take a few moments to download the high-resolution shapefiles).*

2.  Open the generated file in your browser:

      * `mapa_interactivo_ucrania.html`

## 🎨 Visualization Logic

| Region | Color Code | Significance |
| :--- | :--- | :--- |
| **Ukraine** | 🔵 **Blue** | Primary Area of Interest (AOI). |
| **Russian Border Oblasts** | 🔴 **Red** | Critical border/logistics zones (Rostov, Voronezh, Kursk, Belgorod). |
| **Transnistria** | 🟠 **Orange** | Strategic zone of tension in the southwest. |

## 📜 License

