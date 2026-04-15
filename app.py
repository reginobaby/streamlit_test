import streamlit as st
import scipy.stats
import time

st.header('Lanzar una moneda')

# 1. Configuramos los controles (SOLO UNA VEZ)
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

# 2. Definimos la función del experimento
def toss_coin(n):
    # El gráfico empieza en 0.5 (mitad y mitad)
    chart = st.line_chart([0.5])
    
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        
        # Esto es lo que hace que el gráfico se mueva en vivo
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# 3. Lo que pasa cuando picas el botón
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    final_mean = toss_coin(number_of_trials)
    st.write(f'La media final de caras fue: {final_mean:.2f}')