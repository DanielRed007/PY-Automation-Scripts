
import os
import subprocess

def execute_sample_script():
    location = "sample_scripts/hello_world.py"

    if os.path.exists(location):
        command = ["python3", location]

        try:
            subprocess.run(command, check= True)
            print("Success!")
        except subprocess.CalledProcessError as error:
            print(f"Execution Error: {error}")
    else:
        print("Script doesn't exists")

if __name__ == "__main__":
    execute_sample_script()
