# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 20:50:05 2023

@author: User
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open("C:/Users/User/Documents/MultipleDiseasePrediction/savedmodels/diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open("C:/Users/User/Documents/MultipleDiseasePrediction/savedmodels/heart_disease_model.sav",'rb'))
parkinsons_model = pickle.load(open("C:/Users/User/Documents/MultipleDiseasePrediction/savedmodels/parkinsons_model.sav",'rb'))
breast_model = pickle.load(open("C:/Users/User/Documents/MultipleDiseasePrediction/savedmodels/breast_cancer.sav",'rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction',
                           ['Home','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction','Breast Cancer'],
                           icons=['house','activity','heart','person','person'],
                           default_index = 0)


#prediction Page
if(selected == 'Home'):
    st.title('Multile Disease Prediction System Using Machine Learning\t\t\t\t\t')
    
    st.write('\t\tWelcome to our state-of-the-art Disease Prediction System, where cutting-edge machine learning technology meets healthcare expertise to revolutionize the way we approach well-being. Our platform is designed to predict a multitude of diseases with unparalleled accuracy, offering users a proactive stance on their health.  At the core of our system is the power of machine learning algorithms, providing personalized health insights based on individual health profiles. Not only do we predict diseases across a comprehensive spectrum, but we also empower users with tailored preventive strategies, ensuring a holistic approach to health management. Navigate effortlessly through our user-friendly interface, making health predictions accessible to all. Stay informed in real-time with updates on your health status, allowing you to take timely actions for a healthier life. Rest assured, your health data is handled with the highest standards of security and privacy.')
    
    
    
    
    
if(selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction Using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
if(selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex (Male - 1 : Female - 0)')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        input_data = [[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]]

        heart_prediction = heart_disease_model.predict(input_data)
        #heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
if(selected == 'Parkinsons Prediction'):
    
    st.title('Parkinsons Prediction Using ML')
    
    col1, col2, col3, col4 = st.columns(4)  
    
    with col1:
        fo = st.text_input('MDVP Fo')
        
    with col2:
        fhi = st.text_input('MDVP Fhi')
        
    with col3:
        flo = st.text_input('MDVP Flo')
        
    with col4:
        Jitter_percent = st.text_input('MDVP Jitter')
        
    with col1:
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)')
        
    with col2:
        RAP = st.text_input('MDVP RAP')
        
    with col3:
        PPQ = st.text_input('MDVP PPQ')
        
    with col4:
        DDP = st.text_input('Jitter DDP')
        
    with col1:
        Shimmer = st.text_input('MDVP Shimmer')
        
    with col2:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
        
    with col3:
        APQ3 = st.text_input('Shimmer APQ3')
        
    with col4:
        APQ5 = st.text_input('Shimmer APQ5')
        
    with col1:
        APQ = st.text_input('MDVP APQ')
        
    with col2:
        DDA = st.text_input('Shimmer DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col4:
        HNR = st.text_input('HNR')
        
    with col1:
        RPDE = st.text_input('RPDE')
        
    with col2:
        DFA = st.text_input('DFA')
        
    with col3:
        spread1 = st.text_input('spread1')
        
    with col4:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    
    
if(selected == 'Breast Cancer'):
    
    st.title('Breast Cancer Prediction Using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mean_radius  = st.text_input('mean radius')
        
    with col2:
        mean_texture = st.text_input('mean texture')
    
    with col3:
        mean_perimeter = st.text_input('mean perimeter')
    
    with col1:
        mean_area = st.text_input('mean area')
    
    with col2:
        mean_smoothness = st.text_input('mean smoothness')
    
    with col3:
        mean_compactness = st.text_input('mean compactness')
    
    with col1:
        mean_concavity = st.text_input('mean concavity')
    
    with col2:
        mean_concave_points = st.text_input('mean concave points')
        
    with col3:
        mean_symmetry = st.text_input('mean symmetry')
    
    with col1:
        mean_fractal_dimension = st.text_input('mean fractal dimension')
    
    with col2:
        radius_error = st.text_input('radius error')
        
    with col3:
        texture_error = st.text_input('texture error')
    
    with col1:
        perimeter_error = st.text_input('perimeter error')
    
    with col2:
        area_error = st.text_input('area error')
        
    with col3:
        smoothness_error = st.text_input('smoothness error')
        
    with col1:
        compactness_error = st.text_input('compactness error')
    
    with col2:
        concavity_error = st.text_input('concavity error')
        
    with col3:
        concave_points_error = st.text_input('concave points error')
    
    with col1:
        symmetry_error = st.text_input('symmetry error')
    
    with col2:
        fractal_dimension_error = st.text_input('fractal dimension error')
        
    with col3:
        worst_radius = st.text_input('worst radius')
    
    with col1:
        worst_texture = st.text_input('worst texture')
    
    with col2:
        worst_perimeter = st.text_input('worst perimeter')
        
    with col3:
        worst_area = st.text_input('worst area')
        
    with col1:
        worst_smoothness = st.text_input('worst smoothness')
    
    with col2:
        worst_compactness = st.text_input('worst compactness')
        
    with col3:
        worst_concavity = st.text_input('worst concavity')
    
    with col1:
       worst_concave_points = st.text_input('worst concave points')
    
    with col2:
        worst_symmetry = st.text_input('worst symmetry')
        
    with col3:
        worst_fractal_dimension = st.text_input('worst fractal dimension')

    
        

  
    


        
    # code for Prediction
    bc = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        breast_pred = breast_model.predict([[float(mean_radius), float(mean_texture), float(mean_perimeter), float(mean_area), float(mean_smoothness), float(mean_compactness), float(mean_concavity), float(mean_concave_points),float(mean_symmetry) ,float(mean_fractal_dimension),float(radius_error),float(texture_error),float(perimeter_error),float(area_error),float(smoothness_error),float(compactness_error),float(concavity_error),float(concave_points_error),float(symmetry_error),float(fractal_dimension_error),float(worst_radius), float(worst_texture),float(worst_perimeter),float(worst_smoothness),float(worst_compactness),float(worst_concavity),float(worst_concave_points),float(worst_symmetry),float(worst_fractal_dimension)]])
        
        if (breast_pred[0] == 0):
          bc = 'The Breast cancer is Malignant'
        else:
          bc = 'The Breast Cancer is Benign '
        
    st.success(bc)