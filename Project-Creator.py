import os
import sys
import shutil
import pathlib

DIR = os.path.realpath(os.path.dirname(sys.argv[0]));
TEMPLATE_PROJECT_NAME = "sketch_TEMPLATE"
TEMPLATE_PROJECT_DIR = f"{DIR}/{TEMPLATE_PROJECT_NAME}"


def start_new_project():
    PROJECT_NAME = "sketch_" + str(input("\nEnter your new project name :").replace(" ","_").replace("-","_"))
    PROJECT_DIR = f"{DIR}/{PROJECT_NAME}"

    if os.path.exists(PROJECT_DIR):
        print("Project is already exists.")
    else:
        print(f"Creating project at {PROJECT_DIR}...")

        shutil.copytree(f"{TEMPLATE_PROJECT_DIR}",f"{PROJECT_DIR}")
        os.rename(
            f"{PROJECT_DIR}/{TEMPLATE_PROJECT_NAME}.pde",
            f"{PROJECT_DIR}/{PROJECT_NAME}.pde")
        print("Project successfly created!")
    print("Finished")

def main():
    if os.path.exists(TEMPLATE_PROJECT_DIR):
        start_new_project()
    else :
        print(f"Project template file({TEMPLATE_PROJECT_NAME}) does not found.\nCreating project template file at {TEMPLATE_PROJECT_DIR}...")
        os.makedirs(f"{TEMPLATE_PROJECT_DIR}",exist_ok=True)
        program_file = pathlib.Path(f"{TEMPLATE_PROJECT_DIR}/{TEMPLATE_PROJECT_NAME}.pde")
        program_file.touch()
        print(f"Project template file created.")
        start_new_project()

    input("\nPress 'Enter' to stop this command.");


if __name__ == "__main__":
    main()