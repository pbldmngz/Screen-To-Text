
FILE_DELIMITER = "端" * 10 + "\n" * 5 + "端" * 10 + "\n"

EXCEPTIONS = {
    "鳳" : "",
    "端": FILE_DELIMITER,  
    "\\'": "\'",
    "\\rn" : "\n",
    '\\n': '\n',
    "\\sn": "\n",
    "\\&n": "\n",
    "\\nt": "\n", 
}

SAME_CHAR_THRESHOLD = 2

# Tengo que tener mas cuidado de aquellos de una sola letra que de los que aseguraron el caracter dos o mas veces
# Tal vez puedo agrupar los caracters por grupos y "normalizar" los mas frecuentes

def fix_raw_decrypted_output(file_name: str = 'raw_decrypted_output.txt', new_file_name: str = 'fixed_decrypted_output.txt'):
    with open(file_name, 'r', encoding="utf8") as f:
        raw_decrypted_output = f.read()
    
    stabilized_text = stabilize_text(raw_decrypted_output)
    print("CHARACTER COUNT: ", len(stabilized_text))
    separate_in_files = stabilized_text.split(FILE_DELIMITER)

    for i, file in enumerate(separate_in_files):
        with open(f"{new_file_name}_{i}.txt", 'w', encoding="utf8") as f:
            f.write(file[1:-1])

def stabilize_text(text: str):
    stabilized_text = ""

    last_char = ""
    same_char_count = 0

    # remove characters that are repeated less than SAME_CHAR_THRESHOLD times in a row
    for character in text:
        if character == last_char:
            same_char_count += 1
            continue

        if same_char_count >= SAME_CHAR_THRESHOLD:
            stabilized_text += last_char
        else:
            stabilized_text += last_char * same_char_count

        same_char_count = 0
        last_char = character


    for exception in EXCEPTIONS:
        stabilized_text = stabilized_text.replace(exception, EXCEPTIONS[exception])

    return stabilized_text

if __name__ == '__main__':
    fix_raw_decrypted_output()