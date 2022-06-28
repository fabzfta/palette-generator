import streamlit as st
from src import palette

st.title('Palette generator')
uploaded_image = st.file_uploader(
    'Upload a image',
    type=['jpg', 'jpeg']
)
col1, col2 = st.columns(2)
if uploaded_image:
    with col1:
        st.image(uploaded_image)
    with col2:
        n_clusters = st.slider('Number of Colors', 2, 8 , 5)
        if st.button("Generate palette"):
            with st.spinner('Generating Palette...'):
                cores, cores_hex = palette.get(uploaded_image, n_clusters)
    
            # retorna figura
            figura = palette.show(cores)
            st.pyplot(figura)
            st.code(f"{cores_hex}")
            
            # Adiciona botão de salvar
            btn = st.download_button(
                label = "Download Palette",
                data = palette.save(figura),
                file_name = 'palette.png',
                mime = "image/png"
            )
        