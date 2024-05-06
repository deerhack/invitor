from image_generator import InviteGenerator
import functions


def main():
    print("Hello World!")
    generator = InviteGenerator("./invitation.png")
    for person in functions.get_participants():
        generator.create(person)
        # print(person.first_name)


if __name__ == "__main__":
    main()
