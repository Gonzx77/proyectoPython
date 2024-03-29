from tabulate import tabulate


tipos = [{1, "Personal"}, {2, "Zona"}]
print(tabulate(tipos, headers=["ID", "Tipo"], tablefmt="github"))