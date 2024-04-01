from time import sleep
from encrypt_characters_as_dots import get_character_map, encrypt_character

# Change this to adjust the amount of "screenshots" taken (you should ensure at least 4 photos per character)
SAMPLE_RATE = 0.67

CHARACTER_MAP = get_character_map()


def create_and_edit_file(character):
    encrypted_character = CHARACTER_MAP[character]

    with open("temp_file.txt", "w+", encoding="utf8") as f:
        f.write(encrypt_character(encrypted_character))


def read_file_contents(file_path):
    # returns a character matrix, wonder if \n is considered
    with open(file_path, "r", encoding="utf8") as f:
        file_content = repr(f.read())
        return file_content


if __name__ == "__main__":

    target_paths = [
        "C:\\\\Users\\\\you\\\\Desktop\\\\whatever\\\\0001-api-changes-branch-2105-before-the-incident.patch",
        "C:\\\\Users\\\\you\\\\Desktop\\\\something else\\\\0001-changes-before-the-incident.txt",
    ]

    for target_file_path in target_paths:

        COUNTDOWN = 10
        for i in range(COUNTDOWN):
            sleep(1)
            print("Starting in: ", COUNTDOWN - i)

        create_and_edit_file("端")

        char_matrix = read_file_contents(target_file_path)

        last_char = ""

        for character in char_matrix:
            if character == last_char:
                create_and_edit_file("鳳")
                sleep(SAMPLE_RATE)
            last_char = character

            print("current character", character)
            create_and_edit_file(character)
            sleep(SAMPLE_RATE)

        create_and_edit_file("端")