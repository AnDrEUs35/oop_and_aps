class SchoolJournal:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.grade_list = []
    def grade(self, assesment):
        if assesment <= 5 and assesment >= 1:
            self.grade_list.append(assesment)
    def printer(self):
        print(self.name)
        print(self.subject)
        print(self.grade_list)
    def final_grade(self):
        print(sum(self.grade_list) / len(self.grade_list))

obj = SchoolJournal('Petya', 'IT')
obj.grade(5)
obj.grade(4)
obj.grade(3)

obj.printer()
obj.final_grade()

    
