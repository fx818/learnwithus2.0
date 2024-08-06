import sys
import io

class CodeRunner:
    def __init__(self):
        self.code = ""

    def set_code(self, code):
        self.code = code

    def run_code(self, inputs):
        # Create a temporary module to execute the code
        temp_module = {}
        exec(self.code, globals(), temp_module)

        # Get the function to execute from the module
        func = temp_module.get("main", None)

        if func:
            outputs = []
            for inp in inputs:
                input_file = io.StringIO(inp)
                sys.stdin = input_file
                output = io.StringIO()
                sys.stdout = output
                func()
                sys.stdout = sys.__stdout__
                outputs.append(output.getvalue())
            return outputs
        else:
            return ["Error: No main function found"]

    def test_code(self, testcases):
        outputs = []
        for testcase in testcases:
            inputs, expected_output = testcase
            outputs.append(self.run_code([inputs]))
        return outputs
    

def returnOutput(code):
    code_runner = CodeRunner()
    code_runner.set_code(code)
    testcases = [
        ("5\n", "25"),
        ("10\n", "100"),
        ("20\n", "400")
    ]

    outputs = code_runner.test_code(testcases)
    tobesent = []
    for i, output in enumerate(outputs):       
        # print(f"Testcase {i+1}:")
        # print(f"Expected output: {testcases[i][1]}")
        # print(f"Actual output: {output[0]}")
        # print()
        c = 0
        if int(testcases[i][1]) != int(output[0]):
            tobesent.append(["Some error with your code"])
            c=0
        else:
            c = 1
    if c ==1:
        tobesent.append(["You have passed all the test cases"])   
    outputs.append(tobesent[0])
    return outputs