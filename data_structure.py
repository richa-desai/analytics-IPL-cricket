''' This is a review problem '''
input_data = [
    {
        "expense_name": "trip",
        "paid_by": "prashant",
        "dues": {
            "ashok": 150,
            "fabian": 250
        }
    },
    {
        "expense_name": "groceries",
        "paid_by": "ashok",
        "dues": {
            "prashant": 100,
            "akshay": 150,
            "shashi": 300
        }
    },
    {
        "expense_name": "movie",
        "paid_by": "prashant",
        "dues": {
            "shashi": 300,
            "fabian": 100
        }
    },
    {
        "expense_name": "bus tickets",
        "paid_by": "akshay",
        "dues": {
            "prashant": 300,
            "fabian": 100
        }
    }
]

# processed_data = {}
# for record in input_data:
#     record["paid_by"] = processed_data.get(record["paid_by"], {})
#     for person in record["dues"]:
#         processed_data[record["paid_by"]][person] = (
#             processed_data[record["paid_by"]].get(person, 0)
#             + record["paid_by"][person])

# print(record)

all_dues = {}
for record in input_data:
    record = record["dues"]
    for item in record.items():
        all_dues[item[0]] = all_dues.get(item[0], 0) + item[1]

print(all_dues)
