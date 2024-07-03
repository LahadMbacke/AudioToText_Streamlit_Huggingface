# pip install accelerate
from pathlib import Path
import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel

import torch

token_path = Path("token.txt")
token = token_path.read_text().strip()

def page_text_generation():

    st.markdown("<h1 style='text-align: center; color: red;'>Text Generation</h1>", unsafe_allow_html=True)
    st.markdown("---------------")

    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    text = st.text_area("Enter the text you want to generate")


    encoded_input = tokenizer.encode(text, return_tensors='pt')
    output = model.generate(encoded_input, max_length=50, num_return_sequences=1)
    decoded_string = tokenizer.decode(output[0], skip_special_tokens=True)


    st.write(decoded_string)