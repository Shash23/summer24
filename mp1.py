# q1
val = 11/7
type(val)

#q2
fruit_list = ["apple", "pear", "banana", "watermelon"]
fruit_list_length = len(fruit_list) # Don't hardcode this. Use a Python built-in

minimum = 2
maximum = 5
in_range = minimum <= fruit_list_length <= maximum ???? # True if the number of fruits in fruit_list is inside the minimum-to-maximum range
in_range

#q3
filepaths = "TESTING_FILE1.C5V-TESTING_FILE2.CSV-TESTING_FILE3.CSV"
file_list = filepaths.split('-')
csv_count = 0
for file in file_list:
    if file.lower().endswith('.csv'):
        csv_count += 1
csv_count

#q4
def multiply(a, b = 2):
    return a * b

def smart_multiply(nums):
    
    ans = 1
    
    for i in nums:
    
        if num <= 0:
            continue
    
        ans *= i
    
        if ans > 100:
            break
        
    return ans

smart_multiply([4, -2, 0, 5, 5, 2, 7, -2])

#q6

header = ["A", "B", "C"]

coord1 = {"x": 8, "y": 5}
coord2 = {"x": 9, "y": 2, "z" : 4}
coord3 = {"x": 3, "y": 1, "z" : 7}

rows = [
    [1, 6, 7, 8, coord1],
    [3, 4, 9, coord2],
    [5, 2, coord3],
]

coord1["z"] = 6
rows

#q7

rows[-1][-1]["y"]

#q8

import copy
v2 = copy.deepcopy(rows)
v2[0] = 404
v2[1][1] = 404

#q9

ans = header.index("A")
ans = sum(row[ans] for row in rows if len(row) > ans)
ans

#q10
rows.sort(key=lambda row: row[header.index("B")], reverse=True)

#q11
import json

with open("usd.json", "r") as f:
    data = json.load(f)

print(type(data))
print(list(data.keys())[:5])

cad_rate = data['cad']['rate']
cad_rate

usd_amount = 400
cad_amount = usd_amount * cad_rate

cad_amount = round(cad_amount, 2)
cad_amount


   
   
   
#q12

def convert_to_int(value):
    try:
        
        return int(value)
    
    except ValueError:
        
        print("Could not convert string to int.")
        return None
    
    except Exception:
        
        print("Error with your input argument.")
        return None

convert_to_int("320")

# q13
convert_to_int("ninety-nine")

# q14
convert_to_int([3, 2, 0])

# q15

import os
import pandas as pd

grade_data_path = "grade-data"

grades = {}


for filename in os.listdir(grade_data_path):

    if filename.endswith(".csv"):
        year = int(filename.split('-')[-1].replace('.csv', ''))
        file_path = os.path.join(grade_data_path, filename)
        df = pd.read_csv(file_path)
        df.set_index('course', inplace=True)
        
        
        grades[year] = df



asc_keys = sorted(grades.keys())
asc_keys

# q16

comp_sci_320_gpa_2022 = grades[2022].loc['COMP SCI 320', 'gpa']
comp_sci_320_gpa_2022

# q17

comp_sci_2022_df = grades[2022].loc[grades[2022]["course_abbr"] == "COMP SCI"]
num_comp_sci_courses_2022 = comp_sci_2022_df.shape[0]
num_comp_sci_courses_2022

# q18

total_a_count_2022 = comp_sci_2022_df["a_count"].sum()
total_a_count_2022

# q19

smallest_a_fraction_2022 = (comp_sci_2022_df["a_count"] / comp_sci_2022_df["total"]).min()
smallest_a_fraction_2022

# q20

a_fraction_300_399_2022 = comp_sci_300_399_2022_df["a_count"] / comp_sci_300_399_2022_df["total"]


ax = a_fraction_300_399_2022.plot.bar(
    figsize=(10, 6), 
    title="Fraction of Students Receiving an A in COMP SCI Courses (300-399) in 2022"
)
ax.set_xlabel("Course")
ax.set_ylabel("Fraction of Students Receiving an A")

import matplotlib.pyplot as plt
plt.show()








