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
        "Unit II: Control Structures & Exception Handling",
        "Unit III: Functions, Scope of variables & Recursion",
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
elif choice == "Unit II: Control Structures & Exception Handling":
    st.header("Unit II: Control Structures & Exception Handling")
    st.write(
        "Control structures decide the flow of execution in a Python program, while exception handling "
        "prevents runtime errors from crashing your code."
    )

    st.markdown("---")
    tab1, tab2 = st.tabs([
        "Control Structures",
        "Exception Handling"
    ])
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
    with tab2:
        st.markdown("#### Exception Handling Structure (`try` / `except` / `else` / `finally`)")
        learn_and_code(
            "How try, except, else & finally Work Together",
            "`try` tests risky code, `except` catches errors, `else` runs only if no error occurred, and `finally` always executes at the end.",
            'try:\n    x = 10 / 2\nexcept ZeroDivisionError:\n    print("Error!")\nelse:\n    print("Success:", x)\nfinally:\n    print("Execution finished.")',
            'try:\n    res = 20 / 4\nexcept ZeroDivisionError:\n    print("Division failed")\nelse:\n    print("Division succeeded:", res)\nfinally:\n    print("Cleanup complete.")',
            "try_else_finally"
        )

        st.markdown("#### Common Built-in Python Exceptions")

        learn_and_code(
            "1. ZeroDivisionError",
            "Raised when a number is divided or modulo-divided by zero (`0`).",
            'try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero!")',
            'num = 50\ndenom = 0\ntry:\n    print(num / denom)\nexcept ZeroDivisionError:\n    print("Caught ZeroDivisionError: Denominator cannot be 0.")',
            "err_zero"
        )

        learn_and_code(
            "2. ValueError",
            "Raised when a function receives an argument of the right data type, but an inappropriate value (e.g., converting `'abc'` to `int`).",
            'try:\n    age = int("twenty")\nexcept ValueError:\n    print("Invalid value! Enter digits only.")',
            'text = "hello"\ntry:\n    number = int(text)\n    print(number)\nexcept ValueError:\n    print("Caught ValueError: Could not convert text to integer.")',
            "err_value"
        )

        learn_and_code(
            "3. TypeError",
            "Raised when an operation or function is applied to an object of an incompatible type (e.g., adding a `str` and an `int`).",
            'try:\n    print("Age: " + 18)\nexcept TypeError:\n    print("Cannot add string and integer!")',
            'try:\n    total = "100" + 50\n    print(total)\nexcept TypeError:\n    print("Caught TypeError: Convert int to str using str(50) first.")',
            "err_type"
        )

        learn_and_code(
            "4. IndexError",
            "Raised when trying to access an index that is out of range in a sequence like a `list`, `tuple`, or `str`.",
            'items = ["pen", "book"]\ntry:\n    print(items[5])\nexcept IndexError:\n    print("Index out of range!")',
            'colors = ["red", "green", "blue"]\ntry:\n    print(colors[4])\nexcept IndexError:\n    print("Caught IndexError: List only has 3 items (indices 0 to 2).")',
            "err_index"
        )

        learn_and_code(
            "5. KeyError",
            "Raised when trying to access a dictionary key that does not exist.",
            'student = {"name": "Asha"}\ntry:\n    print(student["grade"])\nexcept KeyError:\n    print("Key not found in dictionary!")',
            'marks = {"Math": 90, "Python": 95}\ntry:\n    print(marks["History"])\nexcept KeyError:\n    print("Caught KeyError: \'History\' is not a key in marks.")',
            "err_key"
        )

        learn_and_code(
            "6. NameError",
            "Raised when trying to use a variable or function name that has not been defined yet.",
            'try:\n    print(undeclared_var)\nexcept NameError:\n    print("Variable is not defined!")',
            'try:\n    print(score)\nexcept NameError:\n    print("Caught NameError: Define \'score\' before printing it.")',
            "err_name"
        )

        learn_and_code(
            "7. AttributeError",
            "Raised when an invalid attribute or method is accessed on an object (e.g., calling `.append()` on an integer).",
            'num = 10\ntry:\n    num.append(5)\nexcept AttributeError:\n    print("Integers do not have an append() method!")',
            'word = "python"\ntry:\n    word.push("s")\nexcept AttributeError:\n    print("Caught AttributeError: str object has no attribute \'push\'.")',
            "err_attr"
        )

        learn_and_code(
            "8. FileNotFoundError",
            "Raised when trying to open a file that does not exist in the specified path.",
            'try:\n    f = open("missing_file.txt", "r")\nexcept FileNotFoundError:\n    print("File does not exist!")',
            'try:\n    with open("notes_2026.txt", "r") as file:\n        print(file.read())\nexcept FileNotFoundError:\n    print("Caught FileNotFoundError: Check the filename or path.")',
            "err_file"
        )

        learn_and_code(
            "9. ModuleNotFoundError (ImportError)",
            "Raised when Python cannot find the module you are trying to `import`.",
            'try:\n    import non_existent_library\nexcept ModuleNotFoundError:\n    print("Module is not installed!")',
            'try:\n    import magic_math\nexcept ModuleNotFoundError:\n    print("Caught ModuleNotFoundError: No module named \'magic_math\'.")',
            "err_import"
        )
elif choice == "Unit III: Functions, Scope of variables & Recursion":
    st.header("Unit III: Functions, Scope of variables & Recursion")
    st.write("""
    * **Function:** A self-contained, reusable block of organized code that performs a specific task. Functions help break large programs into smaller, manageable modules (avoiding code repetition) and only run when called.
    * **Parameter vs. Argument:** A **parameter** is the variable listed inside the parentheses in the function definition, whereas an **argument** is the actual value sent to the function when it is called.
    * **Variable Scope:** The region or part of a program where a variable is recognized and can be accessed. Python resolves variable names using the **LEGB Rule** (*Local → Enclosing → Global → Built-in*).
    * **Recursion:** A programming technique in which a function calls itself directly or indirectly to solve a smaller instance of the same problem until it reaches a stopping condition called the **base case**.
    """)
    st.markdown("---")
    tab1, tab2, tab3 = st.tabs([
        "1. Functions & Arguments",
        "2. Variable Scope",
        "3. Recursion"
    ])
    with tab1:
        learn_and_code(
            "Defining & Calling a Function (def & return)",
            "A function is defined using the `def` keyword and can send a result back to the caller using `return`.",
            'def greet(name):\n    return f"Hello, {name}!"\n\nprint(greet("Asha"))',
            'def calculate_area(length, width):\n    return length * width\n\narea = calculate_area(5, 4)\nprint("Area:", area)',
            "u3_def_return"
        )

        learn_and_code(
            "Default & Keyword Arguments",
            "Parameters can have default values if no argument is passed, and keyword arguments let you pass values by parameter name.",
            'def student_info(name, course="B.Sc. LL.B."):\n    print(f"{name} is enrolled in {course}")\n\nstudent_info("Riya")\nstudent_info(course="Data Science", name="Kabir")',
            'def power(base, exponent=2):\n    return base ** exponent\n\nprint("Default square:", power(5))\nprint("Cube:", power(base=5, exponent=3))',
            "u3_args"
        )

        learn_and_code(
            "Returning Multiple Values (String Analyzer)",
            "A Python function can return multiple values separated by commas (packed as a tuple).",
            'def analyze_text(text):\n    chars = len(text)\n    words = len(text.split())\n    return chars, words\n\nc, w = analyze_text("Python is fun")\nprint("Characters:", c, "| Words:", w)',
            'def analyze_text(text):\n    char_count = len(text)\n    word_count = len(text.split())\n    vowels = "aeiouAEIOU"\n    vowel_count = sum(1 for ch in text if ch in vowels)\n    return char_count, word_count, vowel_count\n\nsample = "Python programming is structured."\nc, w, v = analyze_text(sample)\nprint(f"Chars: {c}, Words: {w}, Vowels: {v}")',
            "u3_string_func"
        )

        learn_and_code(
            "Lambda (Anonymous) Functions",
            "A `lambda` function is a small, single-expression anonymous function written in one line without `def`.",
            'square = lambda x: x * x\nprint(square(6))',
            'add = lambda a, b: a + b\nprint("Sum:", add(12, 8))',
            "u3_lambda"
        )
    with tab2:
        learn_and_code(
            "Local vs. Global Scope",
            "A **local** variable is created inside a function and exists only there, while a **global** variable is defined outside all functions and can be read anywhere.",
            'x = "Global Variable"\n\ndef scope_demo():\n    x = "Local Variable"\n    print("Inside function:", x)\n\nscope_demo()\nprint("Outside function:", x)',
            'msg = "Global Hello"\n\ndef test_scope():\n    msg = "Local Hi"\n    print("Inside:", msg)\n\ntest_scope()\nprint("Outside:", msg)',
            "u3_local_global"
        )

        learn_and_code(
            "Modifying Global Variables (global keyword)",
            "To modify a global variable inside a function, you must explicitly declare it using the `global` keyword.",
            'counter = 0\n\ndef increment():\n    global counter\n    counter += 1\n\nincrement()\nincrement()\nprint("Counter:", counter)',
            'score = 10\n\ndef add_bonus():\n    global score\n    score += 5\n\nadd_bonus()\nprint("Updated Score:", score)',
            "u3_global_kw"
        )
    with tab3:
        learn_and_code(
            "Recursive Factorial (Base Case & Recursive Step)",
            "Recursion occurs when a function calls itself. Every recursive function needs a **base case** to stop calling itself and prevent infinite recursion.",
            'def factorial(n):\n    if n <= 1:  # Base case\n        return 1\n    return n * factorial(n - 1)  # Recursive step\n\nprint("5! =", factorial(5))',
            'def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nnum = 6\nprint(f"Factorial of {num} is:", factorial(num))',
            "u3_rec_fact"
        )

        learn_and_code(
            "Recursive Fibonacci Sequence",
            "In the Fibonacci sequence, each number is the sum of the two preceding numbers (`fib(n) = fib(n-1) + fib(n-2)`).",
            'def fib(n):\n    if n <= 1:\n        return n\n    return fib(n - 1) + fib(n - 2)\n\nprint([fib(i) for i in range(6)])',
            'def fib(n):\n    if n <= 1:\n        return n\n    return fib(n - 1) + fib(n - 2)\n\nfor i in range(7):\n    print(f"fib({i}) = {fib(i)}")',
            "u3_rec_fib"
        )
elif choice == "Unit IV: Introduction to NumPy":
    st.header("Unit IV: Numerical Computing with NumPy")

    # 1. Core Definitions Overview
    st.subheader("1. What is NumPy? (Core Concepts & Definitions)")
    st.markdown("""
    * **NumPy (Numerical Python):** An open-source Python library used for scientific and numerical computing. It provides support for large, multi-dimensional arrays and matrices along with high-level mathematical functions.
    * **NumPy Array (`ndarray`):** The core data structure of NumPy—an N-dimensional, homogeneous grid of values (all elements must be of the same data type) stored in contiguous memory, making it much faster and more memory-efficient than standard Python lists.
    * **Vectorization:** The ability to perform element-wise arithmetic operations directly on entire arrays without writing explicit `for` loops.
    * **Shape & Dimensions (`ndim` / `shape`):** **Dimensions (`ndim`)** indicate the number of axes (e.g., 1D vector, 2D matrix), while **shape** is a tuple showing the exact number of elements along each axis (e.g., `(2, 3)` means 2 rows and 3 columns).
    """)

    st.markdown("---")

    # 2. Interactive Tabs (Definitions + Examples + Live Coding)
    st.subheader("2. Explore NumPy & Practice Coding")
    tab1, tab2 = st.tabs([
        "Creating & Inspecting Arrays",
        "Vectorized Math & Statistics"
    ])

    # --- TAB 1: CREATING & INSPECTING ARRAYS ---
    with tab1:
        learn_and_code(
            "Creating 1D & 2D Arrays (np.array)",
            "Use `np.array()` to convert a Python list into a 1D array or a list of lists into a 2D matrix.",
            'import numpy as np\n\narr_1d = np.array([10, 20, 30])\narr_2d = np.array([[1, 2, 3], [4, 5, 6]])\nprint("1D:", arr_1d)\nprint("2D:\\n", arr_2d)',
            'import numpy as np\n\nscores = np.array([85, 90, 78, 92])\nmatrix = np.array([[10, 20], [30, 40]])\nprint("Scores:", scores)\nprint("Matrix:\\n", matrix)',
            "u4_create"
        )

        learn_and_code(
            "Built-in Array Generators (zeros, ones, arange)",
            "NumPy includes helper functions to generate arrays automatically: `np.zeros()` fills with `0`s, `np.ones()` fills with `1`s, and `np.arange(start, stop, step)` works like Python's `range()`.",
            'import numpy as np\n\nprint("Zeros:", np.zeros(4))\nprint("Range:", np.arange(0, 10, 2))',
            'import numpy as np\n\nones_arr = np.ones((2, 3))\nseq_arr = np.arange(1, 11, 2)\nprint("2x3 Ones:\\n", ones_arr)\nprint("Odd sequence:", seq_arr)',
            "u4_generators"
        )

        learn_and_code(
            "Array Attributes (ndim, shape, size, dtype)",
            "Inspect an array's structure using `.ndim` (number of dimensions), `.shape` (rows, columns), `.size` (total elements), and `.dtype` (data type).",
            'import numpy as np\n\narr = np.array([[10, 20, 30], [40, 50, 60]])\nprint("Dimensions:", arr.ndim)\nprint("Shape:", arr.shape)\nprint("Data Type:", arr.dtype)',
            'import numpy as np\n\ndata = np.array([[5, 10], [15, 20], [25, 30]])\nprint("ndim:", data.ndim)\nprint("shape:", data.shape)\nprint("size:", data.size)',
            "u4_attrs"
        )

        learn_and_code(
            "Indexing & Slicing Arrays",
            "Just like lists, NumPy arrays use zero-based indexing (`arr[0]`) and slicing (`arr[start:stop]`). For 2D arrays, use `arr[row, col]`.",
            'import numpy as np\n\narr = np.array([10, 20, 30, 40, 50])\nprint("First:", arr[0])\nprint("Slice [1:4]:", arr[1:4])',
            'import numpy as np\n\nmat = np.array([[11, 12, 13], [21, 22, 23]])\nprint("Row 0, Col 2:", mat[0, 2])\nprint("Second row:", mat[1, :])',
            "u4_slice"
        )

    # --- TAB 2: VECTORIZED MATH & STATISTICS ---
    with tab2:
        learn_and_code(
            "Vectorized Arithmetic Operations",
            "Mathematical operators (`+`, `-`, `*`, `/`, `**`) apply automatically to every element in the array at once—no loops required.",
            'import numpy as np\n\narr = np.array([10, 20, 30, 40])\nprint("Multiplied by 2:", arr * 2)\nprint("Squared:", arr ** 2)',
            'import numpy as np\n\nprices = np.array([100, 250, 400])\ndiscounted = prices * 0.90  # 10% off every item\nprint("Original:", prices)\nprint("After 10% discount:", discounted)',
            "u4_vec_math"
        )

        learn_and_code(
            "Statistical Functions (sum, mean, median, std, max, min)",
            "NumPy provides fast built-in methods to compute descriptive statistics across an array.",
            'import numpy as np\n\nmarks = np.array([72, 85, 90, 68, 95])\nprint("Mean:", np.mean(marks))\nprint("Median:", np.median(marks))\nprint("Max:", np.max(marks))',
            'import numpy as np\n\ndata = np.array([12, 15, 18, 22, 30])\nprint("Sum:", np.sum(data))\nprint("Mean:", np.mean(data))\nprint("Std Dev:", round(np.std(data), 2))',
            "u4_stats"
        )
