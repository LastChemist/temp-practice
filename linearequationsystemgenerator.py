import util.assets
import elementmapper
import equationparser


class LinearEquationsSystemGenerator:
    def __init__(self, chemical_equation: str) -> None:
        """
        Constructs a LinearEquationSystemGenerator object.

        Args:
            chemical_equation (str): A string representing a chemical equation.
        """
        self.chemical_equation: str = chemical_equation

        self.parameter_symbols: str = util.assets.parameter_symbols
        # Junior code, BUG, fix it
        equation_parser_object: object = equationparser.EquationParser(
            chemical_equation=chemical_equation
        )
        equation_parser_object.parse()
        #
        self.reactants_list: list[str] = equation_parser_object.reactants_list
        self.products_list: list[str] = equation_parser_object.products_list

        self.present_elements_in_reaction: list[str] = []

        self.parsed_reactants: dict[str, dict[str, str]] = (
            equation_parser_object.parsed_reactants
        )
        self.parsed_products: dict[str, dict[str, str]] = (
            equation_parser_object.parsed_products
        )
        self.reactants_assigned_parameter_dict: dict[str, str] = {}
        self.products_assigned_parameter_dict: dict[str, str] = {}
        self.demand_for_variables_to_solve_count: int = 0
        self.parametric_equations_list: list[str] = []

    def parse_elements_in_chemical_formula(self, chemical_formula: list):
        return list(
            elementmapper.ElementMapper(chemical_formula=chemical_formula).search()
        )

    def present_elements_in_formula(self, chemical_formula: str) -> list:
        return list(
            elementmapper.ElementMapper(chemical_formula=chemical_formula).search()
        )

    def present_elements_in_reaction(self) -> list:

        element_list: list[str] = []
        temp_list: list = []
        reactants_list: list[str] = self.reactants_list
        products_list: list[str] = self.products_list

        for reactant in reactants_list:
            temp_list.append(self.presentElementsInFormula(chemical_formula=reactant))

        for product in products_list:
            temp_list.append(self.presentElementsInFormula(chemical_formula=product))

        for sublist in temp_list:
            element_list.extend(sublist)

        element_list = list(set(element_list))
        self.present_elements_in_reaction = element_list
        self.demand_for_variables_to_solve_count = len(self.reactants_list) + len(
            self.products_list
        )  # Junior code, fix the formula

    def assign_parameter(self) -> None:

        self.presentElementsInReaction()
        removing_index: int = 0

        for i, reactant in enumerate(self.reactants_list):
            self.reactants_assigned_parameter_dict[reactant] = self.parameter_symbols[i]
            removing_index = i

        self.parameter_symbols = self.parameter_symbols[removing_index + 1 :]

        for i, product in enumerate(self.products_list):
            self.products_assigned_parameter_dict[product] = self.parameter_symbols[i]
            removing_index = i

        self.parameter_symbols = self.parameter_symbols[removing_index + 1 :]
