import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))  # checking the type of the data
print("")

data_dic = data.to_dict()
print(data_dic)  # converts the data into a dictionary
print("")

temp_list = data.temp.to_list()  # converts the data into a list
print(temp_list)
print("")

print(data.temp.mean())  # returns the average of the data
print("")

print(data.temp.max())  # returns the max of the data
print("")

# data in column
print(data.condition)
print("")

# data in row
print(data[data.day == "Monday"])
print("")

print(data[data.temp == data.temp.max()])
print("")

monday = data[data.day == "Monday"]
monday_temp_far = int(monday.temp) * 9 / 5 + 32
print(monday_temp_far)
print("")

# create a dataframe from scratch
vegetables = {
    "vegetables": ["Carrot", "Beans", "Potato"],
    "cost": [10, 15, 22]
}
data_veges = pandas.DataFrame(vegetables)
data_veges.to_csv("new_data.csv")
print(data_veges)


