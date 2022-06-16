import csv

with open("weather_data.csv") as data_file:
    weather_data = csv.reader(data_file)
    temperatures =[]
    for row in weather_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        print(temperatures)


