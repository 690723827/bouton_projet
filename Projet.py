import streamlit as st
import pandas as pd
import altair as alt

# Page configuration
st.set_page_config(
    page_title="Iris Classification", 
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title('Iris Classification')
    page_selection = st.radio(
        "Navigation",
        ('About', 'Dataset', 'EDA', 'Data Cleaning / Pre-processing', 'Machine Learning', 'Prediction', 'Conclusion')
    )

# Load data
try:
    with st.spinner('Chargement des données...'):
        df = pd.read_csv('iris.csv', delimiter=',')
    st.success("Fichier chargé avec succès.")
except FileNotFoundError:
    st.error("Le fichier iris.csv est introuvable. Veuillez vérifier son emplacement.")
    st.stop()

# Content based on page_selection
if page_selection == 'About':
    st.header("À propos de l'application")
    st.write("Ceci est une application Streamlit pour explorer les données des Iris.")
    st.write("Construite avec Streamlit par Stéphane C. K. Tékouabou.")
    
elif page_selection == 'Dataset':
    st.header("Dataset")
    st.subheader('Description des données')
    preview_option = st.selectbox(
        "Choisissez une option de prévisualisation :",
        ["Aucune", "Head", "Tail", "Infos", "Shape"]
    )
    if preview_option == "Head":
        st.write(df.head(2))
    elif preview_option == "Tail":
        st.write(df.tail())
    elif preview_option == "Infos":
        buffer = []
        df.info(buf=buffer)
        st.text("".join(buffer))
    elif preview_option == "Shape":
        st.write(df.shape)

elif page_selection == 'EDA':
    st.header("Analyse exploratoire des données (EDA)")
    chart = alt.Chart(df).mark_point().encode(
        x='petal_length',
        y='petal_width',
        color="species"
    ).properties(
        title="Scatter plot des longueurs et largeurs des pétales"
    )
    st.altair_chart(chart, use_container_width=True)
