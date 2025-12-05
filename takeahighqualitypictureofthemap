import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def map_to_image(html_file_path, output_image_path, width=1920, height=1080, wait_time=5):
    """
    Convierte un mapa HTML de Folium en una imagen estática PNG.
    """
    
    # 1. Verificar que el archivo HTML existe
    if not os.path.exists(html_file_path):
        print(f"Error: No encuentro el archivo {html_file_path}")
        return

    # Obtener la ruta absoluta del archivo HTML (necesario para el navegador)
    abs_html_path = os.path.abspath(html_file_path)
    file_url = f"file://{abs_html_path}"

    print(f"Iniciando navegador 'headless' para capturar: {file_url}...")

    # 2. Configurar opciones de Chrome (para que se ejecute sin ventana visible)
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ejecutar en segundo plano
    # Definir el tamaño de la "ventana" del navegador (resolución de la imagen)
    chrome_options.add_argument(f"--window-size={width},{height}") 
    chrome_options.add_argument("--hide-scrollbars")

    # 3. Inicializar el navegador robot
    # ChromeDriverManager se encarga de bajar la versión correcta del driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        # 4. Cargar la página
        driver.get(file_url)
        
        print(f"Cargando mapa... Esperando {wait_time} segundos para que se rendericen las montañas...")
        # IMPORTANTE: Esperar a que se carguen las teselas de OpenTopoMap.
        # Si tu internet es lento, aumenta este número.
        time.sleep(wait_time)

        # 5. Sacar captura de pantalla
        driver.save_screenshot(output_image_path)
        print(f"¡Imagen guardada con éxito en: {output_image_path}!")

    except Exception as e:
        print(f"Ocurrió un error al tomar la captura: {e}")
    finally:
        # 6. Cerrar el navegador robot pase lo que pase
        driver.quit()

# --- EJECUCIÓN ---
# Asegúrate de que este nombre coincide con el que genera tu script principal
input_html = "mapa_interactivo_ucrania.html" 
output_png = "mapa_statico_ucrania.png"

# Llamamos a la función. Puedes cambiar el ancho/alto si quieres más resolución.
map_to_image(input_html, output_png, width=1920, height=1080, wait_time=8)
