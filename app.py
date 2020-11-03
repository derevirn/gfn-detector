import streamlit as st
import matplotlib.pyplot as plt
import spacy
from spacy.lang.el.stop_words import STOP_WORDS
from wordcloud import WordCloud
from utils import get_page_text

@st.cache(allow_output_mutation=True)
def get_nlp_model(path):   
    return spacy.load(path)

def run_app(select_input):
    if select_input == "URL":
        url = st.text_input("URL")   
        if st.button("Run"):
            text = get_page_text(url)
            
            if nlp(text).cats['FAKE'] > nlp(text).cats['REAL']:
                st.markdown("# <span style='color:red'>Fake news!</span>",
                            unsafe_allow_html=True)
            else:
                st.markdown("## <span style='color:green'>Η είδηση είναι αληθής!<br>  \
                            This news article is real!</span>",
                            unsafe_allow_html=True)
                    
            st.markdown(text)        
                
            wc = WordCloud(width = 1000, height = 700,
                           random_state = 1, background_color = 'white',
                           stopwords = STOP_WORDS).generate(text) 
            
            fig, ax = plt.subplots()
            ax.imshow(wc)
            ax.axis('off')
            st.pyplot(fig)
            
            print(nlp(text).cats)           
    else:
        text = st.text_area("Text", height=300)
        if st.button("Run"):
            print(nlp(text))
            print(nlp(text).cats)

nlp = get_nlp_model('model')

st.title("Greek Fake News Detector")
st.subheader("Είσαγετε τη Διεύθυνση URL ή το Κείμενο μίας Είδησης")


select_input = st.radio("Select Input:", ["URL", "Text"])

if select_input == "URL":
    run_app(select_input)
    
else:
    run_app(select_input)

