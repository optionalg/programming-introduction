class Employee:
    def __init__(self, name, gender, salary):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.adjusted_salary = adjusted_salary(salary)


def get_gender():
    while True:
        gender = input("Digita o gênero (M/F): ")
        if gender != "M" and gender != "F":
            print("Gênero inválido.")
        else:
            return gender


def get_salary():
    while True:
        salary = float(input("Digite o salário: "))
        if salary < 850:
            print("Salário deve ser pelo menos R$ 850")
        else:
            return salary


def adjusted_salary(salary):
    if salary < 2000:
        new_salary = salary * (1 + 8.5/100)
        tier = 1
    elif 2000 <= salary < 3000:
        new_salary = salary * (1 + 6.5/100)
        tier = 2
    else:
        new_salary = salary * (1 + 4.5/100)
        tier = 3
    return [new_salary, tier]


employee_count = int(input("Quantidade de empregados: "))
employees = []
tier_2_salary_adjust_count = 0

men_count = 0
women_count = 0
sum_of_adjusted_salary_for_men = 0

for i in range(employee_count):

    name = input("Nome do empregado: ")
    gender = get_gender()
    salary = get_salary()

    employee = Employee(name, gender, salary)
    employees.append(employee)

    # check if employee has received a tier 2 raise
    if employee.adjusted_salary[1] == 2:
        tier_2_salary_adjust_count += 1

    if gender == "M":
        men_count += 1
    else:
        women_count += 1

    print("{0} teve salário reajustado para {1:.2f}".format(employee.name, employee.adjusted_salary[0]))


print("Quantidade de empregados que receberam reajuste de 6,5%: {0}".format(tier_2_salary_adjust_count))

if men_count > 0:
    average_of_adjusted_salary_for_men = sum_of_adjusted_salary_for_men / men_count
    print("Salário reajustado médio entre os empregados do sexo masculino: {0:.2f}".format(average_of_adjusted_salary_for_men))

if women_count > 0:
    women_percent_total = 100 * (women_count / employee_count)
    print("% empregados do sexo feminino entre o total: {0:.1f}%".format(women_percent_total))
