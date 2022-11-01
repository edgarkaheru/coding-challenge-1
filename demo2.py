class school:
    Students = []
    def __init__ (self,student_id,student_name, email, course ):
        self.student_name = student_name
        self.email =email
        self.student_id = student_id,
        self.course = course 
        
        #store students in a list
        school.Students.append(self)
        
    def display_students(student_id,student_name, email, course ):
        student = {"Student_id": student_id,"Student_name": student_name,"email": email,"course": course}
        
    # def get_student(student_id ):
    
        
        

        
        

# student1 = school(1,"john", "john@gmail.com","law")
# student2 = school(2,"ruth", "ruth@gmail.com","IT")
# istudent3 = school(3,"maate", "maate@gmail.com","law")
# student4 = school(4,"edwin", "edwin@gmail.com","law")
# student5 = school(5,"kule", "kule@gmail.com","law")
# for instance in school.Students:
#     print(instance.student_id)

