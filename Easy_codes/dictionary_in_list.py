travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(new_country, no_of_visits, cities_visited):
    new_country_dict = {}
    new_country_dict["country"] = new_country
    new_country_dict["visits"] = no_of_visits
    new_country_dict["cities"] = cities_visited
    # print(new_country_dict)
    travel_log.append(new_country_dict)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
