from sklearn.preprocessing import minmax_scale
# The holdout set has a missing value in the Fare column which
# we'll fill with the mean.
holdout["Fare"] = holdout["Fare"].fillna(train["Fare"].mean())
holdout["Embarked"] = holdout["Embarked"].fillna("S")
train["Embarked"] = train["Embarked"].fillna("S")
holdout = create_dummies(holdout, "Embarked")
train = create_dummies(train, "Embarked")
train["SibSp_scaled"] = minmax_scale(train["SibSp"])
train["Parch_scaled"] = minmax_scale(train["Parch"])
train["Fare_scaled"] = minmax_scale(train["Fare"])
holdout["SibSp_scaled"] = minmax_scale(holdout["SibSp"])
holdout["Parch_scaled"] = minmax_scale(holdout["Parch"])
holdout["Fare_scaled"] = minmax_scale(holdout["Fare"])


import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior', 'Pclass_1', 'Pclass_2', 'Pclass_3',
       'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
       'SibSp_scaled', 'Parch_scaled', 'Fare_scaled']



import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior', 'Pclass_1', 'Pclass_2', 'Pclass_3',
       'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
       'SibSp_scaled', 'Parch_scaled', 'Fare_scaled']
lr = LogisticRegression()

lr.fit(train[columns],train["Survived"])
coefficients = lr.coef_
feature_importance = pd.Series(coefficients[0], index=train[columns].columns)
feature_importance.plot.barh()
plt.show()





def process_fare(df, cut_points, label_names):
	df["Fare_categories"] = pd.cut(df["Fare"], cut_points, labels= label_names)
	return df

cut_points = [0, 12, 50, 100]
label_names = ["0", "12", "50", "100"]
train = process_fare(train, cut_points, label_names)
holdout = process_fare(holdout, cut_points, label_names)



crime_rates = [749, 371, 828, 503, 1379]


# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print (rows[:5])



print(crime_rates)
first_500 = crime_rates[0] > 500

first_749 = crime_rates[0] >= 749
first_last = crime_rates[0] >= crime_rates[-1]



second_500 = crime_rates[1] < 500
second_371 = crime_rates[1] <= 371
second_last = crime_rates[1] <= crime_rates[-1]

if cities[2] == "Anchorage":
	result = 1

both_conditions = False
if crime_rates[0] > 500:
	if crime_rates[1] > 300:
		both_conditions = True


five_hundred_list = []
five_hundred_list.append(value) 
for value in crime_rates:
	if value > 500:

	five_hundred_list.append(value)






fi = open("dq_unisex_names.csv", "r")
names = fi.read()

names_list = names.split("\n")
first_five = names_list[:5]
nested_list = [row.split(",") for row in names_list]
numerical_list = [i, float(j) for i,j in nested_list]


thousand_or_greater = []
for i in numerical_list:
	if i > 1000:
		thousand_or_greater.append(i)

print (thousand_or_greater[:5])



fi = open("dq_unisex_names.csv", "r")
names = fi.read()

names_list = names.split("\n")
first_five = names_list[:5]
weather_data = [row.split(",") for row in names_list]
weather = [i[1] for i in weather_data]



first_element = weather[0]
last_element = weather[-1]

print (first_element)
print (last_element)

superhero_ranks = {}
superhero_ranks["Aquaman"] = 1
superhero_ranks["Superman"] = 2


president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3


fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]



random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)



animals = {}
animals[7] = "raven"
animals[8] = "goose"
animals[9] = "duck"

times = {}
times["morning"] = 9
times["afternoon"] = 14
times["evening"] = 19
times["night"] = 23

students = {
    "Tom": 60,
    "Jim": 70
}


students["Ann"] = 85
students["Tom"] = 80
students["Jim"] = students["Jim"] + 5

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}

jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]

pantry_counts = {}
for i in pantry:
	pantry_counts[i] = pantry_counts.get(i, 0) + 1



weather_counts = {}

for i in weather:
	weather_counts[i] = weather_counts.get(i, 0) + 1

fi = open("movie_metadata.csv", "r")
data = fi.read()
lines = data.split("\n")
movie_data = [line.split(",") for line in lines]
pritn (movie_data[:5])






def first_elts(inp):
	return [row[0] for row in inp]

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

# def is_usa():

# def summary_statistics(movie_data):







import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()




tokenized_headlines = [row["headline"].split(" ") for row in submissions]