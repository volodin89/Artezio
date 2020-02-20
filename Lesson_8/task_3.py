import requests
import os
from base64 import b64decode


def echo(path_to_file: str, filename: str):
    url = "https://postman-echo.com/post"
    input_filename = os.path.basename(path_to_file)
    with open(path_to_file, "rb") as input_file:
        with open(filename, "wb") as output_file:
            response = requests.post(url, files={"image": input_file}).json()
            data = response.get('files').get(input_filename)
            file = b64decode(data.split(",", 1)[1])
            output_file.write(file)
    return len(file)
