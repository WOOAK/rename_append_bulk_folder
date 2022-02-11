import os

# get list of file/folder in certain path (os.listdir)
# option to put the inserted text in front or back of file name
# Front --> inserted text = "123" change "abc.pdf" to "123abc.pdf"
# Back --> inserted text = "123" change "abc.pdf" to "abc123.pdf"
# Exceptional case for folder which dont have extension

path = r"C:\Users\scakwoo\Desktop\Unrelated work\RQ\Crochet Pattern PDF"

file_list = os.listdir(path)
print(file_list)

option = input("Where you want to insert the text? Front (F) or Back(B)?")
# old_text = input("Old name to be replaced")
inserted_text = input("Insert name")
#
for file in file_list:
    old_file_name = os.path.join(path, file)
    if option == "F":
        new_file_name = inserted_text + file
    else:
        get_extension_position = file.find(".")
        if get_extension_position == -1:
            new_file_name = file + inserted_text
        else:
            extension = file[get_extension_position:]
            name_without_extension = file[:get_extension_position]
            new_file_name = name_without_extension + inserted_text + extension

    os.rename(old_file_name, os.path.join(path, new_file_name))