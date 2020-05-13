#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    temp_list = []
    for key,value in medical_speciality.items():
        temp_list.append(patient_medical_speciality_list.count(key))
    # speciality = list(medical_speciality.values())[temp_list.index(max(temp_list))]
    speciality = tuple(medical_speciality.values())[temp_list.index(max(temp_list))]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)

# print(tuple(patient_medical_speciality_list))