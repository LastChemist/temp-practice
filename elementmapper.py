# Docstring by : Copilot
import re


class ElementMapper:
    """
    A utility class for analyzing chemical formulas and mapping element occurrences to their indices.

    This class takes a chemical formula as input and provides a method to map the occurrences of each element in the formula to their indices.

    Attributes:
        chemical_formula (str): The input chemical formula (e.g., 'CH3COOH').

    Methods:
        search(): Analyzes the chemical formula and returns a dictionary of element occurrences mapped to their indices.
    """

    def __init__(self, chemical_formula: str) -> None:
        """
        Constructs an ElementMapper object.

        Args:
            chemical_formula (str): A string representing a chemical formula.
        """
        self.chemical_formula = chemical_formula

    def search(self):
        """
        Analyzes the chemical formula and returns a dictionary of element occurrences mapped to their indices.

        This method uses regular expressions to find all elements in the chemical formula and their indices. It then stores
        these in a dictionary, with the element symbols as keys and a list of their indices as values.

        Returns:
            dict: A dictionary with element symbols as keys and a list of their indices as values.
        """
        pattern = re.compile(r"([A-Z][a-z]*)")
        found_elements = {}

        for match in pattern.finditer(self.chemical_formula):
            element = match.group(1)
            index = match.start()

            if element in found_elements:
                found_elements[element].append(index)
            else:
                found_elements[element] = [index]

        return found_elements
