import streamlit as st

st.set_page_config(page_title="Mi Chatbot", page_icon="💬", layout="wide")

# URL de la imagen
image_url = "https://www.flowww.com.mx/hubfs/Q42022%20Octubre/M%C3%A9xico/Blog/historia-clinica-diagnostico-preciso.webp"  # Cambia esto por tu URL real

# CSS para centrar el título
st.markdown("""
    <style>
        
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
        }
        .image-container {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Centrar el título
st.markdown('<h1 class="title">¡Hola! Soy Aitana, estoy aquí para poder escucharte</h1>', unsafe_allow_html=True)

# Mostrar imagen desde la URL con el nuevo parámetro
st.markdown('<div class="image-container">', unsafe_allow_html=True)
st.image(image_url, use_container_width=True)  # ✅ Nuevo parámetro sin advertencias
st.markdown('</div>', unsafe_allow_html=True)
