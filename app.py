import pandas as pd
import scipy.stats
import streamlit as st
import time

# 1. Estas variables guardan el historial (Session State)
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

# 2. Creamos la gráfica
chart = st.line_chart([0.5])

# 3. La función del volado
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# 4. Controles para el usuario
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    # Aumentamos el número de experimento
    st.session_state['experiment_no'] += 1
    
    st.write(f'Experimento n.º {st.session_state["experiment_no"]}: {number_of_trials} intentos en curso.')
    
    # Ejecutamos el volado
    mean = toss_coin(number_of_trials)
    
    # Guardamos el resultado en el historial (DataFrame)
    new_row = pd.DataFrame([[st.session_state['experiment_no'], number_of_trials, mean]], 
                           columns=['no', 'iteraciones', 'media'])
    
    st.session_state['df_experiment_results'] = pd.concat([st.session_state['df_experiment_results'], new_row], axis=0)

# 5. Mostramos la tabla con el historial de todos los intentos
st.write(st.session_state['df_experiment_results'])