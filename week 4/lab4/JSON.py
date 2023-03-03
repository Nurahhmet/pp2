import json

with open('sample_data.json', 'r') as sample_file:
     sample_data = json.load(sample_file)
     print(sample_data)