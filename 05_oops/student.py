def main():
    # name = get_name()
    # house = get_house()
    name, house = get_student()
    print(f"{name} from {house}")



# def get_name():
#     name = input("Enter your name: ")
#     return name

# def get_house():
#     house = input("Enter your house: ")
#     return house


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return name, house



if __name__ == "__main__":
    main()
