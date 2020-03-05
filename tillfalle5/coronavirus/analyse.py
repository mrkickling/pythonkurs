import csv
import operator

csv_file = open('time_series_19-covid-Confirmed.csv')
csv_reader = csv.reader(csv_file, delimiter=';')
line_count = 0

# Dictionaryn nedan kommer fyllas med länders namn och deras antal coronafall
# T.ex. { "Sweden": 3, "Norway": 10} osv..
cases_per_country = {}

for row in csv_reader:
    if line_count == 0:
        print("Column names are", ", ".join(row))
    else:
        country = row[1]
        num_cases = int(row[2])
        if country in cases_per_country:
            cases_per_country[country] += num_cases
        else:
            cases_per_country[country] = num_cases
    line_count += 1

csv_file.close()

# Let the user ask for a specific countries number of cases
country_name = input("What country are you interested in? ")
if country_name in cases_per_country:
    print(cases_per_country[country_name], "confirmed cases in", country_name)

# Make into list of tuples, sort them
country_cases = []
for country in cases_per_country:
    country_cases.append((country, cases_per_country[country]))
# Sort by second element (num cases)
country_cases.sort(key = operator.itemgetter(1), reverse=True)

show = input("Would you like to see the full list of countries? (y/n)")
if show == "y"

# Print the maximum and minimum country num infected
max_country = max(cases_per_country, key=cases_per_country.get)
max_value = cases_per_country[max_country]
print("Most cases in", max_country, ":", max_value)

min_country = min(cases_per_country, key=cases_per_country.get)
min_value = cases_per_country[min_country]
print("Least cases in", min_country, ":", min_value)

# Calculate total amount of cases
num_cases = 0
for country in cases_per_country:
    num_cases += cases_per_country[country]
print("Total number of cases world wide:", num_cases)
