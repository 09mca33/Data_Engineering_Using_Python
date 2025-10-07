class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house} "

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Name is required")
        self._name = name
    
def main():
    student = get_student()
    print(student)
    # print(f'{student.name} from {student.house}')
    # print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    print("This is the main module")
    main()
