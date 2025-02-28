import streamlit as st

# Configurar la página
st.set_page_config(page_title="Sobre Nosotros", page_icon="👥", layout="wide")

# CSS para personalizar estilos
st.markdown(
    """
    <style>
        .centered {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: white;
        }
        .container {
            max-width: 800px;
            margin: auto;
        }
        .card {
            background-color: #2b2b2b;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
            width: 100%;
        }
        .card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
        }
        .card h3, .card p {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor principal
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<h1 class="centered">Sobre Nosotros</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered">Descubra el equipo detrás de nuestro éxito y conozca nuestra misión, visión y valores.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="centered">Nuestra Misión</h2>', unsafe_allow_html=True)
st.markdown('<p class="centered">Ofrecer soluciones innovadoras que superen las expectativas de los clientes y impulsen los avances en la industria.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="centered">Nuestra Visión</h2>', unsafe_allow_html=True)
st.markdown('<p class="centered">Ser un líder global en tecnología, conocido por nuestro compromiso con la excelencia y la integridad.</p>', unsafe_allow_html=True)

st.markdown('<h2 class="centered">Nuestros Valores</h2>', unsafe_allow_html=True)
st.markdown('<p class="centered"><b>Integridad:</b> Mantenemos los más altos estándares de honestidad y transparencia.</p>', unsafe_allow_html=True)
st.markdown('<p class="centered"><b>Innovación:</b> Buscamos constantemente soluciones creativas y mejoras.</p>', unsafe_allow_html=True)
st.markdown('<p class="centered"><b>Enfocados en el Cliente:</b> Ponemos a nuestros clientes en el centro de todo lo que hacemos.</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Sección del equipo con tarjetas en una fila horizontal
st.markdown('<h2 class="centered">Nuestro Equipo</h2>', unsafe_allow_html=True)

# Lista de miembros del equipo
team_members = [
     {
        "name": "Giulia Naval",
        "role": "CEO & Back-end",
        "image_url": "https://aitanass.netlify.app/assets/images/Giulia.jpeg"
    },
    {
        "name": "Marcelo Bustios",
        "role": "Back-end",
        "image_url": "https://aitanass.netlify.app/assets/images/Marcelo.png"
    },
    {
        "name": "Alexander Gómez",
        "role": "Front-End & Content Creator",
        "image_url": "https://aitanass.netlify.app/assets/images/Alex.jpg"
    },
    {
        "name": "Josep Marko Quispe",
        "role": "Front-End",
        "image_url": "https://aitanass.netlify.app/assets/images/josep.png"
    }
]

# Crear columnas para mostrar las tarjetas en una fila horizontal
cols = st.columns(len(team_members))

for col, member in zip(cols, team_members):
    with col:
        st.markdown(
            f"""
            <div class="card">
                <img src="{member['image_url']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['role']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
