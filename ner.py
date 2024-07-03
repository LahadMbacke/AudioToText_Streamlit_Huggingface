import streamlit as st

from transformers import AutoTokenizer, AutoModelForTokenClassification

tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner")
model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner")
from transformers import pipeline


st.markdown("<h1 style='text-align: center; color: red;'>Named Entity Recognition</h1>", unsafe_allow_html=True)
st.markdown("---------------")


def page_ner():
    result = []
    text = st.text_area("Enter the text you want to generate")
    if st.button("Generate Token"):
        nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")
        result = nlp(text)
        
        result  = [f"{item['word']} {item['entity_group']} " for item in result]
        st.write(" ".join(result))
