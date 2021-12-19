import os, sys

if len(sys.argv) < 2:
    print("Usage: Type a name for your virtual environment")
    sys.exit()

current_directory = os.getcwd()

for i in range(1, len(sys.argv)):
    new_directory = sys.argv[i]

    path = os.path.join(current_directory, new_directory)
    if not os.path.isdir(path):
        os.mkdir(path)
        print(f"A directory called '{new_directory}' has been created...")
        os.chdir(path)

        os.system("python3 -m venv 11_env")
        print(f"Virtual environment created in folder '{new_directory}'...")
    else:
        print(f"A directory already exists called '{new_directory}'!")



