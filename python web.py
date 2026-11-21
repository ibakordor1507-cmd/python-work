import streamlit as st
import numpy as np
import io
import contextlib
st.set_page_config(page_title="Python Helper", page_icon="🐍", layout="wide")
st.title("🐍 Python Study Companion")
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
def learn_and_code(title, definition, example_code, starter_code="", key_id=""):
    with st.expander(f"📘 {title}", expanded=False):
        st.write(definition)
        st.markdown("**Example:**")
        st.code(example_code, language="python")
        
        st.markdown("**💻 Try Coding It Yourself:**")
        user_code = st.text_area(
            "Write your Python code below:",
            value="",
            placeholder="# Type your Python code here and click Run Code...",
            height=110,
            key=f"code_{key_id}"
        )
        if st.button("▶ Run Code", key=f"btn_{key_id}"):
            if not user_code.strip():
                st.warning("Please write some Python code first before running!")
            else:
                output_buffer = io.StringIO()
                try:
                    with contextlib.redirect_stdout(output_buffer):
                        exec(user_code, {"np": np})
                    res = output_buffer.getvalue()
                    st.code(res if res else "(Executed with no print output)", language="text")
                except Exception as e:
                    st.error(f"{type(e).__name__}: {e}")
if choice == "Unit I: Introduction & Data Types":
    st.header("Unit I: Introduction & Data Types")
    st.subheader("1. What is Python?")
    st.write(
        "**Python** is a high-level, interpreted, general-purpose programming language known for its simple, "
        "English-like syntax. It uses **dynamic typing**, meaning you don't have to declare a variable's data type "
        "before using it—Python detects it automatically."
    )

    st.markdown("---")
    st.subheader("2. Python Data Types (Click any type to learn & code)")
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
            "",
            "str"
        )
        learn_and_code(
            "Integer (int)",
            "Whole numbers (positive, negative, or zero) without any decimal point.",
            'age = 18\nprint(age + 2)\nprint(type(age))',
            "",
            "int"
        )
        learn_and_code(
            "Float (float)",
            "Real numbers that contain a decimal point or use scientific notation.",
            'pi = 3.14\nprint(pi * 2)\nprint(type(pi))',
            "",
            "float"
        )
        learn_and_code(
            "Boolean (bool)",
            "Represents logical truth values and can only be `True` or `False`.",
            'is_student = True\nprint(is_student)\nprint(type(is_student))',
            "",
            "bool"
        )
        learn_and_code(
            "Complex (complex)",
            "Numbers with a real and an imaginary part written as `a + bj` (where `j` is the imaginary unit).",
            'z = 3 + 4j\nprint("Real:", z.real, "Imaginary:", z.imag)\nprint(type(z))',
            "",
            "complex"
        )
    with tab2:
        learn_and_code(
            "List (list)",
            "An ordered, mutable (changeable) collection that allows duplicate items, written with square brackets `[]`.",
            'fruits = ["apple", "banana", "apple"]\nfruits.append("cherry")\nprint(fruits)',
            "",
            "list"
        )
        learn_and_code(
            "Tuple (tuple)",
            "An ordered, immutable (unchangeable) collection that allows duplicates, written with parentheses `()`.",
            'coords = (10, 20)\nprint(coords[0])\nprint(type(coords))',
            "",
            "tuple"
        )
        learn_and_code(
            "Set (set)",
            "An unordered, mutable collection of unique items (automatically removes duplicates), written with `{}`.",
            'nums = {1, 2, 2, 3}\nprint(nums)  # Output: {1, 2, 3}',
            "",
            "set"
        )
        learn_and_code(
            "Dictionary (dict)",
            "An ordered (Python 3.7+), mutable collection of `key: value` pairs with unique keys, written with `{}`.",
            'student = {"name": "Riya", "age": 18}\nprint(student["name"])',
            "",
            "dict"
        )
    with tab3:
        learn_and_code(
            "NoneType (None)",
            "Represents the intentional absence of a value or a null object.",
            'result = None\nprint(result)\nprint(type(result))',
            "",
            "none"
        )
        learn_and_code(
            "Range (range)",
            "Represents an immutable sequence of numbers, commonly used in loops.",
            'r = range(1, 5)\nprint(list(r))  # [1, 2, 3, 4]',
            "",
            "range"
        )
        learn_and_code(
            "Bytes (bytes)",
            "An immutable sequence of single bytes (integers 0–255), prefixed with `b`.",
            'b_data = b"Hello"\nprint(b_data)\nprint(type(b_data))',
            "",
            "bytes"
        )
        learn_and_code(
            "Bytearray (bytearray)",
            "A mutable sequence of bytes whose individual byte values can be modified.",
            'ba = bytearray(b"ABC")\nba[0] = 90  # ASCII for Z\nprint(ba)',
            "",
            "bytearray"
        )
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
    with tab1:
        learn_and_code(
            "Conditional Statements (if / elif / else)",
            "Executes different blocks of code depending on whether a condition evaluates to `True` or `False`.",
            'marks = 78\nif marks >= 75:\n    print("Distinction")\nelif marks >= 40:\n    print("Pass")\nelse:\n    print("Fail")',
            "",
            "if_else"
        )
        learn_and_code(
            "For Loop (for)",
            "Iterates over a sequence (such as a `list`, `string`, or `range`) to repeat an action for each item.",
            'subjects = ["Law", "Python", "Statistics"]\nfor sub in subjects:\n    print("Studying:", sub)\n\n# Multiplication table of 5\nfor i in range(1, 6):\n    print(f"5 x {i} = {5 * i}")',
            "",
            "for_loop"
        )
        learn_and_code(
            "While Loop (while)",
            "Repeats a block of code as long as a specified condition remains `True`.",
            'count = 1\nwhile count <= 3:\n    print("Count:", count)\n    count += 1',
            "",
            "while_loop"
        )
        learn_and_code(
            "Loop Control Statements (break & continue)",
            "`break` exits the loop immediately, while `continue` skips the current iteration and moves to the next one.",
            'for n in range(1, 6):\n    if n == 3:\n        continue  # skips 3\n    if n == 5:\n        break     # stops at 5\n    print(n)',
            "",
            "break_continue"
        )
    with tab2:
        st.markdown("#### Exception Handling Structure (`try` / `except` / `else` / `finally`)")
        learn_and_code(
            "How try, except, else & finally Work Together",
            "`try` tests risky code, `except` catches errors, `else` runs only if no error occurred, and `finally` always executes at the end.",
            'try:\n    x = 10 / 2\nexcept ZeroDivisionError:\n    print("Error!")\nelse:\n    print("Success:", x)\nfinally:\n    print("Execution finished.")',
            "",
            "try_else_finally"
        )

        st.markdown("#### Common Built-in Python Exceptions (Click any error to learn & code)")

        learn_and_code(
            "1. ZeroDivisionError",
            "Raised when a number is divided or modulo-divided by zero (`0`).",
            'try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero!")',
            "",
            "err_zero"
        )

        learn_and_code(
            "2. ValueError",
            "Raised when a function receives an argument of the right data type, but an inappropriate value (e.g., converting `'abc'` to `int`).",
            'try:\n    age = int("twenty")\nexcept ValueError:\n    print("Invalid value! Enter digits only.")',
            "",
            "err_value"
        )

        learn_and_code(
            "3. TypeError",
            "Raised when an operation or function is applied to an object of an incompatible type (e.g., adding a `str` and an `int`).",
            'try:\n    print("Age: " + 18)\nexcept TypeError:\n    print("Cannot add string and integer!")',
            "",
            "err_type"
        )

        learn_and_code(
            "4. IndexError",
            "Raised when trying to access an index that is out of range in a sequence like a `list`, `tuple`, or `str`.",
            'items = ["pen", "book"]\ntry:\n    print(items[5])\nexcept IndexError:\n    print("Index out of range!")',
            "",
            "err_index"
        )

        learn_and_code(
            "5. KeyError",
            "Raised when trying to access a dictionary key that does not exist.",
            'student = {"name": "Asha"}\ntry:\n    print(student["grade"])\nexcept KeyError:\n    print("Key not found in dictionary!")',
            "",
            "err_key"
        )

        learn_and_code(
            "6. NameError",
            "Raised when trying to use a variable or function name that has not been defined yet.",
            'try:\n    print(undeclared_var)\nexcept NameError:\n    print("Variable is not defined!")',
            "",
            "err_name"
        )

        learn_and_code(
            "7. AttributeError",
            "Raised when an invalid attribute or method is accessed on an object (e.g., calling `.append()` on an integer).",
            'num = 10\ntry:\n    num.append(5)\nexcept AttributeError:\n    print("Integers do not have an append() method!")',
            "",
            "err_attr"
        )

        learn_and_code(
            "8. FileNotFoundError",
            "Raised when trying to open a file that does not exist in the specified path.",
            'try:\n    f = open("missing_file.txt", "r")\nexcept FileNotFoundError:\n    print("File does not exist!")',
            "",
            "err_file"
        )

        learn_and_code(
            "9. ModuleNotFoundError (ImportError)",
            "Raised when Python cannot find the module you are trying to `import`.",
            'try:\n    import non_existent_library\nexcept ModuleNotFoundError:\n    print("Module is not installed!")',
            "",
            "err_import"
        )
elif choice == "Unit III: Functions, Scope & Recursion":
    st.header("Unit III: Modular Programming — Functions, Scope & Recursion")
    st.subheader("1. Core Concepts & Definitions")
    st.markdown("""
    * **Function:** A self-contained, reusable block of organized code that performs a specific task. Functions help break large programs into smaller, manageable modules (avoiding code repetition) and only run when called.
    * **Parameter vs. Argument:** A **parameter** is the variable listed inside the parentheses in the function definition, whereas an **argument** is the actual value sent to the function when it is called.
    * **Variable Scope:** The region or part of a program where a variable is recognized and can be accessed. Python resolves variable names using the **LEGB Rule** (*Local → Enclosing → Global → Built-in*).
    * **Recursion:** A programming technique in which a function calls itself directly or indirectly to solve a smaller instance of the same problem until it reaches a stopping condition called the **base case**.
    """)

    st.markdown("---")
    st.subheader("2. Explore Concepts & Practice Coding")
    tab1, tab2, tab3 = st.tabs([
        "Functions & Arguments",
        "Variable Scope (LEGB)",
        "Recursion"
    ])
    with tab1:
        st.markdown(
            "**How Functions Work:** Every Python function starts with the `def` keyword, followed by the function name, "
            "parentheses `()`, and a colon `:`. Inside the indented block, `return` sends a computed value back to the caller."
        )

        learn_and_code(
            "Defining & Calling a Function (def & return)",
            "A function is defined using `def` and sends a result back using `return`. Without `return`, a function returns `None` by default.",
            'def greet(name):\n    return f"Hello, {name}!"\n\nprint(greet("Asha"))',
            "",
            "u3_def_return"
        )

        learn_and_code(
            "Default & Keyword Arguments",
            "**Default arguments** assign a fallback value to a parameter if none is provided during the call. **Keyword arguments** pass values explicitly using `parameter=value`, regardless of order.",
            'def student_info(name, course="B.Sc. LL.B."):\n    print(f"{name} is enrolled in {course}")\n\nstudent_info("Riya")\nstudent_info(course="Data Science", name="Kabir")',
            "",
            "u3_args"
        )

        learn_and_code(
            "Returning Multiple Values (String Analyzer)",
            "A Python function can return multiple values separated by commas, which Python automatically packs into a tuple.",
            'def analyze_text(text):\n    chars = len(text)\n    words = len(text.split())\n    return chars, words\n\nc, w = analyze_text("Python is fun")\nprint("Characters:", c, "| Words:", w)',
            "",
            "u3_string_func"
        )

        learn_and_code(
            "Lambda (Anonymous) Functions",
            "A **lambda function** is a compact, single-expression anonymous function (a function without a name) defined using the `lambda` keyword.",
            'square = lambda x: x * x\nprint(square(6))',
            "",
            "u3_lambda"
        )
    with tab2:
        st.markdown(
            "**Understanding Scope:** Not all variables are accessible everywhere. **Local variables** exist only inside the function "
            "where they are created, while **Global variables** are declared in the main body of the script and persist throughout the program."
        )

        learn_and_code(
            "Local vs. Global Scope",
            "If a local variable inside a function has the same name as a global variable, Python treats them as two separate variables—the local one only affects code inside the function.",
            'x = "Global Variable"\n\ndef scope_demo():\n    x = "Local Variable"\n    print("Inside function:", x)\n\nscope_demo()\nprint("Outside function:", x)',
            "",
            "u3_local_global"
        )

        learn_and_code(
            "Modifying Global Variables (global keyword)",
            "By default, you can read a global variable inside a function, but you cannot reassign it unless you declare it with the `global` keyword.",
            'counter = 0\n\ndef increment():\n    global counter\n    counter += 1\n\nincrement()\nincrement()\nprint("Counter:", counter)',
            "",
            "u3_global_kw"
        )
    with tab3:
        st.markdown(
            "**Two Essential Parts of Recursion:**\n"
            "1. **Base Case:** The condition under which the function stops calling itself (prevents infinite loops and `RecursionError`).\n"
            "2. **Recursive Case:** The part where the function calls itself with a modified input moving closer to the base case."
        )

        learn_and_code(
            "Recursive Factorial (n!)",
            "Factorial multiplies a positive integer by all positive integers below it (`5! = 5 × 4 × 3 × 2 × 1`). Here, `n <= 1` is the **base case**.",
            'def factorial(n):\n    if n <= 1:  # Base case\n        return 1\n    return n * factorial(n - 1)  # Recursive step\n\nprint("5! =", factorial(5))',
            "",
            "u3_rec_fact"
        )

        learn_and_code(
            "Recursive Fibonacci Sequence",
            "In the Fibonacci sequence (`0, 1, 1, 2, 3, 5...`), each term is the sum of the two previous terms (`fib(n) = fib(n-1) + fib(n-2)`).",
            'def fib(n):\n    if n <= 1:\n        return n\n    return fib(n - 1) + fib(n - 2)\n\nprint([fib(i) for i in range(6)])',
            "",
            "u3_rec_fib"
        )
elif choice == "Unit IV: Introduction to NumPy":
    st.header("Unit IV: Numerical Computing with NumPy")
    st.subheader("1. What is NumPy? (Core Concepts & Definitions)")
    st.markdown("""
    * **NumPy (Numerical Python):** An open-source Python library used for scientific and numerical computing. It provides support for large, multi-dimensional arrays and matrices along with high-level mathematical functions.
    * **NumPy Array (`ndarray`):** The core data structure of NumPy—an N-dimensional, homogeneous grid of values (all elements must be of the same data type) stored in contiguous memory, making it much faster and more memory-efficient than standard Python lists.
    * **Vectorization:** The ability to perform element-wise arithmetic operations directly on entire arrays without writing explicit `for` loops.
    * **Shape & Dimensions (`ndim` / `shape`):** **Dimensions (`ndim`)** indicate the number of axes (e.g., 1D vector, 2D matrix), while **shape** is a tuple showing the exact number of elements along each axis (e.g., `(2, 3)` means 2 rows and 3 columns).
    """)

    st.markdown("---")
    st.subheader("2. Explore NumPy & Practice Coding")
    tab1, tab2 = st.tabs([
        "Creating & Inspecting Arrays",
        "Vectorized Math & Statistics"
    ])
    with tab1:
        learn_and_code(
            "Creating 1D & 2D Arrays (np.array)",
            "Use `np.array()` to convert a Python list into a 1D array or a list of lists into a 2D matrix.",
            'import numpy as np\n\narr_1d = np.array([10, 20, 30])\narr_2d = np.array([[1, 2, 3], [4, 5, 6]])\nprint("1D:", arr_1d)\nprint("2D:\\n", arr_2d)',
            "",
            "u4_create"
        )

        learn_and_code(
            "Built-in Array Generators (zeros, ones, arange)",
            "NumPy includes helper functions to generate arrays automatically: `np.zeros()` fills with `0`s, `np.ones()` fills with `1`s, and `np.arange(start, stop, step)` works like Python's `range()`.",
            'import numpy as np\n\nprint("Zeros:", np.zeros(4))\nprint("Range:", np.arange(0, 10, 2))',
            "",
            "u4_generators"
        )

        learn_and_code(
            "Array Attributes (ndim, shape, size, dtype)",
            "Inspect an array's structure using `.ndim` (number of dimensions), `.shape` (rows, columns), `.size` (total elements), and `.dtype` (data type).",
            'import numpy as np\n\narr = np.array([[10, 20, 30], [40, 50, 60]])\nprint("Dimensions:", arr.ndim)\nprint("Shape:", arr.shape)\nprint("Data Type:", arr.dtype)',
            "",
            "u4_attrs"
        )

        learn_and_code(
            "Indexing & Slicing Arrays",
            "Just like lists, NumPy arrays use zero-based indexing (`arr[0]`) and slicing (`arr[start:stop]`). For 2D arrays, use `arr[row, col]`.",
            'import numpy as np\n\narr = np.array([10, 20, 30, 40, 50])\nprint("First:", arr[0])\nprint("Slice [1:4]:", arr[1:4])',
            "",
            "u4_slice"
        )
    with tab2:
        learn_and_code(
            "Vectorized Arithmetic Operations",
            "Mathematical operators (`+`, `-`, `*`, `/`, `**`) apply automatically to every element in the array at once—no loops required.",
            'import numpy as np\n\narr = np.array([10, 20, 30, 40])\nprint("Multiplied by 2:", arr * 2)\nprint("Squared:", arr ** 2)',
            "",
            "u4_vec_math"
        )

        learn_and_code(
            "Statistical Functions (sum, mean, median, std, max, min)",
            "NumPy provides fast built-in methods to compute descriptive statistics across an array.",
            'import numpy as np\n\nmarks = np.array([72, 85, 90, 68, 95])\nprint("Mean:", np.mean(marks))\nprint("Median:", np.median(marks))\nprint("Max:", np.max(marks))',
            "",
            "u4_stats"
        )