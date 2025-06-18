EXCEPTION
✅ Catch errors when your Python program crashes
✅ Print useful error messages:
    – Which file
    – Which line number
    – What error happened
✅ Make your own error class (CustomException) so it’s cleaner
🔸1. sys.exc_info() — What is it?
When an error happens in Python, we can use this to ask:

“Hey Python, where exactly did the error happen?”

It gives 3 things:

python
Copy code
(type, value, traceback)
We only care about the traceback (exc_tb) — it tells us:

In which file the error happened

In which line number

sys.exc_info() = gives you details of where error happened

Custom Exception Class 

| **Component**                                      | **Explanation**                                                      | **Example/Output**                                           |
| -------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ |
| `CustomException(Exception)`                       | Inherits from Python’s built-in `Exception` class                    | Allows you to create a custom error                          |
| `__init__(self, error_message, error_detail: sys)` | Constructor that takes the actual error and system traceback         | Example: `ZeroDivisionError`, `sys`                          |
| `error_message_details(error, error_detail)`       | Function that builds a detailed message with file name & line number | Returns: `Error in [main.py] at line [5] — division by zero` |
| `exc_info()`                                       | From `sys`, gets info about the most recent exception                | Gives: type, value, traceback                                |
| `exc_tb.tb_frame.f_code.co_filename`               | Gets the name of the file where the error occurred                   | Example: `main.py`                                           |
| `exc_tb.tb_lineno`                                 | Gets the exact line number of the error                              | Example: `line 5`                                            |
| `self.error_message = error_message_details(...)`  | Stores the final formatted error string in the object                | Used when you `print` the exception                          |
| `__str__(self)`                                    | Returns the error message when exception is printed                  | Output: `Error in [main.py] at line [5] — division by zero`  |
