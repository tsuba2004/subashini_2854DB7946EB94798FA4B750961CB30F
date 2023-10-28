class student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_no = roll_number
    self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted (student_list,key=lambda student:student.cgpa, reverse=True)
  return sorted_students
students = [student("aravind","01","8.9")]

sorted_students = sort_students
print("Name : {}.,Roll No : {}., cgpa : {}.".format(student.name,student.roll_number,student.cgpa))