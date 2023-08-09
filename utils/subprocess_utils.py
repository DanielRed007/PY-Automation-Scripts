import os
import subprocess

class SubProcess:
    def __init__(self,value):
        self.value = value

    # execute 
    def execute_subprocess():
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
    
    # run sistem diagnostics on linux os by calling htop
    def run_general_diagnostics():
        try:
            subprocess.run(["htop"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running htop: {e}")
