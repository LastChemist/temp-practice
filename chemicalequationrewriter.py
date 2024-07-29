import os
from sympy import sympify
import equationparser
import util.jsonhandler


class ChemicalReactionRewriter:
    def __init__(self) -> None:

        self.parent_folder_directory = os.path.dirname(__file__)
        self.equation_solution: tuple = ()
        self.chemical_formulas_dict = {}
        self.reactants_list: list[str] = []
        self.products_list: list[str] = []
        # self.last_parameter: str = ""

        self.assigned_reactants_list: list[str] = []
        self.assigned_products_list: list[str] = []

        self.json_handler_object: object = util.jsonhandler.Handler(
            file_path=rf"{self.parent_folder_directory}"
        )
        self.json_handler_object.read()

    def load_equation_solution(self):
        self.equation_solution = sympify(
            self.json_handler_object.content["equation_solution"]
        )
        
