from utility import CodeRunner
from mainCode import code

def returnOutput():
    code_runner = CodeRunner()
    code_runner.set_code(code)
    testcases = [
        ("5\n", "25"),
        ("10\n", "100"),
        ("20\n", "400")
        # (input, output)
    ]

    outputs = code_runner.test_code(testcases)

    for i, output in enumerate(outputs):       
        print(f"Testcase {i+1}:")
        print(f"Expected output: {testcases[i][1]}")
        print(f"Actual output: {output[0]}")
        print()
    
    return output

returnOutput()