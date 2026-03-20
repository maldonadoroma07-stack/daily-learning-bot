import os
import requests
import datetime

# --- CONFIGURACIÓN SEGURA (GitHub Secrets) ---
TOKEN = os.getenv("8647406754:AAG_VqudtiqoOaaUhM2UN9NywW3oKf8Cqs0")
CHAT_ID = os.getenv("5600097537")

# --- TU PLAN DE ESTUDIOS ---
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
    # Obtener el día de la semana (0 = Lunes, 6 = Domingo)
    dia_actual = datetime.datetime.now().weekday()
    tema_hoy = plan_semanal.get(dia_actual, "Día de descanso o repaso libre")
    
    mensaje = f"🚀 ¡Hola Romario! Hoy toca aprender:\n\n{tema_hoy}\n\n¡A darle con todo! 🔥"
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje}
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Notificación enviada con éxito.")
        else:
            print(f"Error de Telegram: {response.text}")
    except Exception as e:
        print(f"Ocurrió un error de conexión: {e}")

if __name__ == "__main__":
    enviar_notificacion()
