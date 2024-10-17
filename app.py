import streamlit as st
st.title("Mi primera app")
st.header("header")
st.subheader('subheader')
st.write("text")

slide=0
#Checkboxes
if st.checkbox('Mostrar datos'):
    #Se puede ejecutar alguna función bajo el condicional
    check = True #Definir variable global para otras funciones dentro de la página
    st.subheader('Datos')
    st.write("active")
    slide = st.slider('hour', 0, 23, 17)
if slide >= 15: #[nombre, inicio, final, valor default]
    st.write("active")
else:
    st.write("inactive")
button_numeros = st.button("escribir")
if button_numeros:
    for i in range(20):
        st.write(i+1)
temas_input = st.text_input("Label:", "texto default")
button_texto = st.button("Escribir input")
if button_texto:
    st.write(f"Has escrito: {temas_input}")
add_selectbox = st.sidebar.selectbox(
'How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone')
)