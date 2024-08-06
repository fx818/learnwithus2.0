import script
res = ""
def runMainCode():
    with open('D:/Practice/Program Runner/correct/usercode.txt', 'r') as f:
        data = f.readlines()
        global res
        res = "\n".join(data)
runMainCode()
code = res
