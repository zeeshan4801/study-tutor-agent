from crewai.tools import BaseTool


class CalculatorTool(BaseTool):

    name: str = "Calculator"

    description: str = """
    Calculate mathematical expressions.
    Example:
    25*10
    """

    def _run(self, expression: str):

        try:
            return str(eval(expression))

        except Exception:

            return "Invalid calculation"
