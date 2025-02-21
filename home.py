import streamlit as st

from databases import models
from login import twitch_login

db = models.SessionLocal()
models.create_tables()

st.set_page_config(page_title="TMW - Education", page_icon="📘", initial_sidebar_state="collapsed")


def home():

    twitch_login.twitch_login(db)

    with open("./home.md") as openfile:
        txt = openfile.read()
    st.markdown(txt)

        
    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Confira nossos cursos futuros e que já aconteceram durante este ano.")
            
        with cols[1]:
            cols = st.columns(3)
            with cols[-1]:
                b1 = st.button("2025")
                if b1:
                    st.switch_page("./pages/material_2025.py")

    with st.container(border=True):
        cols = st.columns(2)
        with cols[0]:
            st.markdown("Aqui você entra tudo que rolou em 2024, cursos e projetos")
            
        with cols[1]:
            cols = st.columns(3)
            with cols[-1]:
                b2 = st.button("2024")
                if b2:
                    st.switch_page("./pages/material_2024.py")


    st.markdown("Caso esteja em dúvida por onde seguir, realize nosso Plano de Desenvolvimento Individual (PDI) para escolher a trilhar correta.")

def main():
    home()

if __name__ == "__main__":
    main()
    