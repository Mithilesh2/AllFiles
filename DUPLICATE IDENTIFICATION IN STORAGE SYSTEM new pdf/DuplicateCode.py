# import os
# import hashlib
# from tkinter import Tk, filedialog
#
# def select_directory():
#     root = Tk()
#     root.withdraw()
#     directory = filedialog.askdirectory()
#     if directory:
#         print(f"Selected directory: {directory}")
#         return directory
#     else:
#         print("No directory selected.")
#         return None
#
# def find_duplicates(rootdir):
#     hashes = {}
#     image_duplicates = []
#     text_duplicates = []
#     for subdir, dirs, files in os.walk(rootdir):
#         for file in files:
#             filepath = os.path.join(subdir, file)
#             # Check if file is an image
#             if file.lower().endswith(('.png', '.jpg', '.jpeg', '.pptx', '.rar')):
#                 # Generate hash value for the image
#                 with open(filepath, 'rb') as f:
#                     hash = hashlib.sha256(f.read()).hexdigest()
#                 # Check if the hash value already exists in the dictionary
#                 if hash in hashes:
#                     image_duplicates.append((filepath, hashes[hash]))
#                 else:
#                     hashes[hash] = filepath
#             # Check if file is a text file
#             elif file.lower().endswith('.txt'):
#                 # Generate hash value for the file contents
#                 with open(filepath, 'rb') as f:
#                     hash = hashlib.sha256(f.read()).hexdigest()
#                 # Check if the hash value already exists in the dictionary
#                 if hash in hashes:
#                     text_duplicates.append((filepath, hashes[hash]))
#                 else:
#                     hashes[hash] = filepath
#     return image_duplicates, text_duplicates
#
# def remove_duplicates(duplicates):
#     for duplicate in duplicates:
#         os.remove(duplicate[0])
#
# if __name__ == '__main__':
#     # Select directory using tkinter
#     rootdir = select_directory()
#
#     # Find and remove duplicate files
#     if rootdir:
#         image_duplicates, text_duplicates = find_duplicates(rootdir)
#         remove_duplicates(image_duplicates)
#         remove_duplicates(text_duplicates)

#
#
# # import os
# # import hashlib
# # import tkinter as tk
# # from tkinter import filedialog, messagebox
# #
# # def select_directory():
# #     directory = filedialog.askdirectory()
# #     if directory:
# #         return directory
# #     else:
# #         return None
# #
# # def find_duplicates(rootdir):
# #     hashes = {}
# #     image_duplicates = []
# #     text_duplicates = []
# #     for subdir, dirs, files in os.walk(rootdir):
# #         for file in files:
# #             filepath = os.path.join(subdir, file)
# #             # Check if the file is an image
# #             if file.lower().endswith(('.png', '.jpg', '.jpeg', '.pptx', '.rar')):
# #                 # Generate a hash value for the image
# #                 with open(filepath, 'rb') as f:
# #                     hash = hashlib.sha256(f.read()).hexdigest()
# #                 # Check if the hash value already exists in the dictionary
# #                 if hash in hashes:
# #                     image_duplicates.append((filepath, hashes[hash]))
# #                 else:
# #                     hashes[hash] = filepath
# #             # Check if the file is a text file
# #             elif file.lower().endswith('.txt'):
# #                 # Generate a hash value for the file contents
# #                 with open(filepath, 'rb') as f:
# #                     hash = hashlib.sha256(f.read()).hexdigest()
# #                 # Check if the hash value already exists in the dictionary
# #                 if hash in hashes:
# #                     text_duplicates.append((filepath, hashes[hash]))
# #                 else:
# #                     hashes[hash] = filepath
# #     return image_duplicates, text_duplicates
# #
# # def remove_duplicates(duplicates):
# #     for duplicate in duplicates:
# #         os.remove(duplicate[0])
# #
# # def select_folder_and_run():
# #     rootdir = select_directory()
# #     if rootdir:
# #         image_duplicates, text_duplicates = find_duplicates(rootdir)
# #         output_text.insert("end", "Duplicate Images:\n")
# #         display_files(image_duplicates)
# #         output_text.insert("end", "Duplicate Text Files:\n")
# #         display_files(text_duplicates)
# #
# # def display_files(files):
# #     output_text.delete("1.0", "end")
# #     for file in files:
# #         output_text.insert("end", f"File: {file[0]}, Type: {file[1]}\n")
# #
# # def delete_duplicates():
# #     confirmation = messagebox.askyesno("Confirmation", "Do you want to delete the duplicates?")
# #     if confirmation:
# #         remove_duplicates(image_duplicates)
# #         remove_duplicates(text_duplicates)
# #         output_text.insert("end", "\nDuplicates Deleted.\n")
# #     else:
# #         output_text.insert("end", "\nDeletion Process Canceled.\n")
# #
# # # Create the main window
# # main_window = tk.Tk()
# # main_window.title("Duplicate Identification")
# #
# # # Create a text box for displaying output
# # output_text = tk.Text(main_window, wrap="word", height=20, width=60)
# # output_text.pack()
# #
# # # Create a "Select Folder" button
# # select_folder_button = tk.Button(main_window, text="Select Folder", command=select_folder_and_run)
# # select_folder_button.pack()
# #
# # # Create a "Delete Duplicates" button
# # delete_duplicates_button = tk.Button(main_window, text="Delete Duplicates", command=delete_duplicates)
# # delete_duplicates_button.pack()
# #
# # # Initialize lists for storing duplicate files
# # image_duplicates = []
# # text_duplicates = []
# #
# # main_window.mainloop()
#
#
#
# import os
# import hashlib
# import tkinter as tk
# from tkinter import filedialog, messagebox
#
# image_duplicates = []  # Initialize image_duplicates list
# text_duplicates = []   # Initialize text_duplicates list
#
# def select_directory():
#     directory = filedialog.askdirectory()
#     if directory:
#         return directory
#     else:
#         return None
#
# def find_duplicates(rootdir):
#     hashes = {}
#     image_duplicates = []
#     text_duplicates = []
#     for subdir, dirs, files in os.walk(rootdir):
#         for file in files:
#             filepath = os.path.join(subdir, file)
#             # Check if the file is an image
#             if file.lower().endswith(('.png', '.jpg', '.jpeg', '.pptx', '.rar')):
#                 # Generate a hash value for the image
#                 with open(filepath, 'rb') as f:
#                     hash = hashlib.sha256(f.read()).hexdigest()
#                 # Check if the hash value already exists in the dictionary
#                 if hash in hashes:
#                     image_duplicates.append((filepath, hashes[hash]))
#                 else:
#                     hashes[hash] = filepath
#             # Check if the file is a text file
#             elif file.lower().endswith('.txt'):
#                 # Generate a hash value for the file contents
#                 with open(filepath, 'rb') as f:
#                     hash = hashlib.sha256(f.read()).hexdigest()
#                 # Check if the hash value already exists in the dictionary
#                 if hash in hashes:
#                     text_duplicates.append((filepath, hashes[hash]))
#                 else:
#                     hashes[hash] = filepath
#     return image_duplicates, text_duplicates
#
# def remove_duplicates(duplicates):
#     for duplicate in duplicates:
#         os.remove(duplicate[0])  # Use the stored full file path (index 0)
#
# def select_folder_and_run():
#     global image_duplicates, text_duplicates
#     rootdir = select_directory()
#     if rootdir:
#         image_duplicates, text_duplicates = find_duplicates(rootdir)
#         output_text.insert("end", "Duplicate Images:\n")
#         display_files(image_duplicates)
#         output_text.insert("end", "Duplicate Text Files:\n")
#         display_files(text_duplicates)
#
# def display_files(files):
#     output_text.delete("1.0", "end")
#     for file in files:
#         output_text.insert("end", f"File: {file[0]}, Type: {file[1]}\n")
#
# def delete_duplicates():
#     global image_duplicates, text_duplicates
#     confirmation = messagebox.askyesno("Confirmation", "Do you want to delete the duplicates?")
#     if confirmation:
#         remove_duplicates(image_duplicates)
#         remove_duplicates(text_duplicates)
#         output_text.insert("end", "\nDuplicates Deleted.\n")
#     else:
#         output_text.insert("end", "\nDeletion Process Canceled.\n")
#
# # Create the main window
# main_window = tk.Tk()
# main_window.title("Duplicate Identification")
# main_window.configure(bg="black")  # Set background color to black
#
# # Create a Label widget with title in bold and light green color
# title_label = tk.Label(main_window, text="Duplicate Deduction", font=("Helvetica", 14, "bold"), fg="light green", bg="black")
# title_label.pack()
#
# # Create a text box for displaying output
# output_text = tk.Text(main_window, wrap="word", height=20, width=60, bg="black", fg="white")
# output_text.pack()
#
# # Create a "Select Folder" button with green color
# select_folder_button = tk.Button(main_window, text="Select Folder", command=select_folder_and_run, bg="green", fg="white", height=2, width=20)
# select_folder_button.pack()
#
# # Create a "Delete Duplicates" button with red color
# delete_duplicates_button = tk.Button(main_window, text="Delete Duplicates", command=delete_duplicates, bg="red", fg="white", height=2, width=20)
# delete_duplicates_button.pack()
#
# main_window.mainloop()
#
#
#

# import os
# import hashlib
# import tkinter as tk
# from tkinter import filedialog, messagebox
#
# image_duplicates = []
# text_duplicates = []
#
# def select_directory():
#     directory = filedialog.askdirectory()
#     if directory:
#         print(directory)
#         return directory
#     else:
#         return None
#
# def find_duplicates(rootdir):
#     hashes = {}
#     image_duplicates = []
#     text_duplicates = []
#     for subdir, dirs, files in os.walk(rootdir):
#         for file in files:
#             filepath = os.path.join(subdir, file)
#
#             if file.lower().endswith(('.png', '.jpg', '.jpeg', '.pptx', '.rar')):
#
#                 with open(filepath, 'rb') as f:
#                     hash = hashlib.sha256(f.read()).hexdigest()
#
#                 if hash in hashes:
#                     image_duplicates.append((filepath, hashes[hash]))
#                 else:
#                     hashes[hash] = filepath
#
#             elif file.lower().endswith('.txt'):
#
#                 with open(filepath, 'rb') as f:
#                     hash = hashlib.sha256(f.read()).hexdigest()
#
#                 if hash in hashes:
#                     text_duplicates.append((filepath, hashes[hash]))
#                 else:
#                     hashes[hash] = filepath
#     return image_duplicates, text_duplicates
#
# def remove_duplicates(duplicates):
#     for duplicate in duplicates:
#         os.remove(duplicate[0])
#
# def select_folder_and_run():
#     global image_duplicates, text_duplicates
#     rootdir = select_directory()
#     if rootdir:
#         image_duplicates, text_duplicates = find_duplicates(rootdir)
#         output_text.insert("end", "Duplicate Images:\n")
#         display_files(image_duplicates)
#         output_text.insert("end", "Duplicate Text Files:\n")
#         display_files(text_duplicates)
#
# def display_files(files):
#     output_text.delete("1.0", "end")
#     for file in files:
#         output_text.insert("end", f"File: {file[0]}, Type: {file[1]}\n")
#
# def delete_duplicates():
#     global image_duplicates, text_duplicates
#     confirmation = messagebox.askyesno("Confirmation", "Do you want to delete the duplicates?")
#     if confirmation:
#         remove_duplicates(image_duplicates)
#         remove_duplicates(text_duplicates)
#         output_text.insert("end", "\nDuplicates Deleted.\n")
#     else:
#         output_text.insert("end", "\nDeletion Process Canceled.\n")
#
#
# main_window = tk.Tk()
# main_window.title("Duplicate Identification")
# main_window.configure(bg="black")
#
#
# title_label = tk.Label(main_window, text="Duplicate Deduction", font=("Helvetica", 14, "bold"), fg="light green", bg="black")
# title_label.pack()
#
#
# output_text = tk.Text(main_window, wrap="word", height=20, width=60, bg="black", fg="white")
# output_text.pack()
#
#
# select_folder_button = tk.Button(main_window, text="Select Folder", command=select_folder_and_run, bg="green", fg="white", height=2, width=20)
# select_folder_button.pack()
#
#
# delete_duplicates_button = tk.Button(main_window, text="Delete Duplicates", command=delete_duplicates, bg="red", fg="white", height=2, width=20)
# delete_duplicates_button.pack()
#
# main_window.mainloop()

import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

image_duplicates = []
text_duplicates = []

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        print(directory)
        return directory
    else:
        return None

def find_duplicates(rootdir):
    hashes = {}
    image_duplicates = []
    text_duplicates = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = os.path.join(subdir, file)

            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.pptx', '.rar','.docx','.pdf')):
                with open(filepath, 'rb') as f:
                    hash_val = hashlib.sha256(f.read()).hexdigest()

                if hash_val in hashes:
                    image_duplicates.append((filepath, hashes[hash_val]))
                else:
                    hashes[hash_val] = filepath

            elif file.lower().endswith('.txt'):
                with open(filepath, 'rb') as f:
                    hash_val = hashlib.sha256(f.read()).hexdigest()

                if hash_val in hashes:
                    text_duplicates.append((filepath, hashes[hash_val]))
                else:
                    hashes[hash_val] = filepath
    return image_duplicates, text_duplicates

def remove_duplicates(duplicates):
    for duplicate in duplicates:
        os.remove(duplicate[0])

def list_all_files(rootdir):
    all_files = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = os.path.join(subdir, file)
            all_files.append(filepath)
    return all_files

def display_files(files):
    output_text.delete("1.0", "end")
    for file in files:
        output_text.insert("end", f"File: {file}\n")

def remove_duplicates_from_list(files, duplicates):
    return [file for file in files if file not in duplicates]

def select_folder_and_run():
    global image_duplicates, text_duplicates
    rootdir = select_directory()
    if rootdir:
        image_duplicates, text_duplicates = find_duplicates(rootdir)
        all_files = list_all_files(rootdir)
        output_text.insert("end", "All Files in the Selected Folder:\n")
        display_files(all_files)

def delete_duplicates():
    global image_duplicates, text_duplicates
    confirmation = messagebox.askyesno("Confirmation", "Do you want to delete the duplicates?")
    if confirmation:
        all_files = list_all_files(select_directory())
        non_duplicates = remove_duplicates_from_list(all_files, image_duplicates + text_duplicates)
        remove_duplicates(image_duplicates)
        remove_duplicates(text_duplicates)
        display_files(non_duplicates)
        output_text.insert("end", "\nDuplicates Deleted.\n")
    else:
        output_text.insert("end", "\nDeletion Process Canceled.\n")

main_window = tk.Tk()
main_window.title("Duplicate Identification")
main_window.configure(bg="black")

title_label = tk.Label(main_window, text="Duplicate Deduction", font=("Helvetica", 14, "bold"), fg="light green", bg="black")
title_label.pack()

output_text = tk.Text(main_window, wrap="word", height=20, width=60, bg="black", fg="white")
output_text.pack()

select_folder_button = tk.Button(main_window, text="Select Folder", command=select_folder_and_run, bg="green", fg="white", height=2, width=20)
select_folder_button.pack()

delete_duplicates_button = tk.Button(main_window, text="Delete Duplicates", command=delete_duplicates, bg="red", fg="white", height=2, width=20)
delete_duplicates_button.pack()

main_window.mainloop()

