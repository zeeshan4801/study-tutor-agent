from crewai.tools import BaseTool


class CalculatorTool(BaseTool):

    name="Calculator"

    description="""
    Performs mathematical calculations.
    """


    def _run(self, expression:str):

        try:
            return str(eval(expression))

        except:

            return "Invalid calculation"
