"""
    Generate Hash for given file.
    Spark Technology, Nepal
"""
__author__ = "Satshree Shrestha"

try:
    import hashlib
    import sys
    import os
    import pyperclip
    # import warnings
    # warnings.filterwarnings("ignore", category=DeprecationWarning)
    from tkinter.filedialog import askopenfilename
except:
    print("Unable to import libraries, make sure Python Library 'pyperclip' is installed in your system.")
    exit(0)

print("-" * 100)
print("Generate MD5 Hash For Given File.")

# hash = hashlib.md5()

while True:
    try:
        print("-" * 100)

        if sys.platform == "win32":
            dir = "/"
        else:
            dir=os.path.dirname(os.path.realpath(__file__))

        input("Press Enter to select a file to generate hash.\n")
        file_path = askopenfilename(initialdir=dir)

        if not file_path:
            print("-" * 100)
            exit_ = input("Exit? [y/n]: ")
            if exit_.lower() in ('y', 'yes'):
                raise KeyboardInterrupt
            else:
                continue
    except KeyboardInterrupt:
        print("\n\n>> Exiting \n\n")
        exit(0)

    try:
        with open(file_path, 'rb') as bin:
            contents = bin.read()
            hash = hashlib.md5(contents)

            # for contents in iter(lambda: bin.read(4096)):
            #     hash.update(contents)
    except FileNotFoundError:
        print("File Not Found.")
        continue
    except Exception as e:
        print("Exception caught:", e)
        continue

    print("-" * 100)

    if "/" in file_path:
        file_name = file_path.split("/")[-1]
    else:
        file_name = file_path

    hash_value = hash.hexdigest()
    print("File '{}' Hash:".format(file_name))
    print("")
    print(hash_value)
    print("")
    pyperclip.copy(hash_value)
    print("Hash value copied to clipboard.\n")
