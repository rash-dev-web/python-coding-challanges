# with open("weather_data.csv") as file:
#     weather_dat_list = file.readlines()
# print(weather_dat_list)

# import csv
#
# with open("weather_data.csv") as data_file:
#     weather_data = csv.reader(data_file)
#     print(weather_data)
#     temperatures = []
#     datalist = []
#     for data in weather_data:
#         print(data[1])
#         daily_temp = data[1]
#         datalist.append(daily_temp)
#
#     for daily_data in datalist[1:]:
#         temperatures.append(int(daily_data))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# sum = 0
# for list_data in temp_list:
#     sum += list_data
# print(f"Average: {sum/len(temp_list)}")
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)
# print(data.day)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.temp * 9/5 + 32)

# create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Mir", "Angela"],
#     "scores": [54, 66, 50],
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_csv.csv")


# Squirrel data analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cin_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)
print(cin_squirrels)
print(black_squirrels)

color_dict = {
    "color": ["gray", "black", "cinnamon"],
    "count": [gray_squirrels, black_squirrels, cin_squirrels],
}
new_data = pandas.DataFrame(color_dict)
new_data.to_csv("number3.csv")

# data_list = data["Primary Fur Color"].to_list()
# cin = 0
# gray = 0
# black = 0
# print(len(data_list))
# for color in data_list:
#     if color == "Cinnamon":
#         cin += 1
#     elif color == "Gray":
#         gray += 1
#     else:
#         black += 1
#
# print(cin)
# print(gray)
# print(black)
