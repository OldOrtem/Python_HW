


def generate_latex_table(data):
    if not data:
        return ''

    rows = len(data)
    cols = len(data[0])
    latex_code = "\\begin{table}[H]\n"
    latex_code += "\\centering\n"
    latex_code += "\\begin{tabular}{|" + "c|" * cols + "}\n"

    latex_code += "\\hline\n"
    stringify_row = lambda row: " & ".join(map(str, row)) + " \\\\ \\hline\n"
    latex_rows = "".join(map(stringify_row, data))

    latex_code += latex_rows
    latex_code += "\\end{tabular}\n"
    latex_code += "\\end{table}\n"

    return latex_code

def latex_tables(tables):
    for table in tables:
        yield generate_latex_table(table)


def generate_latex_image(image_path):
    latex_code = "\\begin{figure}[H]\n"
    latex_code += "\\centering\n"
    latex_code += "\\includegraphics[width=0.5\linewidth]{" + image_path + "}\n"
    latex_code += "\\caption{" + image_path.split("/")[-1] + "}\n"
    latex_code += "\\end{figure}\n"
    return latex_code

def latex_images(images):
    for image in images:
        yield generate_latex_image(image)
# в аргс передаются функции, в кваргс передаются параметры, которые будут наверху документа, типа тайтл, имя, дата
def make_latex(*args, **kwargs):
    latex_code = "\\documentclass{article}\n"
    latex_code += "\\usepackage{graphicx}\n"
    latex_code += "\\usepackage{float}"

    format_key_value = lambda key, value: "\\" + str(key) + "{" + str(value) + "}\n"
    latex_code += ''.join(map(lambda item: format_key_value(*item), kwargs.items()))

    latex_code += "\\begin{document}\n"
    latex_code += "\\maketitle\n"

    latex_code += ''.join(map(lambda func: next(func), args))

    latex_code += "\\end{document}"
    return latex_code