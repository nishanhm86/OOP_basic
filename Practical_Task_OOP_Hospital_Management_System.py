import os

class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = int(age)
        self.contact = contact

    def __str__(self):
        return f"{self.name} is {self.age} years old, can be contacted on {self.contact}"


class Doctor(Person):
    def __init__(self, name, age, contact, specialization, schedule, available=True):
        super().__init__(name, age, contact)
        self.specialization = specialization
        self.schedule = schedule
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"Doctor {self.name} is a specialized {self.specialization} - Schedule: {self.schedule} - {status}"

class Patient(Person):
    def __init__(self, name, age, contact, illness, appointment_number):
        super().__init__(name, age, contact)
        self.illness = illness
        self.appointment_number = int(appointment_number)

    def __str__(self):
        return f"{self.name} is {self.age} having {self.illness} and will be checked under appointment number {self.appointment_number}"

class Appointment:
    def __init__(self, appointment_number, doctor_name, patient_name, date):
        self.appointment_number = appointment_number
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.date = date

    def __str__(self):
        return f"Dr. {self.doctor_name} has an appointment on {self.date} - Patient name is {self.patient_name} - Appointment number {self.appointment_number}"

class Hospital_System:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []
        self.load_Doctors = []
        self.load_patients = []
        self.load_Appointments = []

    #Admin Functions

    def add_doctor(self):
        name = input("Enter doctor name")
        age = input("Enter doctor age")
        contact = input("Enter doctor contact")
        specialization = input("Enter doctor specialization")
        schedule = input("Enter doctor schedule")
        doctor = Doctor(name, age, contact, specialization, schedule)
        self.doctors.append(doctor)
        print("Doctor information saved to file")
        self.save_data()

    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.\n")
            return
        print("Available list of doctors:")
        for doctor in self.doctors:
            if doctor.available:
                print(doctor, "\n")

    #Patient Functions

    def register_patient(self):
        name = input("Enter patient name")
        age = input("Enter patient age")
        contact = input("Enter patient contact")
        illness = input("Enter patient illness")
        appointment_number = len(self.patients) + 1
        patient = Patient(name, age, contact, illness, appointment_number)
        self.patients.append(patient)
        print("Patient information saved to file")
        self.save_data()

    def view_patient(self):
        if not self.patients:
            print("No patients found.\n")
            return
        for patient in self.patients:
            print(patient, "\n")

    def place_appointment(self):
        if not self.doctors or not self.patients:
            print("Ensure both patient and doctor are registered .\n")
            return

        patient_name = input("Enter patient name")
        doctor_name = input("Enter doctor name")
        date = input("Enter appointment date (YYYY-MM-DD)")

        for app in self.appointments:
            if app.doctor_name == doctor_name and app.patient_name == patient_name and app.date == date:
                print (f"Doctor{doctor_name} is already booked on {date}\n")
                return

        for app in self.appointments:
            if app.doctor_name == doctor_name and app.date == date:
                print(f"Doctor{doctor_name} is already booked on {date}\n")
                return


        appointment_number = len(self.appointments) + 1

        appointment = Appointment(appointment_number, doctor_name, patient_name, date)
        self.appointments.append(appointment)
        print("Appointment information saved to file")

        for doctor in self.doctors:
            if doctor.name == doctor_name:
                doctor.available = False
                break


        self.save_data()


    #Appointment Functions

    def view_appointments(self):
        if not self.appointments:
            print("No appointment found.")
            return
        print("Appointment List")
        for appointment in self.appointments:
            print(appointment, "\n")


#File handling


    def save_data(self):
        with open("doctors.txt", "w") as file:
            for doctor in self.doctors:
                file.write(f"{doctor.name},{doctor.age},{doctor.contact},{doctor.specialization},{doctor.schedule},{doctor.available}\n")

        # Save patients
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(f"{patient.name},{patient.age},{patient.contact},{patient.illness},{patient.appointment_number}\n")

        # Save appointments
        with open("appointments.txt", "w") as file:
            for appointment in self.appointments:
                file.write(f"{appointment.appointment_number},{appointment.doctor_name},{appointment.patient_name},{appointment.date}\n")

        print("All data saved successfully.\n")


    def load_data(self):
        if os.path.exists("doctors.txt"):
            with open("doctors.txt", "r") as file:
                for line in file:
                    name, age, contact, specialization, schedule, available = line.strip().split(",")
                    self.doctors.append(Doctor(name, age, contact, specialization, schedule, available=="True"))

        if os.path.exists("patients.txt"):
            with open("patients.txt", "r") as file:
                for line in file:
                    name, age, contact, illness, appointment_number = line.strip().split(",")
                    self.patients.append(Patient(name, age, contact, illness, appointment_number))

        if os.path.exists("appointments.txt"):
            with open("appointments.txt", "r") as file:
                for line in file:
                    appointment_number, doctor_name, patient_name, date = line.strip().split(",")
                    self.appointments.append(Appointment(appointment_number, doctor_name, patient_name, date))

        print("Information loaded successfully")

    def refresh_doctor_availability(self):
        for doctor in self.doctors:
            doctor.available = not any(app.doctor_name == doctor.name for app in self.appointments)


hospital_system = Hospital_System()
hospital_system.load_data()
hospital_system.refresh_doctor_availability()


while True:

    print("="*40)
    print("Welcome to the hospital management system")
    print("="*40)
    print("1. Admin Login")
    print("2. Patient Login")
    print("3. Exit")
    print("="*40)

    choice = input("Enter your choice: ")
    if choice == "1":
        admin_login = input("Enter your login: ")
        admin_password = input("Enter your password: ")
        if admin_login == "Nishan" and admin_password == "Nishan123":
            print(f"{admin_login} Login Successfully")

            while True:
                print("="*40)
                print("Welcome to Admin Menu")
                print("="*40)
                print("1. Add a Doctor")
                print("2. View All Doctors")
                print("3. View All Patient")
                print("4. View All Appointments")
                print("5. Logout")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    hospital_system.add_doctor()
                elif admin_choice == "2":
                    hospital_system.view_doctors()
                elif admin_choice == "3":
                    hospital_system.view_patient()
                elif admin_choice == "4":
                    hospital_system.view_appointments()
                elif admin_choice == "5":
                    print("Leaving the System")
                    break

                else:
                    print("Invalid choice. Select correct choice")
        else:
            print("Invalid Credentials. Enter valid credentials")
    elif choice == "2":
        user_login = input("Enter your login: ")
        user_password = input("Enter your password: ")
        if user_login == "user" and user_password == "user123":
            print(f"{user_login} Login Successfully")
            while True:
                print("="*40)
                print("Welcome to User Menu")
                print("="*40)
                print("1. User Registration")
                print("2. View Available Doctors")
                print("3. Place an Appointments")
                print("4. View All Appointments")
                print("5. Logout")
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    hospital_system.register_patient()
                elif user_choice == "2":
                    hospital_system.view_doctors()
                elif user_choice == "3":
                    hospital_system.place_appointment()
                elif user_choice == "4":
                    hospital_system.view_appointments()
                elif user_choice == "5":
                    print("User Logging Out")
                    break

        else:
            print("Invalid Credentials. Enter valid credentials")
    elif choice == "3":
        hospital_system.save_data()
        print("All data saved successfully. Leaving the System")
        break

    else:
        print("Invalid choice. Select correct choice")
