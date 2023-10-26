class Student:
    def __init__(self, first_name, last_name, date_of_birth, email, essay):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.essay = essay

    def display_application(self):
        print("College Application Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Email: {self.email}")
        print("Essay:")
        print(self.essay)


def main():
    print("Welcome to the College Application System")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    email = input("Enter your email address: ")
    essay = input("Write your college admission essay: ")

    student = Student(first_name, last_name, date_of_birth, email, essay)
    student.display_application()

if __name__ == "__main__":
    main()
