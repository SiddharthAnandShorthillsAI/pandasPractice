import os
import requests

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

folder_name = "input_files"
file_name = "chipotle.tsv"
file_path = os.path.join(folder_name, file_name)

os.makedirs(folder_name, exist_ok=True)

response = requests.get(url)
if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"File saved successfully at: {file_path}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
