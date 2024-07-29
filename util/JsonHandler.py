import json
import os


class Handler:
    content: dict = {"equation_solution": "", "error_msg": ""}

    def __init__(self, file_path: str, content=content) -> None:
        self.content = content
        self.file_path: str = rf"{file_path}\data.json"
        if not os.path.isfile(self.file_path):
            self.write(content=self.content)

    def write(self, content: dict = content):
        with open(self.file_path, "w") as file:
            json.dump(content, file)

    def read(self):
        with open(self.file_path, "r") as file:
            self.content = json.load(file)