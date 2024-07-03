# pip install accelerate
from pathlib import Path
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

token_path = Path("token.txt")
token = token_path.read_text().strip()

st.markdown("<h1 style='text-align: center; color: red;'>Text Generation</h1>", unsafe_allow_html=True)
st.markdown("---------------")

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b-it")
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-9b-it",
    device_map="auto",
    torch_dtype=torch.bfloat16
)

input_text = st.text_area("Enter your text here", "Write me a poem about Machine Learning.")
input_ids = tokenizer(input_text, return_tensors="pt").to("cpu")

outputs = model.generate(**input_ids)

st.write(tokenizer.decode(outputs[0]))
