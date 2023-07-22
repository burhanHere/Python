import platform
import os
# import subprocess


if __name__ == "__main__":
    while True:
        textByUser = str("tum yaha aammb lana ayy ho!!!")
        textByUser = input("Enter your text(_exit_ to exit programs): ")
        if textByUser == "_exit_":
            break
        else:
            if platform.system() == "Windows":
                command = f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{textByUser}');"
            # elif platform.system() == "Linux":
            #     # command = f"espeak\"{textByUser}\""
            #     command = f"subprocess.call([\"espeak\", \"-ven-us\", {textByUser}])"
            # //this part is not working properly i dont have the exact command of text to speech in linux
            elif platform.system() == "Darwin":#mac
                command = f"say {textByUser}"
            else:
                print("Not a suitable OS")
                break
            os.system(command)
