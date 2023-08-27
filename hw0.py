import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("Vandy Info")

# Initialize state variables
website_link = st.text_input("Enter the website link")
website_content_string = ""
summary = ""

# Load the website content as a Document from the provided link
def load_website_content(website_link):
    from langchain.document_loaders import WebBaseLoader
    loader = WebBaseLoader(website_link)
    docs = loader.load()
    return docs

# Generate a summary of the information about Vanderbilt University from the website content
def universitySummaryGenerator(website_content_string):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are an AI assistant tasked with generating a summary of the information about Vanderbilt University from the {website_content_string}."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please generate a summary of the information about Vanderbilt University based on the provided {website_content_string}."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(website_content_string=website_content_string)
    return result # returns string   

# Get input from the user
if st.button("Submit"):
    if website_link:
        website_content = load_website_content(website_link)
        website_content_string = "".join([doc.page_content for doc in website_content])
        if website_content_string:
            summary = universitySummaryGenerator(website_content_string)

# Display the summary of the information about Vanderbilt University to the user
st.markdown(summary)