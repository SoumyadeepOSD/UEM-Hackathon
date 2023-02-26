# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 19:10:45 2023

@author: user
"""



import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
from PIL import Image

#loading the saved models

diabetes_model = pickle.load(open('C:/Users/user/trained_model_diabetes.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/user/trained_model_heart.sav', 'rb'))


#sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Our Services', 
                           ['Diabetes Prediction', 
                            'Heart Disease Prediction',
                            'Personal Health Assistant',
                            'General Guidance',
                            'Food Donation',
                            ],
                           
                           icons = ['activity', 
                                    'heart', 
                                    'robot', 
                                    'bandaid fill',
                                    'egg'],
                           default_index=0)
    
    
    
    
    





def diabetes_prediction(input_data):

     ## Changing the data into the numpy array
    input_data_as_numpy_array = np.asarray(input_data)
     
     #reshaping the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
     
    prediction = diabetes_model.predict(input_data_reshaped)
     
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic!! Go to Personal Health Assistant'
     
     
     #Giving the title
def DFunc():
    st.title(':blue[HEALTH MANAGER]')
    st.subheader(':violet[Diabetes Prediction WebApp]')
     
     #Getting the input data from the user
    Pregnancies = st.text_input('Number of pregnencies')
     
    Glucose = st.text_input('Amount of Glucose')
     
    BloodPressure = st.text_input('Amount of BloodPressure')
     
    SkinThickness = st.text_input('Amount of SkinThickness')
     
    Insulin = st.text_input('Amount of Insulin')
     
    BMI = st.text_input('Amount of BMI')
     
    DiabetesPedigreeFunction = st.text_input('Amount of DiabetesPedigreeFunction')
     
    Age = st.text_input('Amount of Age')
 
 
 
     # Code for Prediction
    diagnosis = ''
 
     # Creating a button for Prediction
    if st.button('Diabetes test Result'):
        diagnosis = diabetes_prediction([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
     
    st.success(diagnosis)
    
#if selected == 'Diabetes Prediction':
    #creating a function for prediction
    







######## For Heart Disease Prediction ###############









def heart_prediction(input_data):

    ## Changing the data into the numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshaping the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    prediction = heart_model.predict(input_data_reshaped)
    
    if (prediction[0] == 0):
        return 'Thee is no Problem in heart'
    else:
        return 'There is a problem in heart! Go to Personal Health Assistant'

    
def HFunc():
    st.title(':blue[HEALTH MANAGER]')
    st.subheader(':violet[Heart Disease Prediction WebApp]')
    
    #Getting the input data from the user
    age = st.text_input('Enter your age')
    
    sex = st.text_input('Enter your Gender')
    
    cp = st.text_input('Chest pain type')
    
    trestbps = st.text_input('Resting blood pressure')
    
    chol = st.text_input('Serum cholestoral in mg/dl')
    
    fbs = st.text_input('Fasting blood sugar')
    
    restecg = st.text_input('Resting electrocardiographic results')
    
    thalach = st.text_input('Maximum heart rate achieved')
    
    exang = st.text_input('Exercise induced angina')
    
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    
    slope = st.text_input('Solpe of the peak exercise ST segment')
    
    ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    
    thal = st.text_input('Enter the amount of thal [that:0(normal), thal:1(fixed defect), thal:2(reversable defect)]')


    # Code for Prediction
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease test Result'):
        diagnosis = diabetes_prediction([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
    st.success(diagnosis)




def AIChat():
    url = 'https://tourmaline-lolly-da56d6.netlify.app/'
    st.header('Contact with your personal Health Assistant Here🤖')
    if st.button('Guidance from Bot'):
        webbrowser.open_new_tab(url)
    st.subheader(':violet[This will open it new page]')





def Donation():
    video_file = open('myvideo.webm', 'rb')
    video_bytes = video_file.read()
    st.header('Current health scenario According to WHO')
    st.video(video_bytes)
    image = Image.open('myimage.png')
    st.subheader(":orange[Checkout the govt. site for more detail]")
    st.image(image, caption='Govt. of India Helpline site')
    st.subheader('If you want to donate your food or can help orphans/poors with any kind of help please submit your information to us we will reach out to you')
    st.text_input('Name')
    st.text_input('Address')
    st.text_input('Blood Group(for blood donation)')
    st.text_input('Location')
    st.text_input('Your contact number')
    st.text_area('How can you contribute?')
    if st.button('Submit'):
        st.success("You have successfully submitted the form. Thankyou visit again✔️")
    
    
    
def General():
    image = Image.open('mysuggestion.png')
    st.image(image, caption="Govt. help line number")
    image = Image.open('guide.png')
    st.image(image, caption="General Suggestions from WHO")
    st.text_area('Have any suggestions? Fill here')
    st.text_input('Enter your mail')
    if st.button('Submit'):
        st.success("You have successfully submitted the form. Thankyou visit again✔️")
    
    
if (__name__=="__main__"):
    if selected == 'Diabetes Prediction':
        DFunc()
    elif selected == 'Personal Health Assistant':
        AIChat()
    elif selected == 'Food Donation':
        Donation()
    elif selected == 'General Guidance':
        General()
    else:
        HFunc()






    