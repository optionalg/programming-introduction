"""
Aula 9
Exercícios Extras 4

Autor: Lucien Constantino
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


price = float(input("Valor da Xerox: R$ "))
rows = 10
columns = 10

row_count = 0
while row_count < rows:

    column_count = 0
    line_message = ""
    while column_count < columns:

        copies = ((row_count) * 10) + (column_count+1)

        line_message += bcolors.HEADER + \
                        "{0}".format(copies) + \
                        bcolors.ENDC + \
                        " = " + \
                        bcolors.OKBLUE + \
                        "{0:.2f}".format(price * copies) +\
                        bcolors.ENDC +\
                        " "

        column_count += 1

    row_count += 1
    print(line_message)
