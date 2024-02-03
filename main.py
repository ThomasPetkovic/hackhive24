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
    def __init__(self, name, dob, checkin, phone, address, email, doctor, occupation, allergies, conditions, sex, race, image, body_count, insurance, credit_card, height, weight, emergency_contact):

        self.name = name
        self.dob = dob
        self.checkin = checkin
        self.phone = phone
        self.address = address
        self.email = email
        self.doctor = doctor
        self.occupation = occupation
        self.allergies = allergies
        self.conditions = conditions
        self.sex = sex
        self.race = race
        self.image = image
        self.body_count = body_count
        self.insurance = insurance
        self.credit_card = credit_card
        self.height = height
        self.weight = weight
        self.emergency_contact = emergency_contact

        self.patient_dict = {
            "name": self.name,
            "dob": self.dob,
            "checkin": self.checkin,
            "phone": self.phone,
            "address": self.address,
            "email": self.email,
            "doctor": self.doctor,
            "occupation": self.occupation,
            "allergies": self.allergies,
            "conditions": self.conditions,
            "sex": self.sex,
            "race":self.race,
            "self.image": self.image,
            "body_count": self.body_count,
            "insurance": self.insurance,
            "credit_card": self.credit_card,
            "height": self.height,
            "weight": self.weight,
            "emergency_contact": self.emergency_contact
            
        }


    
    


#function to create Patients
        
    def create_patient(self):
        return self.patient_dict


#test create patient
    
patient1 = Patient("John Doe", "01/01/1990", "12:00", "123-456-7890", "1234 Main St", "John.Doe@gmail.com", "Dr. Smith", "Engineer", ["Peanuts", "Shellfish"], ["Diabetes", "Hypertension"],"Male", "White","", 10, "Blue Cross", 123456789, 72, 180, "Jane Doe")
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
            print(patient.name, patient.conditions)
    
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




    