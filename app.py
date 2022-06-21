import streamlit as st
import matplotlib.pyplot as plt
import spacy
from spacy.lang.el.stop_words import STOP_WORDS
from wordcloud import WordCloud
from utils import get_page_text

st.set_page_config(page_title = "Greek Fake News Detector")

@st.cache(allow_output_mutation=True)
def get_nlp_model(path):   
    return spacy.load(path)

def generate_output(text):
     cats = nlp(text).cats
     if cats['FAKE'] > cats['REAL']:
         st.markdown("<h1><span style='color:red'>This is a fake news article!</span></h1>",
                     unsafe_allow_html=True)
     else:
         st.markdown("<h1><span style='color:green'>This is a real news article!</span></h1>",
                     unsafe_allow_html=True)
             
     q_text = '> '.join(text.splitlines(True))   
     q_text = '> ' + q_text
     st.markdown(q_text)

     wc = WordCloud(width = 1000, height = 600,
                    random_state = 1, background_color = 'white',
                    stopwords = STOP_WORDS).generate(text) 
     
     fig, ax = plt.subplots()
     ax.imshow(wc)
     ax.axis('off')
     st.pyplot(fig)
     print(cats)

nlp = get_nlp_model('model')

desc = "This web app detects fake news written in the Greek language.\
        You can either enter the URL of a news article, or paste the text directly (works better).\
        This app was developed with the Streamlit and spacy Python libraries.\
        The Github repository of the app is available [here](https://github.com/derevirn/gfn-detector).\
        Feel free to contact me on [LinkedIn](https://www.linkedin.com/in/giannis-tolios-0020b067/)\
        or via [e-mail](mailto:info@giannis.io)."

st.title("Greek Fake News Detector")
st.markdown(desc)
st.subheader("Enter the URL address/text of a news article written in Greek")
select_input = st.radio("Select Input:", ["URL", "Text"])

if select_input == "URL":
    url = st.text_input("URL")   
    if st.button("Run"):
        text = get_page_text(url)
        generate_output(text)  

else:
    text = st.text_area("Text", height=300)
    if st.button("Run"):
        generate_output(text) 

