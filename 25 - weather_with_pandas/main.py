# with open("weather_data.csv", mode="r") as list:
#     data = list.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temp = data["temp"]
# temp_list = temp.tolist()
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# # print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# farenheight = (1.8 * monday_temp) + 32
# print(farenheight)


import pandas
data = pandas.read_csv("squirrel_census.csv")
black_count = len(data[data["Primary Fur Color"] == "Black"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")