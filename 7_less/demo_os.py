import os

def domo_os_base():
    print(os.name)

    os.environ["SECRET"] = "123"
    #print(os.environ)
    print(os.environ["PATH"])
    print(os.environ["HOME"])
    print(os.environ["SECRET"])
    #print(os.environ["PYTHONUNBUFFERED"])
    cwd = os.getcwd()
    print(cwd)

    subdir = os.path.join(cwd, "subdir")
    print("subdir", subdir)
    subdir_123 = os.path.join(cwd, "subdir2","123", "4443")
    print("subdir_123= ", subdir_123)


    if not os.path.isdir(subdir):
        #os.makedirs() #create all folders if there is no here
        os.mkdir(subdir) #only needed folder
    else:
        print('Folder is exists')
        
    os.chdir(subdir)
    print(os.getcwd())


def demo_file():
        
    file_name = "file.txt"
    
    with open(file_name, "w"):
        pass

    print(os.listdir("."))

    os.remove(file_name)

    print(os.stat("."))
    

        
def domo_walk():
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        print("root:", root)
        print("dirs:")
        for d in dirs:
            print("-", d)
        print("files:")
        for d in files:
            print("-", d)
            
cwd = os.getcwd()
print("cwd: ",cwd)
print("base name cwd:", os.path.basename(cwd))
print("dir name cwd:", os.path.dirname(cwd))

print(os.path.exists(cwd))

print(os.path.split(cwd))

domo_os_base()