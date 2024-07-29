import re
from collections import Counter


class ElementCounter:
    def __init__(self, chemical_formula: str) -> None:
        self.chemical_formula: str = chemical_formula

    def parse_formula(self):
        def expand(match):
            content, count = match.groups()
            if count == "":
                count = 1
            else:
                count = int(count)
            return content * count

        # Expand parentheses
        while "(" in self.chemical_formula:  # or '[' in formula or '{' in formula:
            self.chemical_formula = re.sub(
                r"\(([^()]+)\)(\d*)", expand, self.chemical_formula
            )
        # Count elements
        element_counts = Counter()
        for element, count in re.findall(r"([A-Z][a-z]*)(\d*)", self.chemical_formula):
            if count == "":
                count = 1
            else:
                count = int(count)
            element_counts[element] += count

        return element_counts
