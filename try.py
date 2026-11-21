import streamlit as st
import numpy as np
import io
import contextlib
st.set_page_config(page_title="Python Helper", page_icon="🐍", layout="wide")
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Introduction to Python and the different data types",
        "Unit II: Control & Logic",
        "Unit III: Functions, Scope & Recursion",
        "Unit IV: Introduction to NumPy",
        "Interactive Syllabus Quiz"
    ]
)
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
if choice == "Unit I: Introduction to Python and the different data types":
    st.header("Introduction to Python and the different data types")
    st.subheader("1. What is Python?")
    st.write(
        "**Python** is a high-level, interpreted, general-purpose programming language known for its simple, "
        "English-like syntax. It uses **dynamic typing**, meaning you don't have to declare a variable's data type "
        "before using it—Python detects it automatically."
    )
    st.markdown("---")
    st.subheader("2. Python Data Types")
    tab1, tab2, tab3 = st.tabs([
        "Basic Data Types", 
        "Collection Data Types", 
        "Other Data Types"
    ])
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
        )
# ---------------------------------------------------------
# UNIT II: Control Structures & Exception Handling
# ---------------------------------------------------------
elif choice == "Unit II: Control & Logic":
    st.header("Unit II: Control Structures & Exception Handling")
    st.write(
        "Control structures decide the flow of execution in a Python program, while exception handling "
        "prevents runtime errors from crashing your code."
    )

    st.markdown("---")
    tab1, tab2 = st.tabs([
        "Control Structures (Conditionals & Loops)",
        "Exception Handling"
    ])

    # --- TAB 1: CONTROL STRUCTURES ---
    with tab1:
        learn_and_code(
            "Conditional Statements (if / elif / else)",
            "Executes different blocks of code depending on whether a condition evaluates to `True` or `False`.",
            'marks = 78\nif marks >= 75:\n    print("Distinction")\nelif marks >= 40:\n    print("Pass")\nelse:\n    print("Fail")',
            'temperature = 22\nif temperature > 30:\n    print("It is hot outside")\nelif temperature >= 15:\n    print("Pleasant weather")\nelse:\n    print("It is cold")',
            "if_else"
        )
        learn_and_code(
            "For Loop (for)",
            "Iterates over a sequence (such as a `list`, `string`, or `range`) a fixed number of times.",
            'for i in range(1, 6):\n    print("*" * i)',
            '# Print a 5-row star triangle\nfor i in range(1, 6):\n    print("*" * i)',
            "for_loop"
        )
        learn_and_code(
            "While Loop (while)",
            "Repeats a block of code as long as a specified condition remains `True`.",
            'count = 1\nwhile count <= 3:\n    print("Count:", count)\n    count += 1',
            'num = 5\nwhile num > 0:\n    print("Countdown:", num)\n    num -= 1\nprint("Go!")',
            "while_loop"
        )
        learn_and_code(
            "Loop Control Statements (break & continue)",
            "`break` exits the loop immediately, while `continue` skips the current iteration and moves to the next one.",
            'for n in range(1, 6):\n    if n == 3:\n        continue  # skips 3\n    if n == 5:\n        break     # stops at 5\n    print(n)',
            'for n in range(1, 8):\n    if n == 4:\n        continue\n    if n == 6:\n        break\n    print("Number:", n)',
            "break_continue"
        )

    # --- TAB 2: EXCEPTION HANDLING ---
    with tab2:
        learn_and_code(
            "try and except Blocks",
            "Code that might raise an error goes inside `try`, and the fallback response goes inside `except` so the program does not crash.",
            'try:\n    result = 10 / 0\n    print(result)\nexcept ZeroDivisionError:\n    print("Error: Cannot divide by zero!")',
            'try:\n    a = 10\n    b = 0\n    print("Result:", a / b)\nexcept ZeroDivisionError:\n    print("Caught ZeroDivisionError: Division by zero is not allowed.")',
            "try_except"
        )
        learn_and_code(
            "Handling Multiple Exceptions (ValueError & ZeroDivisionError)",
            "You can attach multiple `except` blocks to catch different types of runtime errors separately.",
            'try:\n    num = int("abc")\n    print(100 / num)\nexcept ValueError:\n    print("Invalid number format!")\nexcept ZeroDivisionError:\n    print("Cannot divide by zero!")',
            'user_input = "twenty"  # Try changing this to "0" or "5"\ntry:\n    val = int(user_input)\n    print("100 divided by input:", 100 / val)\nexcept ValueError:\n    print("ValueError: Please provide digits only.")\nexcept ZeroDivisionError:\n    print("ZeroDivisionError: Cannot divide by zero.")',
            "multi_except"
        )
        learn_and_code(
            "else and finally Blocks",
            "`else` runs only if no exception occurred in `try`, while `finally` always runs whether an error happened or not.",
            'try:\n    x = 10 / 2\nexcept ZeroDivisionError:\n    print("Error!")\nelse:\n    print("Success:", x)\nfinally:\n    print("Execution finished.")',
            'try:\n    res = 20 / 4\nexcept ZeroDivisionError:\n    print("Division failed")\nelse:\n    print("Division succeeded:", res)\nfinally:\n    print("Cleanup complete.")',
            "else_finally"
        )
