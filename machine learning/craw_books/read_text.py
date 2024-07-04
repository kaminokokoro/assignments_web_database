import os
from collections import Counter
from openpyxl import Workbook

# Function to count words in a file
def count_words_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
    return len(words)

def get_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to process files in a directory
def process_directory(directory_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["File Name", "Word Count"])

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory_path, file_name)
            word_count = count_words_in_file(file_path)
            sheet.append([file_name, word_count])

    workbook.save(filename='word_counts.xlsx')

def convert_into_excel(directory_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["File Name", "Word Count", "Content"])

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory_path, file_name)
            print(file_path)
            word_count = count_words_in_file(file_path)
            content = get_content(file_path)
            sheet.append([file_name, word_count, content])

    workbook.save(filename='dataset.xlsx')

# Main function
directory_path = 'text'
# process_directory(directory_path)
convert_into_excel(directory_path)


