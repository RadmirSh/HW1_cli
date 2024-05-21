import subprocess
import string

def check_command_output(command, text, mode='line'):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if mode == 'line':
        if text in result.stdout:
            return True
        else:
            return False
    elif mode == 'word':
        for word in result.stdout.split():
            word_clean = ''.join(char for char in word if char not in string.punctuation)
            if text == word_clean:
                return True
        return False
    

# запуск кода, вывод:
command = "ls -l"
text = "file"
print(check_command_output(command, text, mode='word'))
    
