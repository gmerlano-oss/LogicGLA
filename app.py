import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lógica Matemática", page_icon="🧠")

st.title("🧠 Entrenador de Lógica")
st.write("Selecciona los valores de P y Q para ver los resultados.")

# Interfaz de usuario
col_input1, col_input2 = st.columns(2)
with col_input1:
    p = st.toggle("Proposición P", value=True)
with col_input2:
    q = st.toggle("Proposición Q", value=False)

st.divider()

# Cálculos
st.subheader("Resultados Lógicos")
c1, c2, c3 = st.columns(3)
c1.metric("P ∧ Q (AND)", "V" if p and q else "F")
c2.metric("P ∨ Q (OR)", "V" if p or q else "F")
c3.metric("P ⊕ Q (XOR)", "V" if p ^ q else "F")

# Tabla de verdad interactiva
if st.checkbox("Mostrar Tabla de Verdad"):
    data = [
        {"P": True, "Q": True, "AND": True, "OR": True},
        {"P": True, "Q": False, "AND": False, "OR": True},
        {"P": False, "Q": True, "AND": False, "OR": True},
        {"P": False, "Q": False, "AND": False, "OR": False},
    ]
    st.table(pd.DataFrame(data))
