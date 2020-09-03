"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    # print(data)
    formatted_data = format_data(data)
    print(formatted_data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects_and_details = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        subjects_and_details.append(parts)
        # print("----------")
    input_file.close()
    return subjects_and_details


def format_data(data):
    formatted_data = ""
    for item in data:
        formatted_data += "{:6} is taught by {:12} and it has {:3} students.\n".format(item[0], item[1], item[2])
    return formatted_data


main()
