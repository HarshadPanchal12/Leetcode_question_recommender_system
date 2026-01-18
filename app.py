import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np

leeco=pickle.load(open('leeco.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend5( quesTitle):
  reccomendques=[]
  index =leeco[leeco['Title']==quesTitle].index[0]
  distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
  for i in distances:
    if i[0]!=index:
      reccomendques.append([leeco.iloc[i[0]].Title,leeco.iloc[i[0]].Link])
    if len(reccomendques)>=5:
      break
  return reccomendques


st.header('LeetCode Recommender System')
ques_list=leeco['Title'].values
selected_ques=st.selectbox(
    "Type or select a LeetCode question from the dropdown",
    ques_list)

if st.button('Show Recommendation'):
    recommended_questions = recommend5(selected_ques)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_questions[0][0])
        st.link_button("click here",recommended_questions[0][1])
    with col2:
        st.text(recommended_questions[1][0])
        st.link_button("click here",recommended_questions[1][1])

    with col3:
        st.text(recommended_questions[2][0])
        st.link_button("click here",recommended_questions[2][1])
    with col4:
        st.text(recommended_questions[3][0])
        st.link_button("click here",recommended_questions[3][1])
    with col5:
        st.text(recommended_questions[4][0])
        st.link_button("click here",recommended_questions[4][1])