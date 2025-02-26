import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

diabetes_model= pickle.load(open(r"C:\Users\vedab\Microsoft_AI\Project\training_models\diabetes_models.sav",'rb'))
heart_disease_model=pickle.load(open(r"C:\Users\vedab\Microsoft_AI\Project\training_models\best_heart_disease_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\vedab\Microsoft_AI\Project\training_models\parkinson_models.sav",'rb'))
with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI  value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of the person')
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreeFunction, Age]
        user_input= [float(x) for x in user_input]
        diab_prediction= diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'
    st.success(diab_diagnosis)
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of person')
    with col2:
        sex = st.text_input('Gender of person')
    with col3:
        cp = st.text_input('Chest Pain Type (cp value)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (trestbps)')
    with col2:
        chol = st.text_input('Cholesterol Level (chol)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (fbs)')
    with col1:
        restecg = st.text_input('Resting ECG Results (restecg)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate (thalach)')
    with col3:
        exang = st.text_input('Exercise Induced Angina (exang)')
    with col1:
        oldpeak = st.text_input('ST Depression (oldpeak)')
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment (slope)')
    with col3:
        ca = st.text_input('Number of Major Vessels (ca)')
    with col1:
        thal = st.text_input('Thalassemia (thal)')
    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        # Ensure all inputs are numeric
        try:
            user_input = [float(x) if x.strip() != "" else 0.0 for x in user_input]
        except ValueError:
            st.error("Invalid input! Please enter only numbers.")

        #user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    
    st.success(heart_diagnosis)

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo_Hz = st.text_input('Enter fundamental frequency')
    with col2:
        MDVP_Fhi_Hz = st.text_input('Enter highest frequency')
    with col3:
        MDVP_Flo_Hz = st.text_input('Enter lowest frequency')
    with col1:
        MDVP_Jitter_Percent = st.text_input('Enter jitter percentage')
    with col2:
        MDVP_Jitter_Abs = st.text_input('Enter absolute jitter')
    with col3:
        MDVP_RAP = st.text_input('Enter RAP jitter')
    with col1:
        MDVP_PPQ = st.text_input('Enter PPQ jitter')
    with col2:
        Jitter_DDP = st.text_input('Enter DDP jitter')
    with col3:
        MDVP_Shimmer = st.text_input('Enter shimmer value')
    with col1:
        MDVP_Shimmer_dB = st.text_input('Enter shimmer in dB')
    with col2:
        Shimmer_APQ3 = st.text_input('Enter APQ3 shimmer')
    with col3:
        Shimmer_APQ5 = st.text_input('Enter APQ5 shimmer')
    with col1:
        MDVP_APQ = st.text_input('Enter APQ shimmer')
    with col2:
        Shimmer_DDA = st.text_input('Enter DDA shimmer')
    with col3:
        NHR = st.text_input('Enter noise-to-harmonics ratio')
    with col1:
        HNR = st.text_input('Enter harmonics-to-noise ratio')
    with col2:
        RPDE = st.text_input('Enter recurrence period entropy')
    with col3:
        DFA = st.text_input('Enter detrended fluctuation')
    with col1:
        spread1 = st.text_input('Enter first spread measure')  
    with col2:
        spread2 = st.text_input('Enter second spread measure')
    with col3:
        D2 = st.text_input('Enter correlation dimension')
    with col1:
        PPE = st.text_input('Enter pitch period entropy') 

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Disease Test Result'):
        user_input = [
            MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_Percent,
            MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
            MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
            MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA,
            spread1, spread2, D2, PPE
        ]

        user_input = [float(x) for x in user_input]  # Convert inputs to float

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinson’s disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinson’s disease'

    st.success(parkinsons_diagnosis)