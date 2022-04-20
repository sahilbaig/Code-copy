import ast

function_count=0
program1={}
program2={}
def show_info(functionNode):
    global function_count
    program1[function_count]=len(functionNode.args.args)
    function_count=function_count+1
    print("Function name:", functionNode.name)
    print("Args:")
    for arg in functionNode.args.args:
        #import pdb; pdb.set_trace()
        print("\tParameter name:", arg.arg)


filename = "1.py"
with open(filename) as file:
    node = ast.parse(file.read())

functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

for function in functions:
    show_info(function)

for class_ in classes:
    print("Class name:", class_.name)
    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
    for method in methods:
        show_info(method)


print("------------------------")


function_count_2=0
def show_info(functionNode):
    global function_count_2
    function_coun_2=function_count+1
    program2[function_count_2]=len(functionNode.args.args)
    print("Function name:", functionNode.name)
    print("Args:")
    for arg in functionNode.args.args:
        #import pdb; pdb.set_trace()
        print("\tParameter name:", arg.arg)



filename = "2.py"
with open(filename) as file:
    node = ast.parse(file.read())

functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
classes = [n for n in node.body if isinstance(n, ast.ClassDef)]

for function in functions:
    show_info(function)

for class_ in classes:
    print("Class name:", class_.name)
    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
    for method in methods:
        show_info(method)


print(program1 == program2)