class student:

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_rno(self, rollnumber):
        self.__rollnumber = rollnumber
    def get_rno(self):
        return self.__rollnumber

obj = student()
obj.set_name("Hemalatha")
print(obj.get_name())
obj.set_rno(10)
print(obj.get_rno())




