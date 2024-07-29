import linearequationsystemsolverfilemaker
import chemicalequationrewriter


def execute(input_chemical_equation: str) -> None:

    linear_equations_system_object: object = (
        linearequationsystemsolverfilemaker.LinearEquationSystemSolverFileMaker(
            chemical_equation=input_chemical_equation
        )
    )
    linear_equations_system_object.generateEquationAndSaveSolverFile()
    linear_equations_system_object.executeSolverFile()
    return chemicalequationrewriter.ChemicalReactionRewriter().executeRewriter(
        chemical_equation=input_chemical_equation
    )

