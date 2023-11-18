from openai import OpenAI 
import streamlit as st


with st.sidebar:
    openai_model=st.radio('Pick your open ai model',("gpt-3.5-turbo","gpt-4", "gpt-4-1106-preview"))
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
client = OpenAI(
    api_key = openai_api_key
)
st.markdown('''
[![Account](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/marco-baldan)
''', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.title('Open AI')

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()


    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=openai_model, messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)