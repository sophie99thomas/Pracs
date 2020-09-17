from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print("\n", ruby, "\n", python, "\n", visual_basic, "\n")

languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for i in range(len(languages)):
    if languages[i].is_dynamic():
        print(languages[i].name)
