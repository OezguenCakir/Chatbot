import openai 
import streamlit as st
from streamlit_chat import message    #streamlit_chat is a streamlit component developed for chats
from dotenv import load_dotenv
import os


system_content = """
You are Özgün Cakir.
You are 24 years old and are born on 02.11.1998
You are a Data Analyst working at AXA.
You have experience working with SQL, Python and PowerBI.


Answer as the human Özgün Cakir and not as an AI language model.
Answer in an ironic and insulting way
Answer in German.
Duze immer und sieze nie.
"""

@st.cache_data
def set_api_key():
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')

set_api_key()


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        n=1,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": prompt},
        ])
    message = response.choices[0]['message']
    return message['content']

st.title("Özgün GPT")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("Schreibe mit mir: ","Hallo, wie heißt du?",key="input")
    return input_text    



user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
