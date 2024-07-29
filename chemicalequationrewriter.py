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

    def load_chemical_formulas_dictionary(self, chemical_equation: str):
        # epo stands for equation parser object
        epo = equationparser.EquationParser(chemical_equation=chemical_equation)
        epo.parse()

        # Note : if you uncomment the followings the output
        for reac in epo.reactants_list:
            reac = reac[1:]
            reac = reac[:-1]
            self.chemical_formulas_dict[reac] = 0
            self.reactants_list.append(reac)

        for prod in epo.products_list:
            prod = prod[1:]
            prod = prod[:-1]
            self.chemical_formulas_dict[prod] = 0
            self.products_list.append(prod)

    def assign_coefficients_to_chemical_formulas_in_equation(self):

        for index, chemical_formula in enumerate(
            list(self.chemical_formulas_dict.keys())
        ):
            self.chemical_formulas_dict[chemical_formula] = self.equation_solution[
                index
            ]

        for reactant in self.reactants_list:
            if self.chemical_formulas_dict[reactant] == 1:
                self.assigned_reactants_list.append(reactant)
            else:
                self.assigned_reactants_list.append(
                    f"{self.chemical_formulas_dict[reactant]} {reactant}"
                )

        for product in self.products_list:
            if self.chemical_formulas_dict[product] == 1:
                self.assigned_products_list.append(product)
            else:
                self.assigned_products_list.append(
                    f"{self.chemical_formulas_dict[product]} {product}"
                )

    def execute_rewriter(self, chemical_equation: str):
        self.loadEquationSolutionInformation()
        # self.substituteSymbolsInSolution()
        self.loadChemicalFormulasDictionary(chemical_equation=chemical_equation)
        self.assignCoefficientsToChemicalFormulas()

        reactants_string: str = ""
        products_string: str = ""

        for reactant in self.assigned_reactants_list:
            reactants_string += f"{reactant} + "

        for product in self.assigned_products_list:
            products_string += f"{product} + "

        reactants_string = reactants_string[:-2]
        products_string = products_string[:-2]

        return f"{reactants_string} = {products_string}"
