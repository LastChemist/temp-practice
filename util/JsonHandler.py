# Docstring by : Copilot
import json
import os


class Handler:
    """
    A class to handle operations on a JSON file.

    Attributes:
        content (dict): A dictionary to store the content of the JSON file.
        file_path (str): The path of the JSON file.
    """

    content: dict = {"equation_solution": "", "error_msg": ""}

    def __init__(self, file_path: str, content=content) -> None:
        """
        The constructor for Handler class.

        Parameters:
            file_path (str): The path of the JSON file.
            content (dict, optional): The content to write into the JSON file. Defaults to class attribute 'content'.
        """
        self.content = content
        self.file_path: str = rf"{file_path}\data.json"
        if not os.path.isfile(self.file_path):
            self.write(content=self.content)

    def write(self, content: dict = content):
        """
        Writes the content into the JSON file.

        Parameters:
            content (dict, optional): The content to write into the JSON file. Defaults to class attribute 'content'.
        """
        with open(self.file_path, "w") as file:
            json.dump(content, file)

    def read(self):
        """
        Reads the content from the JSON file and updates the 'content' attribute.
        """
        with open(self.file_path, "r") as file:
            self.content = json.load(file)

    def update(self, key: str, value: any):
        """
        Updates a specific key in the JSON file with a new value.

        Parameters:
            key (str): The key in the JSON file to update.
            value (any): The new value to update the key with.
        """
        self.read()
        self.content[key] = value
        self.write(content=self.content)

    def remove_json_file(self):
        """
        Removes the JSON file if it exists.
        """
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)
