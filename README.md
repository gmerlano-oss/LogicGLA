# LogicGLA
Práctica lógica matemática 
import streamlit as st

st.set_page_config(page_title="Lógica Proposicional", page_icon="⚖️")

st.title("⚖️ Práctica de Reglas de Inferencia")

# Diccionario de reglas para el modo práctica
reglas = {
    "Modus Ponendo Ponens": "Si P → Q es verdad, y P es verdad, entonces Q es verdad.",
    "Modus Tollendo Tollens": "Si P → Q es verdad, y ¬Q es verdad, entonces ¬P es verdad.",
    "Doble Negación": "¬(¬P) es equivalente a P.",
    "Tautología": "Una fórmula que siempre es verdadera (ej: P ∨ ¬P)."
}

modo = st.sidebar.radio("Selecciona modo:", ["Explorador", "Desafío de Reglas"])

if modo == "Explorador":
    st.subheader("Simulador de Reglas Básicas")
    p = st.toggle("P (Verdadero)")
    
    st.write(f"**Doble Negación:** ¬(¬P) es **{p}**")
    st.write(f"**Tautología (P ∨ ¬P):** Siempre es **True**")

    st.divider()
    st.info("💡 Consejo: El Ponens 'pone' (afirma el consecuente), el Tollens 'tolle' (niega el antecedente).")

else:
    st.subheader("¿Qué regla se está aplicando?")
    
    ejercicios = [
        {"pregunta": "Premisa 1: Si llueve, hay nubes. Premisa 2: Llueve. Conclusión: Hay nubes.", "correcta": "Modus Ponendo Ponens"},
        {"pregunta": "Premisa 1: Si estudio, apruebo. Premisa 2: No aprobé. Conclusión: No estudié.", "correcta": "Modus Tollendo Tollens"},
        {"pregunta": "No es cierto que no soy estudiante. Conclusión: Soy estudiante.", "correcta": "Doble Negación"}
    ]
    
    for i, ej in enumerate(ejercicios):
        st.write(f"**Ejercicio {i+1}:** {ej['pregunta']}")
        opcion = st.selectbox("Selecciona la regla:", ["Selecciona...", "Modus Ponendo Ponens", "Modus Tollendo Tollens", "Doble Negación"], key=f"ex_{i}")
        
        if opcion != "Selecciona...":
            if opcion == ej['correcta']:
                st.success("¡Correcto!")
            else:
                st.error("Sigue intentando.")
