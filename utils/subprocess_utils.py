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
    
    # run system diagnostics on linux os by calling htop
    def run_general_diagnostics():
        try:
            subprocess.run(["htop"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running htop: {e}")
    
    # check space management in os
    def check_available_space():
        command = ["df", "-h"]

        try:
            exec = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print("Standard Output:")
            print(exec.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running htop: {e}")
