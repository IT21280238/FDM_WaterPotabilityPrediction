# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:55:12 2023

@author: Dell
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open(r"D:\YEAR 3\FDM Project\trained_model2.sav", 'rb'))

# creating a function for Prediction

def potability_prediction(input_data):
    
    #x = normalize_df(input_data)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'Water is not potable'
    else:
      return 'Water is potable'
  

def get_ph_alert_message(ph):
    ph_ranges = [
        (0, 2, "Strong Acidic: Extremely corrosive and harmful to health."),
        (3, 6, "Moderately Acidic: Still highly acidic and potentially harmful if ingested."),
        (7, 7, "Neutral: Generally safe for consumption."),
        (8, 11, "Moderately Alkaline: Usually safe for drinking, and may have benefits."),
    ]

    alert_message = "pH value not recognized."

    for min_range, max_range, message in ph_ranges:
        if min_range <= ph <= max_range:
            alert_message = message
            break

    return alert_message
    
def main():
    
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://cdn.pixabay.com/photo/2023/04/03/11/45/water-7896610_1280.jpg');
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    
    # giving a title
    st.title('Potability Prediction')
    
    # getting the input data from the user
    custom_css = """
        <style>
        
        .stForm {
            border: none;
            box-shadow: none;
            background: transparent;
            padding: 0;
            margin: 0;
        }
    
        .stTextInput, .stNumberInput, .stSelectbox, .stDateInput, .stSlider {
            width: 75%;
            margin: 0 auto;
        }
        .st-form-container {
            max-width: 1000px;  /* Adjust the width as needed */
            background-color: #FAFAFA;
        }
        
        .potabilityform_sec{
            background-color: #D6D7F3;
            }
        
        .stForm button[type="submit"] {
            background-color: #0074cc;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 100px auto 20px auto;
            display: block;
        }

        .st-success {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            border-radius: 5px;
            padding: 10px;
            margin: 20px 0;
        }

        .custom-slider::-webkit-slider-thumb {
            background: #4BB0FF; /* Set the thumb (slider handle) color */
        }

        .custom-slider::-webkit-slider-runnable-track {
            background: #4BB0FF; /* Set the track color */
        }
        

        </style>
        """
    
    st.markdown(custom_css, unsafe_allow_html=True)
    
    
    with st.form(key='potabilityform'):
        
        selected_value = st.slider("pH Level", 0.00, 14.00 ,key='custom-slider')
        ph = (selected_value - 0.0) / (13.999999999999998 - 0.0)

        
        col1,col2 = st.columns(2)
        
        with col1:
            Hardness = ((float(st.text_input('Hardness (mg/L)', "0.0")) - 73.4922336890611) / (323.124 - 73.4922336890611))
            Solids = ((float(st.text_input('Total dissolved solids (ppm)', "0.0")) - 320.942611274359) / (61227.19600771213 - 320.942611274359))
            Chloramines = ((float(st.text_input('Chloramines Level (ppm)', "0.0")) - 0.3520000000000003) / (13.127000000000002 - 0.3520000000000003))
            Sulfate = ((float(st.text_input('Sulfate Level (mg/L)', "0.0")) - 129.00000000000003) / (481.0306423059972 -129.00000000000003))
            
        with col2:
            Conductivity = ((float(st.text_input('Conductivity (μS/cm)', "0.0")) - 181.483753985146) / (753.3426195583046 - 181.483753985146))
            Organic_carbon = ((float(st.text_input('Total organic carbon level (ppm)', "0.0")) - 2.1999999999999886) / (28.30000000000001 - 2.1999999999999886))
            Trihalomethanes = ((float(st.text_input('Trihalomethanes Level (μg/L)', "0.0")) - 0.7379999999999995) / (124.0 - 0.7379999999999995))
            Turbidity = ((float(st.text_input('Turbidity (NTU)', "0.0")) - 1.45) / (6.739 - 1.45))
            
        # code for Prediction
        diagnosis = ''
        
        st.markdown('<style>div.stButton > button { display: block; margin: 0 auto; }</style>', unsafe_allow_html=True)
        
        # creating a button for Prediction
        
        if st.form_submit_button('Potability Test Result'):
            diagnosis = potability_prediction([ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity])
            result_style = f"background-color: {'#4CAF50' if diagnosis == 'Water is potable' else '#FF5733'}; color: white; text-align: center; border-radius: 5px; padding: 10px; margin: 20px 0;"
            st.markdown(f'<div style="{result_style}">{diagnosis}</div>', unsafe_allow_html=True)

      
    #ph = st.text_input('pH Level')
    #Hardness = st.text_input('Hardness')
    #Solids = st.text_input('Total dissolved solids')
    #Chloramines = st.text_input('Chloramines Level')
    #Sulfate = st.text_input('Sulfate Level')
    #Conductivity = st.text_input('Conductivity')
    #Organic_carbon = st.text_input('Total organic carbon level')
    #Trihalomethanes = st.text_input('Trihalomethanes Level')
    #Turbidity = st.text_input('Turbidity')
    


if __name__ == '__main__':
        main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    