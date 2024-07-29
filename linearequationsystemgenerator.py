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

    def present_elements_in_chemical_formula(self, chemical_formula: str) -> list:
        return list(
            elementmapper.ElementMapper(chemical_formula=chemical_formula).search()
        )

    def present_elements_in_reaction(self) -> list:

        element_list: list[str] = []
        temp_list: list = []
        reactants_list: list[str] = self.reactants_list
        products_list: list[str] = self.products_list

        for reactant in reactants_list:
            temp_list.append(
                self.present_elements_in_chemical_formula(chemical_formula=reactant)
            )

        for product in products_list:
            temp_list.append(
                self.present_elements_in_chemical_formula(chemical_formula=product)
            )

        for sublist in temp_list:
            element_list.extend(sublist)

        element_list = list(set(element_list))
        self.present_elements_in_reaction = element_list
        self.demand_for_variables_to_solve_count = len(self.reactants_list) + len(
            self.products_list
        )  # Junior code, fix the formula

    def assign_parameter(self) -> None:

        self.present_elements_in_reaction()
        removing_index: int = 0

        for i, reactant in enumerate(self.reactants_list):
            self.reactants_assigned_parameter_dict[reactant] = self.parameter_symbols[i]
            removing_index = i

        self.parameter_symbols = self.parameter_symbols[removing_index + 1 :]

        for i, product in enumerate(self.products_list):
            self.products_assigned_parameter_dict[product] = self.parameter_symbols[i]
            removing_index = i

        self.parameter_symbols = self.parameter_symbols[removing_index + 1 :]

    def generate_equations_system(self) -> list:

        self.assign_parameter()
        equations_list: list[str] = []
        equation: str = ""
        left_hand: str = ""
        right_hand: str = ""

        for element in self.present_elements_in_reaction:
            for reactant in self.reactants_list:
                if element in self.parsed_reactants[reactant]:
                    left_hand += f"{self.parsed_reactants[reactant][element]}*{self.reactants_assigned_parameter_dict[reactant]}+"

            for product in self.products_list:
                if element in self.parsed_products[product]:
                    right_hand += f"{self.parsed_products[product][element]}*{self.products_assigned_parameter_dict[product]}-"

            left_hand = left_hand[:-1]
            right_hand = right_hand[:-1]

            equation = f"{left_hand}-{right_hand}"
            equations_list.append(equation)
            left_hand = ""
            right_hand = ""

        return equations_list
