from crewai.tools import BaseTool


class CalculatorTool(BaseTool):

    name: str = "Calculator"

    description: str = """
    Useful for solving mathematical calculations.
    Input should be a mathematical expression.
    Example:
    25*10
    """

    def _run(self, expression: str):

        try:

            answer = eval(expression)

            return str(answer)

        except Exception:

            return "Cannot calculate this expression."
