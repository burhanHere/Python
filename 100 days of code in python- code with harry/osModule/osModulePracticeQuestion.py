import os

# print(os.getcwd())# print(os.name)#let's which operating system is this.
# os.chdir(".\osModule")
# print(os.getcwd())

# if not os.path.exists("practice"):
#     os.mkdir("practice")#create a directory/folder at any path ,we can also pass a path in this fucntion
#     print("File created👍")

# if not os.path.exists("practice\cowBoy"):
#     os.makedirs("practice\cowBoy")#create all the directories/folders which are given in this functuion at any path
#     print("File created👍")

# listOfDir=os.listdir()#return a list of all the files and folders in current working directory
# print(listOfDir)

print(os.environ)#The os.environ value is known as a mapping object that returns a dictionary of the user’s environmental variables. You may not know this, but every time you use your computer, some environment variables are set. These can give you valuable information, such as number of processors, type of CPU, the computer name, etc. there are to mode methos related to this os.getenv(soem arg here) os.putenv(name, value)