import streamlit as st
import spacy
from utils import get_page_text

@st.cache(allow_output_mutation=True)
def get_nlp_model(path):   
    return spacy.load(path)

def run_app(select_input):
    if select_input == "URL":
        url = st.text_input("URL")   
        if st.button("Run"):
            text = get_page_text(url)
            print(nlp(text))
            print(nlp(text).cats)           
    else:
        text = st.text_area("Text", height=300)
        if st.button("Run"):
            print(nlp(text))
            print(nlp(text).cats)

nlp = get_nlp_model('model')

select_input = st.radio("Select Input:", ["URL", "Text"])

if select_input == "URL":
    run_app(select_input)
    
else:
    run_app(select_input)

