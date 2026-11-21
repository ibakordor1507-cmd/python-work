import streamlit as st
import numpy as np
import io
import contextlib

# Set page layout and title
st.set_page_config(page_title="Python Helper", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Coding Lab")
st.write("Welcome! Learn Python theory, inspect examples, and practice writing code.")

# Sidebar navigation 
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
st.sidebar.info("Tip: Select a unit above to explore interactive syllabus concepts and coding exercises.")

# ---------------------------------------------------------
# UNIT I: Introduction & Data Types
# ---------------------------------------------------------
if choice == "Unit I: Introduction & Data Types":
    st.header("Unit I: Introduction & Data Types")

    # 1. Definition of Python
    st.subheader("1. What is Python?")
    st.write(
        "**Python** is a high-level, interpreted, general-purpose programming language known for its clean, "
        "English-like syntax and readability. It uses **dynamic typing**, meaning you do not need to declare "
        "a variable's data type explicitly—Python automatically determines it at runtime."
    )

    st.markdown("---")

    # 2. Data Types Theory Grouped into 3 Categories
    st.subheader("2. Python Data Types Classification")
    tab1, tab2, tab3 = st.tabs([
        "Basic Data Types", 
        "Collection Data Types", 
        "Other Data Types"
    ])

    with tab1:
        st.markdown("#### Basic (Primitive) Python Data Types")
        st.markdown("""
        * **String (`str`):** An immutable sequence of Unicode characters enclosed in single, double, or triple quotes (e.g., `"Hello"`).
        * **Integer (`int`):** Whole numbers—positive, negative, or zero—without a fractional or decimal part (e.g., `42`, `-7`).
        * **Float (`float`):** Real numbers written with a decimal point or scientific notation (e.g., `3.14`, `-0.05`).
        * **Boolean (`bool`):** Represents truth values and can only be `True` or `False`.
        * **Complex (`complex`):** Numbers with a real and an imaginary part written as `a + bj`, where `j` is the imaginary unit (e.g., `3 + 4j`).
        """)
        st.code(
            'name = "Python"      # str\n'
            'age = 18             # int\n'
            'price = 99.95        # float\n'
            'is_active = True     # bool\n'
            'z = 2 + 3j           # complex',
            language="python"
        )

    with tab2:
        st.markdown("#### Collection Data Types")
        st.markdown("""
        * **List (`list`):** An ordered, mutable (changeable) collection that allows duplicate elements, written with square brackets `[]`.
        * **Tuple (`tuple`):** An ordered, immutable (unchangeable) collection that allows duplicate elements, written with parentheses `()`.
        * **Set (`set`):** An unordered, mutable collection of unique elements (automatically removes duplicates), written with curly braces `{}`.
        * **Dictionary (`dict`):** An ordered (Python 3.7+), mutable collection of `key: value` pairs with unique keys, written with curly braces `{}`.
        """)
        st.code(
            'my_list = [10, 20, 20, 30]              # list\n'
            'my_tuple = ("apple", "banana")          # tuple\n'
            'my_set = {1, 2, 3, 3}                   # set -> {1, 2, 3}\n'
            'student = {"name": "Asha", "year": 1}   # dict',
            language="python"
        )

    with tab3:
        st.markdown("#### Other Built-in Data Types")
        st.markdown("""
        * **NoneType (`None`):** Represents the intentional absence of a value or a null object.
        * **Range (`range`):** Represents an immutable sequence of numbers commonly used for looping a specific number of times (e.g., `range(5)`).
        * **Bytes (`bytes`):** An immutable sequence of single bytes (integers from `0` to `255`), prefixed with `b` (e.g., `b"hello"`).
        * **Bytearray (`bytearray`):** A mutable counterpart to `bytes` whose individual byte values can be modified in place.
        """)
        st.code(
            'empty_val = None                  # NoneType\n'
            'nums = range(1, 6)                # range (1 to 5)\n'
            'raw_data = b"ABC"                 # bytes (immutable)\n'
            'mutable_data = bytearray(b"ABC")  # bytearray (mutable)',
            language="python"
        )

    st.markdown("---")

    # 3. Interactive Data Type Explorer (with live code preview)
    st.subheader("3. Interactive Data Type Explorer")
    col1, col2 = st.columns(2)

    with col1:
        user_str = st.text_input("Enter text (String):", value="Hello Python!")
        user_int = st.number_input("Enter a whole number (Integer):", value=42, step=1)
        user_float = st.number_input("Enter a decimal (Float):", value=3.14, step=0.1)
        user_bool = st.checkbox("Toggle for Boolean (True/False)", value=True)
        user_complex = st.text_input("Enter a complex number (e.g., 2+3j):", value="2+3j")

    with col2:
        st.write("**Live Python Code & `type()` Output:**")
        try:
            parsed_complex = complex(user_complex)
            complex_line = f"type({parsed_complex}) -> {type(parsed_complex).__name__}"
        except ValueError:
            complex_line = f"# Invalid complex format: {repr(user_complex)} (use format like 2+3j)"

        st.code(
            f"type({repr(user_str)}) -> {type(user_str).__name__}\n"
            f"type({user_int}) -> {type(user_int).__name__}\n"
            f"type({user_float}) -> {type(user_float).__name__}\n"
            f"type({user_bool}) -> {type(user_bool).__name__}\n"
            f"{complex_line}",
            language="python"
        )

    st.markdown("---")

    # 4. Unit I Hands-On Coding Exercise
    st.subheader("4. 💻 Unit I Coding Exercise: Practice Data Types")
    st.write(
        "**Task:** Create one variable for a `complex` number, one `list`, and one `dict`, "
        "then print each variable along with its `type()`."
    )

    starter_code_u1 = (
        "# 1. Create a complex number, a list, and a dictionary\n"
        "c_num = 4 + 5j\n"
        "subjects = ['Law', 'Python', 'Statistics']\n"
        "profile = {'course': 'B.Sc. LL.B.', 'year': 1}\n\n"
        "# 2. Print their data types using type()\n"
        "print('Complex:', type(c_num))\n"
        "print('List:', type(subjects))\n"
        "print('Dictionary:', type(profile))\n"
    )

    u1_code = st.text_area("Write and edit your Unit I Python code below:", value=starter_code_u1, height=210, key="u1_editor")

    if st.button("▶ Run Unit I Code"):
        output_buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(output_buffer):
                exec(u1_code, {})
            result = output_buffer.getvalue()
            st.success("Executed Successfully!")
            st.code(result if result else "(No output printed — use print() to see results)", language="text")
        except Exception as e:
            st.error(f"{type(e).__name__}: {e}")