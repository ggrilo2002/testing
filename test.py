import streamlit as st
from streamlit_chunk_file_uploader import uploader

file = uploader("uploader", key="chunk_uploader", chunk_size=32)