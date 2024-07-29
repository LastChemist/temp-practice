import elementcounter


class EquationParser:
    def __init__(self, chemical_equation: str) -> None:

        self.chemical_equation: str = chemical_equation
        self.equation_splitter: str = "="
        self.species_splitter: str = "+"

        self.reactants_list: list[str] = []
        self.products_list: list[str] = []

        self.parsed_reactants: dict = {}
        self.parsed_products: dict = {}

    def split_equation_into_species(self) -> None:

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
