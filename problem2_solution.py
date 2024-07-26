import pickle
import logging
from collections import defaultdict

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AddressBook:
    def __init__(self, data_file='problem2_data_file.pickle'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'rb') as f:
                logging.info(f"Loading data from {self.data_file}")
                data = pickle.load(f)
                if not isinstance(data, dict):
                    logging.error(f"Data format is incorrect. Starting with an empty database.")
                    return {}
                return data
        except FileNotFoundError:
            logging.warning(f"{self.data_file} not found. Starting with an empty database.")
            return {}
        except EOFError:
            logging.warning(f"{self.data_file} is empty. Starting with an empty database.")
            return {}
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            return {}

    def save_data(self):
        try:
            with open(self.data_file, 'wb') as f:
                pickle.dump(self.data, f)
                logging.info(f"Data saved to {self.data_file}")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def add_contact(self, fname, lname, street, city, state, country, mobile, email):
        if email in self.data or mobile in {c['mobile'] for c in self.data.values()}:
            logging.error(f"Duplicate email or mobile detected.")
            return "Duplicate email or mobile detected."
        
        self.data[email] = {
            'fname': fname, 'lname': lname, 'street': street,
            'city': city, 'state': state, 'country': country,
            'mobile': mobile, 'email': email
        }
        self.save_data()
        logging.info(f"Added contact: {fname} {lname}")
        return "Contact added."

    def count_occurrences(self, field_name, value):
        return sum(1 for contact in self.data.values() if contact.get(field_name) == value)

    def summary(self):
        fields = ['fname', 'lname', 'street']
        results = defaultdict(int)
        
        for field in fields:
            value = input(f"Enter {field.replace('street', 'street address')} to search: ")
            results[field] = self.count_occurrences(field, value)
        
        for field, count in results.items():
            print(f"Occurrences of '{value}' in {field.title().replace('Street', 'Street Address')}: {count}")

    def input_with_retries(self, prompt, validation_func, error_message, max_retries=3):
        for attempt in range(max_retries):
            value = input(prompt)
            if validation_func(value):
                return value
            print(error_message)
            logging.warning(f"Invalid input: {value} (attempt {attempt + 1} of {max_retries})")
        print("Max retries reached. Exiting.")
        logging.error("Max retries reached for input")
        return None

    def run(self):
        while True:
            print("\nOptions: 1. Add Contact 2. Summary 3. Exit")
            option = input("Enter option number: ")

            if option == '1':
                fname = self.input_with_retries("Enter first name: ", lambda x: bool(x.strip()), "Invalid first name.")
                if not fname:
                    continue
                lname = self.input_with_retries("Enter last name: ", lambda x: bool(x.strip()), "Invalid last name.")
                if not lname:
                    continue
                street = self.input_with_retries("Enter street address: ", lambda x: bool(x.strip()), "Invalid street address.")
                if not street:
                    continue
                city = self.input_with_retries("Enter city: ", lambda x: bool(x.strip()), "Invalid city.")
                if not city:
                    continue
                state = self.input_with_retries("Enter state: ", lambda x: bool(x.strip()), "Invalid state.")
                if not state:
                    continue
                country = self.input_with_retries("Enter country: ", lambda x: bool(x.strip()), "Invalid country.")
                if not country:
                    continue
                mobile = self.input_with_retries("Enter mobile number: ", lambda x: x.isdigit(), "Invalid mobile number.")
                if not mobile:
                    continue
                email = self.input_with_retries("Enter email: ", lambda x: "@" in x, "Invalid email.")
                if not email:
                    continue
                result = self.add_contact(fname, lname, street, city, state, country, mobile, email)
                print(result)

            elif option == '2':
                self.summary()

            elif option == '3':
                print("Exiting.")
                break

            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    address_book = AddressBook()
    address_book.run()

