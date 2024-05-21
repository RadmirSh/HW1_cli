import subprocess

def check_command_output(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if text in result.stdout:
        return True
    else:
        return False