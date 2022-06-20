import pandas

vegetables = {
    "vegetables": ["Carrot", "Beans", "Potato"],
    "cost": [10, 15, 22]
}

data = pandas.DataFrame(vegetables)

# looping through a row
for (index, row) in data.iterrows():
    print("")
    print(index)
    print(row.vegetables)
    print(row.cost)