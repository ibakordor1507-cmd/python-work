import streamlit as st
import numpy as np
import io
import contextlib
# 1. Page configuration (must be first Streamlit command)
st.set_page_config(page_title="Python Helper", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Quiz Hub")
st.write("Welcome! This tool helps you review concepts and test your knowledge")

# 2. Define 'choice' in the sidebar BEFORE using 'if choice == ...'
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Introduction & Data Types",
        "Unit II: Control & Logic",
        "Unit III: Functions, Scope & Recursion",
        "Unit IV: Introduction to NumPy",
        "Interactive Syllabus Quiz"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Tip: Select a unit above to explore interactive syllabus concepts.")

# Helper function to display Definition + Example + Interactive Code Box cleanly
def learn_and_code(title, definition, example_code, starter_code, key_id):
    with st.expander(f"📘 {title}", expanded=False):
        st.write(definition)
        st.markdown("**Example:**")
        st.code(example_code, language="python")
        
        st.markdown("**💻 Try Coding It Yourself:**")
        user_code = st.text_area("Edit and run code:", value=starter_code, height=110, key=f"code_{key_id}")
        if st.button("▶ Run Code", key=f"btn_{key_id}"):
            output_buffer = io.StringIO()
            try:
                with contextlib.redirect_stdout(output_buffer):
                    exec(user_code, {})
                res = output_buffer.getvalue()
                st.code(res if res else "(Executed with no print output)", language="text")
            except Exception as e:
                st.error(f"{type(e).__name__}: {e}")

# ---------------------------------------------------------
# UNIT I: Introduction & Data Types
# ---------------------------------------------------------
if choice == "Unit I: Introduction & Data Types":
    st.header("Unit I: Introduction & Data Types")

    # 1. Definition of Python
    st.subheader("1. What is Python?")
    st.write(
        "**Python** is a high-level, interpreted, general-purpose programming language known for its simple, "
        "English-like syntax. It uses **dynamic typing**, meaning you don't have to declare a variable's data type "
        "before using it—Python detects it automatically."
    )

    st.markdown("---")

    # 2. Grouped Data Types (Theory + Coding inside each one)
    st.subheader("2. Python Data Types (Click any type to learn & code)")
    tab1, tab2, tab3 = st.tabs([
        "Basic Data Types", 
        "Collection Data Types", 
        "Other Data Types"
    ])

    # --- TAB 1: BASIC DATA TYPES ---
    with tab1:
        learn_and_code(
            "String (str)",
            "An immutable sequence of characters enclosed in single (`' '`), double (`\" \"`), or triple quotes.",
            'msg = "Hello, Python!"\nprint(msg)\nprint(type(msg))',
            'text = "I am learning Python"\nprint(text)\nprint("Type:", type(text))',
            "str"
        )
        learn_and_code(
            "Integer (int)",
            "Whole numbers (positive, negative, or zero) without any decimal point.",
            'age = 18\nprint(age + 2)\nprint(type(age))',
            'num = 25\nprint("Double:", num * 2)\nprint("Type:", type(num))',
            "int"
        )
        learn_and_code(
            "Float (float)",
            "Real numbers that contain a decimal point or use scientific notation.",
            'pi = 3.14\nprint(pi * 2)\nprint(type(pi))',
            'price = 49.99\nprint("With tax:", price + 5.0)\nprint("Type:", type(price))',
            "float"
        )
        learn_and_code(
            "Boolean (bool)",
            "Represents logical truth values and can only be `True` or `False`.",
            'is_student = True\nprint(is_student)\nprint(type(is_student))',
            'is_ready = True\nprint("Is 10 > 5?", 10 > 5)\nprint("Type:", type(is_ready))',
            "bool"
        )
        learn_and_code(
            "Complex (complex)",
            "Numbers with a real and an imaginary part written as `a + bj` (where `j` is the imaginary unit).",
            'z = 3 + 4j\nprint("Real:", z.real, "Imaginary:", z.imag)\nprint(type(z))',
            'c = 2 + 5j\nprint("Complex number:", c)\nprint("Type:", type(c))',
            "complex"
        )

    # --- TAB 2: COLLECTION DATA TYPES ---
    with tab2:
        learn_and_code(
            "List (list)",
            "An ordered, mutable (changeable) collection that allows duplicate items, written with square brackets `[]`.",
            'fruits = ["apple", "banana", "apple"]\nfruits.append("cherry")\nprint(fruits)',
            'subjects = ["Law", "Python", "Stats"]\nsubjects.append("Economics")\nprint(subjects)\nprint(type(subjects))',
            "list"
        )
        learn_and_code(
            "Tuple (tuple)",
            "An ordered, immutable (unchangeable) collection that allows duplicates, written with parentheses `()`.",
            'coords = (10, 20)\nprint(coords[0])\nprint(type(coords))',
            'colors = ("red", "green", "blue")\nprint("First color:", colors[0])\nprint(type(colors))',
            "tuple"
        )
        learn_and_code(
            "Set (set)",
            "An unordered, mutable collection of unique items (automatically removes duplicates), written with `{}`.",
            'nums = {1, 2, 2, 3}\nprint(nums)  # Output: {1, 2, 3}',
            'unique_ids = {101, 102, 102, 103}\nprint("Unique set:", unique_ids)\nprint(type(unique_ids))',
            "set"
        )
        learn_and_code(
            "Dictionary (dict)",
            "An ordered (Python 3.7+), mutable collection of `key: value` pairs with unique keys, written with `{}`.",
            'student = {"name": "Riya", "age": 18}\nprint(student["name"])',
            'book = {"title": "Python 101", "pages": 250}\nprint("Title:", book["title"])\nprint(type(book))',
            "dict"
        )

    # --- TAB 3: OTHER DATA TYPES ---
    with tab3:
        learn_and_code(
            "NoneType (None)",
            "Represents the intentional absence of a value or a null object.",
            'result = None\nprint(result)\nprint(type(result))',
            'data = None\nprint("Value:", data)\nprint(type(data))',
            "none"
        )
        learn_and_code(
            "Range (range)",
            "Represents an immutable sequence of numbers, commonly used in loops.",
            'r = range(1, 5)\nprint(list(r))  # [1, 2, 3, 4]',
            'nums = range(0, 10, 2)\nprint("Even numbers:", list(nums))\nprint(type(nums))',
            "range"
        )
        learn_and_code(
            "Bytes (bytes)",
            "An immutable sequence of single bytes (integers 0–255), prefixed with `b`.",
            'b_data = b"Hello"\nprint(b_data)\nprint(type(b_data))',
            'raw = b"Python"\nprint("First byte ASCII:", raw[0])\nprint(type(raw))',
            "bytes"
        )
        learn_and_code(
            "Bytearray (bytearray)",
            "A mutable sequence of bytes whose individual byte values can be modified.",
            'ba = bytearray(b"ABC")\nba[0] = 90  # ASCII for Z\nprint(ba)',
            'ba = bytearray(b"cat")\nba[0] = 98  # ASCII for b\nprint("Modified:", ba)\nprint(type(ba))',
            "bytearray"