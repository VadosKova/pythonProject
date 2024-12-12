#Задание 1, 2, 3
from tkinter import *
import os

def hello():
    print("Hello world")

def analyze():
    path = entry.get()
    condition = c1.get()
    additional_info = c2.get()

    files_count = 0
    folders_count = 0
    images_count = 0
    music_count = 0
    documents_count = 0
    archives_count = 0

    if not os.path.exists(path):
        result.config(text="Путь не найден")
        return

    items = os.listdir(path)

    image_types = ['.jpg', '.jpeg', '.png', '.gif']
    music_types = ['.mp3', '.wav', '.wma']
    document_types = ['.txt', '.docx', '.xlsx', '.pptx', '.pdf']
    archive_types = ['.zip', '.rar', '.7z']

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            folders_count += 1
            if condition:
                sub_items = os.listdir(item_path)
                for sub_item in sub_items:
                    if os.path.isfile(os.path.join(item_path, sub_item)):
                        files_count += 1
                        file_type = os.path.splitext(sub_item)[1].lower()
                        if file_type in image_types:
                            images_count += 1
                        elif file_type in music_types:
                            music_count += 1
                        elif file_type in document_types:
                            documents_count += 1
                        elif file_type in archive_types:
                            archives_count += 1
        else:
            files_count += 1
            file_type = os.path.splitext(item)[1].lower()
            if file_type in image_types:
                images_count += 1
            elif file_type in music_types:
                music_count += 1
            elif file_type in document_types:
                documents_count += 1
            elif file_type in archive_types:
                archives_count += 1

    result_info = f"Количество файлов: {files_count}\nКоличество папок: {folders_count}"

    if additional_info:
        result_info += f"\nИзображения: {images_count}\nМузыка: {music_count}\nДокументы: {documents_count}\nАрхивы: {archives_count}"

    result.config(text=result_info)

root = Tk()
root.geometry("400x250")
root.title("Файлы/Папки")

label = Label(root, text="Путь:")
label.pack()

entry = Entry(root, width=40)
entry.pack()

c1 = IntVar()
nested_checkbox = Checkbutton(root, text="Вложенные файлы", variable=c1)
nested_checkbox.pack()

c2 = IntVar()
additional_info_checkbox = Checkbutton(root, text="Доп. информация", variable=c2)
additional_info_checkbox.pack()

analyze_button = Button(root, text="Analyze", command=analyze)
analyze_button.pack()

result = Label(root, text="", font=("Calibri", 14))
result.pack()

root.mainloop()