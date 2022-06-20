import pandas

data = pandas.read_csv("squirrel_data.csv")

grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dci = {
    "Fur Colour": ["Grey", "Red", "Black"],
    "Colour Count": [grey_squirrel, red_squirrel , black_squirrel]
}

new_csv = data.to_csv("squirrel_count")
