# Docstring by : Copilot
import elementcounter


class EquationParser:
    """
    A utility class for parsing chemical equations into individual species and counting element occurrences.

    This class takes a chemical equation as input and provides methods to split the equation into individual species,
    count the occurrences of each element in each species, and parse the entire equation.

    Attributes:
        chemical_equation (str): The input chemical equation.
        equation_splitter (str): The character used to split the equation into reactants and products.
        species_splitter (str): The character used to split the reactants and products into individual species.
        reactants_list (list[str]): The list of reactants in the equation.
        products_list (list[str]): The list of products in the equation.
        parsed_reactants (dict): The parsed reactants with element counts.
        parsed_products (dict): The parsed products with element counts.

    Methods:
        splitIntoSpecies(): Splits the equation into individual species.
        countElementsInChemicalSpecie(): Counts the occurrences of each element in each species.
        parse(): Parses the entire equation.
    """

    def __init__(self, chemical_equation: str) -> None:
        """
        Constructs an EquationParser object.

        Args:
            chemical_equation (str): A string representing a chemical equation.
        """
        self.chemical_equation: str = chemical_equation
        self.equation_splitter: str = "="
        self.species_splitter: str = "+"

        self.reactants_list: list[str] = []
        self.products_list: list[str] = []

        self.parsed_reactants: dict = {}
        self.parsed_products: dict = {}

    def split_equation_into_species(self) -> None:
        """
        Splits the equation into individual species.

        This method splits the equation into reactants and products, and then splits these into individual species.
        It also encloses each species in parentheses if it is not already enclosed.

        Returns:
            None
        """

        # Split the equation into reactants and products
        splitted_equation: list[str] = self.chemical_equation.split(
            self.equation_splitter
        )

        # Split the reactants and products into individual species
        # and enclose each species in parentheses if it is not already
        self.reactants_list = [
            (
                "(" + species.strip() + ")"
                if not species.strip().startswith("(")
                else species.strip()
            )
            for species in splitted_equation[0].split(self.species_splitter)
        ]
        self.products_list = [
            (
                "(" + species.strip() + ")"
                if not species.strip().startswith("(")
                else species.strip()
            )
            for species in splitted_equation[1].split(self.species_splitter)
        ]

    def count_elements_in_chemical_specie(self) -> None:
        """
        Counts the occurrences of each element in each species.

        This method uses the ElementCounter_extended class to count the occurrences of each element in each species.
        It stores these counts in the parsed_reactants and parsed_products dictionaries.

        Returns:
            None
        """

        for reactant in self.reactants_list:
            self.parsed_reactants[reactant] = elementcounter.ElementCounter(
                chemical_formula=reactant
            ).parseFormula()

        for product in self.products_list:
            self.parsed_products[product] = elementcounter.ElementCounter(
                chemical_formula=product
            ).parseFormula()

    def parse(self):
        """
        Parses the entire equation.

        This method first splits the equation into individual species using the splitIntoSpecies method,
        then counts the occurrences of each element in each species using the countElementsInChemicalSpecie method.

        Returns:
            list: A list containing the parsed reactants and parsed products dictionaries.
        """
        self.split_equation_into_species()
        self.count_elements_in_chemical_specie()
        return [self.parsed_reactants, self.parsed_products]
