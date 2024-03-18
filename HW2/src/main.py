import subprocess
subprocess.check_call(["pip", "install", "tolatex"])
from tolatex import make_latex, latex_tables, latex_images


def write_to_file(filename, content):
    with open("../artifacts/" + filename, 'w') as file:
        file.write(content)

data1 = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "+"]
]

data2 = [
    ["Recent","Status", "Num"],
    ["Mom","Skipped", "39"],
    ["Mom","Out", "1"],
    ["Bro","In", "1"]

]

latex_code = make_latex(latex_tables([data1]))
write_to_file("table.tex", latex_code)

tables = latex_tables([data1,data2])
images = latex_images(["../src_files/1.png",
                       "../src_files/2.png"])

latex_code = make_latex(images,tables,images,tables, title="hw", author="artem")
write_to_file("doc.tex", latex_code)




# Путь к вашему LaTeX-файлу
tex_file_path = "../artifacts/doc.tex"

# Запускаем pdflatex для генерации PDF
subprocess.run(["C:/texlive/2024/bin/windows/pdflatex.exe", "-output-directory=../artifacts/", tex_file_path])