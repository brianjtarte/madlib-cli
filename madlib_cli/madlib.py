print("Hello World!")


# file = "./assets/dark_and_stormy_night_template.txt"


def read_template(file):
    with open(file) as f:
        contents = f.read()

    return contents


def parse_template(file):
    pass


def merge():
    pass


def welcome_msg():
    print('Welcome to MadLibs, please follow the prompts ')


def user_input():
    words_list = []
    response = input(f'Please enter a:')
    words_list.append(response)
    print(words_list)


if __name__ == "__main__":
    welcome_msg()
    read_template()
    parse_template()
