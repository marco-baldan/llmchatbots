import streamlit as st

with st.sidebar:
    "[Sign up to Hugging face](https://huggingface.co/join)"
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/marco-baldan/llmchatbots)"
st.markdown('''
[![Account](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/marco-baldan)
''', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.title("LLM Chatbots")
st.caption("🚀 A streamlit application with various different chatbots")
