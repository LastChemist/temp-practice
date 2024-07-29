import re


class ElementMapper:
    def __init__(self, chemical_formula: str) -> None:
        self.chemical_formula = chemical_formula

    def search(self):
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
