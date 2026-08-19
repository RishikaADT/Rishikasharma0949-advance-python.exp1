class patient:
    def _init__(self,patient_ID, name,treatment_cost,category):
        self.patient_ID=patient_ID
        self.name=name
        self.treatment_cost=treatment_cost
        self.category=category

    def display(self):
        print("patient_ID",self.patient_ID)
        print("name",self.name)
        print("treatment_cost",self.treatment_cost)
        print("category",self.category)

class hospital:
    def _init__(self):
        self.patient=[]   

    def add_patient(self) :
     self.patient .append(patient)


     def display_Records(self):
         print("Hospital patient racords")
         for patient in self.patient:
             patient.diaplay()

#create hospital object
hospital=hospital() 

#add patient
p1=patient(9443,"Rahul",2000,"OBC")
p2=patient(1563,"Mohan",30000,"General")
p3=patient(2818,"sunil",10000,"special")

hospital.add_patient(p1)
hospital.add_patient(p2)
hospital.add_patient(p3)

#display all records
hospital.display_records()
