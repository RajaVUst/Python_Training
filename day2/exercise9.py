file_name1="day2_notes.docx"
file_name2="day2_notes.pdf"


file_names=[file_name1,file_name2]

for i in file_names:
    print(f"{i}:{i.endswith("docx")}")

    
print(file_name1.endswith("docx"))