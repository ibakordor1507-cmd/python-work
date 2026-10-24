import streamlit as st

# Set page layout and title
st.set_page_config(page_title="Python helper", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Quiz Hub")
st.write("Welcome! This simple tool helps you review concepts and test your knowledge.")

# Sidebar navigation 
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Introduction to python & Data Types",  # Updated title
        "Unit II: Control & Logic",
        "Unit III: Functions & Data Structures",
        "Interactive Syllabus Quiz"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Tip: Select a topic above to practice syllabus concepts.")

# ---------------------------------------------------------
# UNIT I: Introduction & Data Types
# Concepts: Intro to Python, Variables, Data Types
# ---------------------------------------------------------
if choice == "Unit I: Introduction & Data Types":
    st.header("Unit I: Introduction & Data Types")
    st.write("Welcome to Python! Learn what Python is and explore how variables and data types work.")

    st.subheader("1. What is Python?")
    st.write(
        "Python is a popular, high-level programming language known for its simplicity and readability. "
        "It uses dynamic typing, meaning you don't have to declare a variable's type explicitly before using it."
    )