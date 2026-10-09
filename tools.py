from crewai.tools import BaseTool


class CalculatorTool(BaseTool):

    name: str = "Calculator"

    description: str = (
        "Useful for mathematical calculations. "
        "Input should be a mathematical expression."
    )


    def _run(self, expression: str):

        try:
            result = eval(expression)
            return str(result)

        except Exception:

            return "Unable to calculate expression."
