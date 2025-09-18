import json      # Para guardar y leer el conocimiento en un archivo JSON
import os        # Para verificar si el archivo ya existe

# Nombre del archivo donde se guarda la base de conocimiento
BASE_FILE = "base_conocimiento.json"

# --- Inicialización de la base de conocimiento ---
# Si el archivo aún no existe, se crea con frases iniciales
if not os.path.exists(BASE_FILE):
    base = {
        "hola": "¡Hola! ¿Cómo estás?",
        "como estas": "Muy bien, gracias. ¿Y tú?",
        "de que te gustaria hablar": "Me encantan los carros, ¿quieres hablar de motores, marcas o historia?",
    }
    # Guardamos la base inicial en el archivo JSON
    with open(BASE_FILE, "w", encoding="utf-8") as f:
        json.dump(base, f, indent=4, ensure_ascii=False)

# --- Cargar base de conocimiento existente ---
with open(BASE_FILE, "r", encoding="utf-8") as f:
    base = json.load(f)  # Aquí se carga el contenido del archivo JSON en un diccionario


# --- Función para guardar la base de conocimiento ---
def guardar_conocimiento():
    """
    Esta función sobrescribe el archivo JSON
    con la base de conocimiento actualizada.
    """
    with open(BASE_FILE, "w", encoding="utf-8") as f:
        json.dump(base, f, indent=4, ensure_ascii=False)


# --- Función para responder al usuario ---
def responder(pregunta):
    """
    Busca si la pregunta existe en la base de conocimiento.
    - Si existe: devuelve la respuesta guardada.
    - Si no existe: pide al usuario que enseñe una respuesta nueva,
      la guarda en el diccionario y la escribe en el archivo JSON.
    """
    pregunta = pregunta.lower().strip()  # Normalizamos la entrada (minúsculas y sin espacios extras)

    # Si la pregunta ya está en la base, devuelve la respuesta
    if pregunta in base:
        return base[pregunta]
    else:
        # Si no se encuentra, se activa el módulo de adquisición de conocimiento
        print("No sé qué responder a eso ")
        nueva_resp = input(f"¿Qué debería contestar cuando me digan '{pregunta}'?\n>>> ")
        
        # Guardamos la nueva respuesta en la base
        base[pregunta] = nueva_resp
        guardar_conocimiento()  # Actualizamos el archivo JSON
        
        return f"¡Listo! Aprendí algo nuevo: {nueva_resp}"


# --- Chat principal ---
print(" Bot Experto en Carros  (escribe 'salir' para terminar)\n")

# Ciclo infinito para mantener el chat activo
while True:
    user_input = input("Tú: ")  # El usuario escribe su mensaje
    if user_input.lower() == "salir":  # Condición de salida
        print("Bot: ¡Hasta luego, maneja con cuidado! 🚦")
        break  # Se rompe el ciclo para terminar el chat

    # El bot genera una respuesta
    respuesta = responder(user_input)
    print("Bot:", respuesta)
