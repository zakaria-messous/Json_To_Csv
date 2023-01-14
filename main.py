import json
import pandas as pd

def export_to_csv():
    with open("data.json") as f:
        list1 = []
        data = json.loads(f.read())
        temp = data[0]
        header_items = ["firstName","lastName"]
        list1.append(header_items)
      
        for obj in data:
            d = []
            d.append(obj["firstName"])
            d.append(obj["lastName"])
            list1.append(d)
        
        with open('output.csv', 'w') as output_file:
            for a in list1:
                output_file.write(','.join(map(str, a)) + "\n")
    df = pd.read_csv('output.csv')
    df.to_excel('output.xlsx', index=False)

export_to_csv()