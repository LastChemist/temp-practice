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