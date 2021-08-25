# Program for calculating the accumulated funds for a year of deposit in each of the banks

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Enter the amount of money you plan to deposit: "))
deposit = [int(round(val * money * 0.01)) for val in per_cent.values()]
print(f"deposit = {deposit}")
i = deposit.index(max(deposit))
print(f"Maximum amount you can earn - {deposit[i]}")