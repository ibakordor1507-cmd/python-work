import streamlit as st

#Set page layout and page title
st.set_page_config(page_title="Python Learning Program",page_icon="🐍",layout = "wide")
st.title("Python Study Comapanion")
st.write("Hello user, this is a website that helps you learn python")

#sidebar navigation 
st.sidebar.header("Navigation")
choice = st.sidebar.radio("Choose a module:","Unit 1: Intro to python","Unit 2: The different types of operators","Unit 3: Control  and logic","Unit 4: Functions")
#________________________________________________
#Unit 1: Introduction to Python
#Concepts: Input/Output,Variables,Data types
#________________________________________________
if choice == "Unit 1 : Intro to python":
    st.header("Unit 1: Intro to python")
    st.write("Welcome to python!Let us learn what python is about and see how variables work and the different data types")
    st.subheader("1. What is Python?")
    st.write(
        "Python is a popular, high-level programming language known for its simplicity and readability. "
        "It uses dynamic typing, meaning you don't have to declare a variable's type explicitly before using it."
    )
