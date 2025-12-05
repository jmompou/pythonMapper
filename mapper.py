import geopandas as gpd
import folium

# --- 1. CARGAR DATOS (Mismos datos de Natural Earth) ---
print("Cargando geometrías...")
# Usamos URLs directas. Si ya tienes los archivos descargados, cambia la ruta.
url_countries = "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip"
url_states = "https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_1_states_provinces.zip"

countries = gpd.read_file(url_countries)
states = gpd.read_file(url_states)

# --- 2. PREPARAR LAS CAPAS ---

# A. Ucrania
ukraine = countries[countries['NAME'] == "Ukraine"]

# B. Oblasts Rusos (Rostov, Voronezh, Kursk, Belgorod)
target_oblasts = ['Rostov', 'Voronezh', 'Kursk', 'Belgorod']
russia_oblasts = states[
    (states['admin'] == 'Russia') & 
    (states['name'].isin(target_oblasts))
]

# C. Transnistria (Stînga Nistrului)
transnistria = states[
    (states['admin'] == 'Moldova') & 
    ((states['name'] == 'Stînga Nistrului') | (states['name'].str.contains('Transnistria')))
]

# --- 3. CREAR EL MAPA INTERACTIVO ---

# Usamos 'OpenTopoMap' para que se vean MONTANAS y RELIEVE real.
# Centramos el mapa en Ucrania (aprox lat 49, lon 31)
m = folium.Map(location=[49.0, 31.0], zoom_start=6, tiles='OpenTopoMap')

# --- 4. AÑADIR LAS ZONAS COLOREADAS ---

# Estilo para Ucrania (Borde azul, relleno transparente para ver el mapa debajo)
folium.GeoJson(
    ukraine,
    name='Ucrania',
    style_function=lambda x: {
        'fillColor': 'blue',
        'color': 'blue',
        'weight': 3,
        'fillOpacity': 0.1
    },
    tooltip="Ucrania"
).add_to(m)

# Estilo para Oblasts Rusos (Rojo suave)
folium.GeoJson(
    russia_oblasts,
    name='Oblasts Fronterizos (RU)',
    style_function=lambda x: {
        'fillColor': '#ff0000',
        'color': 'red',
        'weight': 2,
        'fillOpacity': 0.3
    },
    tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['Región:'])
).add_to(m)

# Estilo para Transnistria (Naranja/Rayado visualmente con color fuerte)
folium.GeoJson(
    transnistria,
    name='Transnistria',
    style_function=lambda x: {
        'fillColor': 'orange',
        'color': 'darkorange',
        'weight': 2,
        'fillOpacity': 0.5
    },
    tooltip="Transnistria"
).add_to(m)

# --- 5. GUARDAR Y MOSTRAR ---
# Añadimos un control de capas para activar/desactivar cosas
folium.LayerControl().add_to(m)

output_file = "mapa_interactivo_ucrania.html"
m.save(output_file)

print(f"¡Mapa creado con éxito! Abre el archivo '{output_file}' en tu navegador web.")
# Si estás en Jupyter Notebook, descomenta la siguiente línea para verlo ahí mismo:
# m
