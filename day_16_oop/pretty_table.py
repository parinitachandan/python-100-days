from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",
                 ["Pikachu", "Azurill", "Squirtle"])
table.add_column("Type",
                 ["Electric", "Fairy", "Water"])
print(table)

table.align = "l"    # left aligned; c = center; r = right
table.vertical_char = "|"
table.junction_char = "*"
table.horizontal_char = "_"
table.header_style = "upper"

print(table)
