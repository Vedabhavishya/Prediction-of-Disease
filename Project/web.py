import os
import pickle # pre trained model loading
import streamlit as st    # web app

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

diabetes_model= pickle.load(open(r"C:\Users\vedab\Microsoft_AI\Project\training_models\diabetes_models.sav",'rb'))
heart_disease_model=pickle.load(open(r"C:\Users\vedab\Microsoft_AI\Project\training_models\best_heart_disease_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\vedab\Microsoft_AI\Project\training_models\parkinson_models.sav",'rb'))

st.sidebar.title('Prediction of Disease Outbreak System')
selected = st.sidebar.radio("Choose a prediction model:", ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'])

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
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
        diab_diagnosis= 'The person is diabetic' if diab_prediction[0]==1 else 'The person is not diabetic'
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
        try:
            user_input = [float(x) if x.strip() != "" else 0.0 for x in user_input]
        except ValueError:
            st.error("Invalid input! Please enter only numbers.")
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
    st.success(heart_diagnosis)

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    inputs = [
        'Enter fundamental frequency', 'Enter highest frequency', 'Enter lowest frequency',
        'Enter jitter percentage', 'Enter absolute jitter', 'Enter RAP jitter',
        'Enter PPQ jitter', 'Enter DDP jitter', 'Enter shimmer value',
        'Enter shimmer in dB', 'Enter APQ3 shimmer', 'Enter APQ5 shimmer',
        'Enter APQ shimmer', 'Enter DDA shimmer', 'Enter noise-to-harmonics ratio',
        'Enter harmonics-to-noise ratio', 'Enter recurrence period entropy',
        'Enter detrended fluctuation', 'Enter first spread measure', 'Enter second spread measure',
        'Enter correlation dimension', 'Enter pitch period entropy'
    ]
    user_input = []
    for idx, label in enumerate(inputs):
        with (col1 if idx % 3 == 0 else col2 if idx % 3 == 1 else col3):
            user_input.append(st.text_input(label))
    parkinsons_diagnosis = ''
    if st.button('Parkinsons Disease Test Result'):
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = 'The person has Parkinson’s disease' if parkinsons_prediction[0] == 1 else 'The person does not have Parkinson’s disease'
    st.success(parkinsons_diagnosis)
