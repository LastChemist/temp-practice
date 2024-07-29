import util.assets
import os
import linearequationsystemgenerator


class LinearEquationSystemSolverFileMaker:

    def __init__(self, chemical_equation: str) -> None:

        self.chemical_equation = chemical_equation
        self.current_directory = os.path.dirname(__file__)
        equation_generator_object = (
            linearequationsystemgenerator.LinearEquationsSystemGenerator(
                chemical_equation=self.chemical_equation
            )
        )

        self.system_of_linear_equations = (
            equation_generator_object.generateEquationSystem()
        )
        self.num_of_variables = (
            equation_generator_object.demand_for_variables_to_solve_count
        )
        self.symbols_list = util.assets.parameter_symbols
        self.variables_str = ""

        for i, symbol in enumerate(self.symbols_list):
            self.variables_str += symbol
            if self.num_of_variables == i:
                break
            else:
                self.variables_str += ","
