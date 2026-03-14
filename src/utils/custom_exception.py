"""
custom_exception.py

This module defines a custom exception class used to provide
more detailed error messages when an error occurs in the application.

Instead of showing only a basic error message, this custom exception
captures additional debugging information such as:

- The original error message
- The file where the error occurred
- The line number of the error

This helps developers quickly identify and debug issues in the code.

The module uses Python's `sys.exc_info()` function to retrieve
information about the most recent exception.
"""

import sys

class CustomException(Exception):
    """
    Custom exception class that provides detailed error information.

    This class extends Python's built-in `Exception` class and adds
    additional debugging details such as the file name and line number
    where the error occurred.

    Parameters
    ----------
    message : str
        A custom message describing the error.

    error_detail : Exception, optional
        The original exception object that triggered this error.

    Purpose
    -------
    To make debugging easier by providing more context about
    where and why the error happened.
    """

    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        """
        Generate a detailed error message.

        This method extracts information from the current exception
        including the file name and line number where the error occurred.

        Returns
        -------
        str
            A formatted error message containing:
            - Custom message
            - Original error
            - File name
            - Line number
        """

        _, _, exc_tb = sys.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"

        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        """
        Return the formatted error message when the exception is printed.
        """
        return self.error_message