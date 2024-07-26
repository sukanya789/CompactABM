# CompactABM
Overview

This design is a compact address book management system designed to store and manage contact information efficiently. The system allows users to add, retrieve, and search contact details such as names, addresses, and phone numbers. Data is persisted using Python's pickle module, ensuring that the information remains available between sessions.

Features

Add Contact Information: Input personal details including first name, last name, street address, city, state, country, mobile number, and email. The system ensures that email addresses and phone numbers are unique.
Search Functionality: Find the number of occurrences of first names, last names, and street addresses in the address book.
Data Persistence: Information is saved to a file (problem2_data_file.pickle) and loaded on startup.
Input Validation: Proper validation and error handling for user inputs with retry attempts for incorrect entries.
Logging: Logs actions and errors to aid in debugging and tracking.

Prerequisites

Python 3.x

Usage

Add Contact: Choose option 1 to add a new contact. Follow the prompts to input the required details.
Summary: Choose option 2 to search for the number of occurrences of specific first names, last names, or street addresses.
Exit: Choose option 3 to exit the application.
Files
problem2_solution.py: The main script containing the implementation of the address book management system.
problem2_data_file.pickle: The file where contact data is stored.
README.md: This file.


Contributing

Feel free to submit pull requests or open issues to contribute to the development of this project.
