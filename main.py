from image_generator import InviteGenerator
# import functions
from person import Person


def main():
    # print("Hello World!")
    generator = InviteGenerator("./invitation.png")
    # for person in functions.get_participants():
    #     generator.create(person)
        # print(person.first_name)
    
    person = Person(uuid=None, first_name="John",last_name="Doe",email="john.doe@gmail.com",team=None)

    generator.create(sanjay)


if __name__ == "__main__":
    main()
