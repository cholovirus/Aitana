import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# Configurar API de Gemini con tu clave
GEMINI_API_KEY = "AIzaSyA4V7scBMil8EVpTuHdcrN9GCvCHRYG_aY"  # Reemplaza con tu clave de Google AI
genai.configure(api_key=GEMINI_API_KEY)

# Inicializar el modelo de Gemini
model = genai.GenerativeModel("gemini-1.5-flash-latest")  # Usa un modelo gratuito

# Estado de sesión para historial del chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "HOLA, SOY AITANA Y ESTOY AQUÍ PARA AYUDARTE. ¿CÓMO TE SIENTES HOY?"}]

# Mostrar el historial del chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Entrada del usuario
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Instrucciones para que Aitana siempre haga preguntas
        prompt_with_instructions = (
            f"Eres Aitana, un asistente experto que recopila información. Siempre debes responder con una pregunta para obtener más datos.\n\n"
            f"Historial de la conversación:\n{st.session_state.messages}\n\n"
            f"Usuario: {prompt}\n\n"
            f"Aitana (respuesta esperada):"
        )

        # Generar respuesta de Gemini
        response = model.generate_content(prompt_with_instructions)

        # Extraer respuesta del chatbot
        assistant_response = response.text if response and response.text else "Error al obtener la respuesta."

        # Agregar la respuesta al historial
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        st.chat_message("assistant").write(assistant_response)

    except Exception as e:
        st.error(f"Error al conectar con Gemini: {e}")

