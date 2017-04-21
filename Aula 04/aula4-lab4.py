import math
# Aula 4
# Exercício Laboratorio 4
eventCost = float(input("Type the event cost: "))
ticketPrice = float(input("Type the ticket price: "))

numberOfTicketsBreakEven = math.ceil(eventCost / ticketPrice)
numberOfTickets23Profit = math.ceil((eventCost * 1.23) / ticketPrice) 

print("Number of tickets for break even: {0}".format(numberOfTicketsBreakEven))
print("Number of tickets for 23% profit: {0}".format(numberOfTickets23Profit))
