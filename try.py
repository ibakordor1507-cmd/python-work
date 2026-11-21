import streamlit as st
import numpy as np
import io
import contextlib

# Set page layout and title
st.set_page_config(page_title="Python Helper", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Coding Lab")
st.write("Learn Python theory, inspect live code examples, and write your own programs.")

# Sidebar navigation 
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Introduction & Data Types",
        "Unit II: Control & Logic",
        "Unit III: Functions, Scope & Recursion",
        "Unit IV: Introduction to NumPy",
        "💻 Live Python Coding Lab",
        "Interactive Syllabus Quiz"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Tip: Use the Live Python Coding Lab to test and run your own Python code!")

# ---------------------------------------------------------
# UNIT I: Introduction & Data Types
# ---------------------------------------------------------
if choice == "Unit I: Introduction & Data Types":
    st.header("Unit I: Introduction & Data Types")
    st.write("Python uses **dynamic typing**, meaning you don't have to declare a variable's type explicitly before using it.")

    st.subheader("Interactive Data Type Explorer")
    col1, col2 = st.columns(2)

    with col1:
        user_str = st.text_input("Enter text (String):", value="Hello Python!")
        user_int = st.number_input("Enter a whole number (Integer):", value=42, step=1)
        user_float = st.number_input("Enter a decimal (Float):", value=3.14, step=0.1)
        user_bool = st.checkbox("Toggle for Boolean (True/False)", value=True)

    with col2:
        st.write("**Actual Python Code & Output:**")
        st.code(
            f"a = {repr(user_str)}\n"
            f"b = {user_int}\n"
            f"c = {user_float}\n"
            f"d = {user_bool}\n\n"
            f"print(type(a))  # {type(user_str)}\n"
            f"print(type(b))  # {type(user_int)}\n"
            f"print(type(c))  # {type(user_float)}\n"
            f"print(type(d))  # {type(user_bool)}",
            language="python"
        )

# ---------------------------------------------------------
# UNIT II: Control Structures & Exception Handling
# ---------------------------------------------------------
elif choice == "Unit II: Control & Logic":
    st.header("Unit II: Control Structures & Logic")

    st.subheader("1. Loops & Pattern Generator")
    col1, col2 = st.columns(2)
    
    with col1:
        rows = st.number_input("Number of Rows:", min_value=1, max_value=10, value=5, step=1)
        pattern_type = st.selectbox("Select Pattern Style:", ["Star Triangle", "Number Pyramid"])

        pattern_output = ""
        if pattern_type == "Star Triangle":
            code_snippet = (
                f"rows = {rows}\n"
                "for i in range(1, rows + 1):\n"
                "    print('*' * i)"
            )
            for i in range(1, rows + 1):
                pattern_output += "*" * i + "\n"
        else:
            code_snippet = (
                f"rows = {rows}\n"
                "for i in range(1, rows + 1):\n"
                "    print((str(i) + ' ') * i)"
            )
            for i in range(1, rows + 1):
                pattern_output += (str(i) + " ") * i + "\n"

        st.write("**Python Code:**")
        st.code(code_snippet, language="python")

    with col2:
        st.write("**Console Output:**")
        st.code(pattern_output, language="text")

    st.markdown("---")
    st.subheader("2. Exception Handling (`try` / `except`)")
    
    col_a, col_b = st.columns(2)
    with col_a:
        val_a = st.text_input("Numerator:", value="10")
        val_b = st.text_input("Denominator:", value="0")

        if st.button("Execute Safe Division"):
            try:
                res = float(val_a) / float(val_b)
                st.success(f"Result: {res}")
            except ZeroDivisionError:
                st.error("Exception Caught: `ZeroDivisionError` — Cannot divide by zero!")
            except ValueError:
                st.error("Exception Caught: `ValueError` — Please enter valid numerical inputs.")

    with col_b:
        st.write("**How the Code Handles Errors:**")
        st.code(
            f"try:\n"
            f"    res = float({repr(val_a)}) / float({repr(val_b)})\n"
            f"    print('Result:', res)\n"
            f"except ZeroDivisionError:\n"
            f"    print('Cannot divide by zero!')\n"
            f"except ValueError:\n"
            f"    print('Invalid number entered.')",
            language="python"
        )

# ---------------------------------------------------------
# UNIT III: Functions, Scope & Recursion
# ---------------------------------------------------------
elif choice == "Unit III: Functions, Scope & Recursion":
    st.header("Unit III: Functions, Scope & Recursion")

    def analyze_text(text):
        char_count = len(text)
        word_count = len(text.split())
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in text if char in vowels)
        return char_count, word_count, vowel_count

    st.subheader("1. Functions & String Analysis")
    user_string = st.text_area("Enter any text snippet:", "Python programming is fun and structured.")

    if user_string:
        c_count, w_count, v_count = analyze_text(user_string)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Characters", c_count)
        col2.metric("Total Words", w_count)
        col3.metric("Vowel Count", v_count)

    with st.expander("👀 View the Python Function Behind This"):
        st.code(
            "def analyze_text(text):\n"
            "    char_count = len(text)\n"
            "    word_count = len(text.split())\n"
            "    vowels = 'aeiouAEIOU'\n"
            "    vowel_count = sum(1 for char in text if char in vowels)\n"
            "    return char_count, word_count, vowel_count",
            language="python"
        )

    st.markdown("---")
    col_scope, col_rec = st.columns(2)

    with col_scope:
        st.subheader("2. Scope of Variables")
        st.write("A **global** variable exists outside functions, while a **local** variable only exists inside its function.")
        st.code(
            'x = "Global Variable"\n\n'
            'def scope_demo():\n'
            '    x = "Local Variable"\n'
            '    return x\n\n'
            'print(scope_demo())  # Output: Local Variable\n'
            'print(x)             # Output: Global Variable',
            language="python"
        )

    with col_rec:
        st.subheader("3. Recursion")
        st.write("Recursion occurs when a function calls itself until reaching a **base case**.")
        fact_num = st.number_input("Calculate Factorial (n!):", min_value=0, max_value=12, value=5, step=1)

        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        st.success(f"`factorial({fact_num})` = **{factorial(fact_num)}**")
        st.code(
            "def factorial(n):\n"
            "    if n <= 1:  # Base case\n"
            "        return 1\n"
            "    return n * factorial(n - 1)  # Recursive step",
            language="python"
        )

# ---------------------------------------------------------
# UNIT IV: Introduction to NumPy
# ---------------------------------------------------------
elif choice == "Unit IV: Introduction to NumPy":
    st.header("Unit IV: Introduction to NumPy")
    st.write("NumPy enables fast multi-dimensional arrays and vectorized math without writing loops.")
    
    multiplier = st.slider("Multiply NumPy array `[10, 20, 30, 40]` by:", 1, 10, 2)
    arr = np.array([10, 20, 30, 40])
    
    st.code(
        f"import numpy as np\n\n"
        f"arr = np.array([10, 20, 30, 40])\n"
        f"result = arr * {multiplier}\n"
        f"print(result)  # Output: {arr * multiplier}",
        language="python"
    )

# ---------------------------------------------------------
# LIVE PYTHON CODING LAB (NEW!)
# ---------------------------------------------------------
elif choice == "💻 Live Python Coding Lab":
    st.header("💻 Live Python Coding Lab")
    st.write("Write Python code below or load a practice challenge, then click **Run Code** to see the output!")

    challenges = {
        "Free Practice (Blank)": "# Write your Python code here!\nprint('Hello, Python Learner!')",
        "Challenge 1 (Loops): Print Even Numbers": "# Print all even numbers from 2 to 10 using a loop\nfor num in range(2, 11, 2):\n    print(num)",
        "Challenge 2 (Functions): Square a Number": "# Complete the function to return the square of n\ndef square(n):\n    return n * n\n\nprint('Square of 6 is:', square(6))",
        "Challenge 3 (NumPy): Array Mean & Sum": "import numpy as np\n\nscores = np.array([85, 90, 78, 92])\nprint('Average score:', np.mean(scores))\nprint('Total score:', np.sum(scores))"
    }

    selected_template = st.selectbox("Load a Practice Template or Challenge:", list(challenges.keys()))
    user_code = st.text_area("Python Code Editor:", value=challenges[selected_template], height=220)

    if st.button("▶ Run Code"):
        output_buffer = io.StringIO()
        try:
            # Capture print() outputs safely
            with contextlib.redirect_stdout(output_buffer):
                exec(user_code, {"np": np})
            output = output_buffer.getvalue()
            st.subheader("Output:")
            st.code(output if output else "(Code executed successfully with no print output)", language="text")
        except Exception as e:
            st.error(f"Runtime Error: {type(e).__name__} — {e}")

# ---------------------------------------------------------
# INTERACTIVE QUIZ MODULE
# ---------------------------------------------------------
elif choice == "Interactive Syllabus Quiz":
    st.header("📝 Python Knowledge Check")

    q1 = st.radio(
        "1. [Unit I] Which built-in function is used to find the data type of a variable?",
        ["find()", "datatype()", "type()", "check()"],
        index=None
    )

    q2 = st.radio(
        "2. [Unit II] Which keyword pair is used in Python to handle exceptions?",
        ["try / except", "do / catch", "if / else", "error / handle"],
        index=None
    )

    q3 = st.radio(
        "3. [Unit III] What is required to stop a recursive function from calling itself infinitely?",
        ["A global variable", "A base case", "A string", "A loop counter"],
        index=None
    )

    q4 = st.radio(
        "4. [Unit IV] Which Python library is designed for fast numerical arrays and vectorized math?",
        ["NumPy", "math", "random", "csv"],
        index=None
    )

    if st.button("Submit Answers"):
        if None in (q1, q2, q3, q4):
            st.warning("Please answer all 4 questions before submitting!")
        else:
            score = 0
            st.markdown("---")
            if q1 == "type()":
                score += 1
                st.success("Q1: Correct! `type()` returns the data type of an object.")
            else:
                st.error("Q1: Incorrect. The correct answer is `type()`.")

            if q2 == "try / except":
                score += 1
                st.success("Q2: Correct! `try / except` catches and handles runtime exceptions.")
            else:
                st.error("Q2: Incorrect. Python uses `try / except` (not `do / catch`).")

            if q3 == "A base case":
                score += 1
                st.success("Q3: Correct! A base case stops further recursive calls.")
            else:
                st.error("Q3: Incorrect. Without a base case, recursion runs until a `RecursionError` occurs.")

            if q4 == "NumPy":
                score += 1
                st.success("Q4: Correct! NumPy is built for fast vectorized array operations.")
            else:
                st.error("Q4: Incorrect. The correct library is `NumPy`.")

            st.subheader(f"Final Score: {score} / 4")
            if score == 4:
                st.balloons()