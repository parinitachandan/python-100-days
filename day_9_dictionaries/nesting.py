# Nesting
captials = {"France": "Paris",
            "Germany": "Berlin"}

# Nesting a list in a dictionary
travel_log = {"France": ["Paris", "Lille", "Dijon"],
              "Germany": ["Berlin", "Hamburg", "Stuttgart"]}
print(travel_log)

# Nesting a list inside a list - not quiet useful
fruits = ["Apples", "Bananas", "Grapes", ["Watermelon", "Blueberries", "Cherry"]]
print(fruits)

# Nesting a dictionary in a dictionary
seasons = {
    "Summer": {"Months": ["March", "April", "May", "June", "July"], "Total months": 5},
    "Monsoon": {"Months": ["August", "September", "October"], "Total months": 3},
    "Winter": {"Months": ["November", "December", "January", "February"], "Total months": 4}
}
print(seasons)

# Nesting a dictionary in a list
countries = [
    {"Country": "France",
     "Capital": "Paris",
     "Famous": "Eiffel Tower"},

    {"Country": "Germany",
     "Capital": "Berlin",
     "Famous": "Art scene and modern landmarks"}
]


def add_new_country(name, capital, famous_for):
    new_country = {}
    new_country["Country"] = name
    new_country["Capital"] = capital
    new_country["Famous"] = famous_for
    countries.append(new_country)


add_new_country("Russia", "Moscow", "Red Square")
print(countries)

