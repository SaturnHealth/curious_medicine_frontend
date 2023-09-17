import streamlit as st
import requests
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")

URL = config_object["BACKEND"]["URL"]

def main():
    st.title("Curious Medicine")
    st.header("Ask a question about your medicines")
    st.subheader("How to use ?")
    st.write("You can ask questions like 'How does Adderall work ?' or 'What medicines should I consume for headaches ?'")
    st.divider()
    try:
        query = st.text_input("Enter your query: ")
        params = {"question" : query}
        answers = requests.post(url=URL, params=params)
        st.write(answers.json()["response"])
    except Exception as e:
        print(e)
    
    st.divider()
    st.subheader("WARNING")
    st.write("This is powered by ChatGPT. Additionally, Generative AI is known for hallucinations and create falsible information")
    st.write(" Please be careful. Consult a medical professional before taking any steps ")
    st.write("Email vivek.rm17@gmail.com for doubts and queries")
    
    
if __name__ == "__main__" :
    main()