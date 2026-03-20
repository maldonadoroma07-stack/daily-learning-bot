import os
import requests
import datetime

# --- CONFIGURACIÓN SEGURA ---
# No borres estas palabras, GitHub las usará para buscar tus secretos
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

plan_semanal = {
    0: "Lunes: Fundamentos de Python (Sintaxis y Estructuras)",
    1: "Martes: Manipulación de Datos con Pandas (Limpieza y Filtros)",
    2: "Miércoles: Visualización de Datos con Matplotlib/Seaborn",
    3: "Jueves: Estadística Descriptiva e Inferencial aplicada",
    4: "Viernes: SQL Avanzado (Joins, Subconsultas, CTEs)",
    5: "Sábado: Introducción a Machine Learning (Regresión Lineal)",
    6: "Domingo: Procesamiento de Imágenes con OpenCV (Básico)"
}

def enviar_notificacion():
    dia_actual = datetime.datetime.now().weekday()
    tema_hoy = plan_semanal.get(dia_actual, "Día de descanso")
    
    mensaje = f"🚀 ¡Hola Romario! Hoy toca aprender:\n\n{tema_hoy}\n\n¡A darle con todo! 🔥"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    try:
        response = requests.post(url, data={"chat_id": CHAT_ID, "text": mensaje})
        print("Estado del envío:", response.status_code)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    enviar_notificacion()
