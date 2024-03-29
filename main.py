#git add --all
#git commit -m "hackhive"
#git push origin main 


"""
Patient class with

name(str)
date of birth(str)
checkout/in time(str)
phone number(str)
address(str)
email(str)
doctor(str)
address(list)
occupation(str)
allergies(list)
conditions(list)
sex(str)
race(str)
image(img)
bodycount(int)
healthcard(str)
insurace(str)
credit card(int)
height(int)
weight(int)
emergency contacty(str)



"""


class Patient:
    def __init__(self, firstName, lastName, birthday, married, checkIn, phone, address, email, doctor, occupation, allergies, conditions, sex, ethnicity, image, insurance, credit_card, height, weight, emergency_contact):
    


        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.married = married
        self.checkIn = checkIn
        self.phone = phone
        self.address = address
        self.email = email
        self.doctor = doctor
        self.occupation = occupation
        self.allergies = allergies
        self.conditions = conditions
        self.sex = sex
        self.ethnicity = ethnicity
        self.image = image
        self.insurance = insurance
        self.credit_card = credit_card
        self.height = height
        self.weight = weight
        self.emergency_contact = emergency_contact
    
    
        self.patient_dict = {
            "First Name": self.firstName,
            "Last Name": self.lastName,
            "Birthday": self.birthday,
            "Married": self.married,
            "Check In Time": self.checkIn,
            "Phone": self.phone,
            "Address": self.address,
            "Email": self.email,
            "Doctor": self.doctor,
            "Occupation": self.occupation,
            "Allergies": self.allergies,
            "Conditions": self.conditions,
            "Sex": self.sex,
            "Ethnicity":self.ethnicity,
            "Image": self.image,
            "Insurance": self.insurance,
            "Credit Card": self.credit_card,
            "Height": self.height,
            "Weight": self.weight,
            "Emergency Contact": self.emergency_contact
            
            }
        
    def create_patient(self):
        return self.patient_dict
    



for i in range(1):
    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    birthday = input("Enter Birthday: ")
    married = input("Married? YES or NO: ")
    checkIn = input("Enter Check In Time: ")
    phone = int(input("Enter Phone Number: "))
    address = input("Enter Address: ")
    email = input("Enter Email: ")
    doctor = input("Enter Doctor: ")
    occupation = input("Enter Occupation: ")  
    allergies = input("Enter Allergies: ").split()
    conditions = input("Enter Conditions: ").split()
    sex = input("Enter Sex:")
    ethnicity = input("Enter Ethnicity: ")
    insurance = input("Enter Insurance: ")
    credit_card = int(input("Enter Credit Card: "))
    height = int(input("Enter Height: "))
    weight = int(input("Enter Weight: "))
    contact = input("Enter Emergency Contact: ")       


    
   
patient1 = Patient(firstName, lastName, birthday, married, checkIn, phone, address, email, doctor, occupation, allergies, conditions,sex,ethnicity,"Image",insurance,credit_card,height,weight,contact)              


    

print()

for key, value in patient1.create_patient().items():
    print(f"{key}: {value}")

print()



class Queue:
    def __init__(self):
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)

    def remove_patient(self):
        return self.queue.pop(0)

    def show_queue(self):
        for patient in self.queue:
            print(patient.firstName, patient.lastName, patient.conditions)
    
    def next_patient(self):
        return self.queue[0]
    
    def queue_length(self):
        return len(self.queue)

#test
    
queue = Queue()
queue.add_patient(patient1)
queue.show_queue()
print("Length of Queue:",queue.queue_length())
queue.remove_patient()
queue.show_queue()
print("Length of Queue:",queue.queue_length())

        
        




#:3