from crewai.tools import BaseTool


class CalculatorTool(BaseTool):

    name: str = "Calculator"

    description: str = """
    Use this tool for mathematical calculations.
    Example input:
    25*5
    """


    def _run(self, expression: str):

        try:

            return str(eval(expression))

        except:

            return "Calculation error"
