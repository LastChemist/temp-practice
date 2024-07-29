import linearequationsystemsolverfilemaker
import chemicalequationrewriter


def execute(input_chemical_equation: str) -> None:

    linear_equations_system_object: object = (
        linearequationsystemsolverfilemaker.LinearEquationSystemSolverFileMaker(
            chemical_equation=input_chemical_equation
        )
    )
    linear_equations_system_object.generate_equations_and_build_solver_file()
    linear_equations_system_object.execute_solver_file()
    return chemicalequationrewriter.ChemicalReactionRewriter().execute_rewriter(
        chemical_equation=input_chemical_equation
    )

