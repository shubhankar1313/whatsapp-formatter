# from fpdf import FPDF

file = open("dataset\smaller sample.txt", "r", encoding="utf8")
content=file.readlines()
print(content)
file.close()

for entry in content:
    print(entry)