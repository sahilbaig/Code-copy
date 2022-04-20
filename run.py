import ast
import ast
import code1
import code2

code1_contents=""
with open('code1.py') as f:
    code1_contents = f.read()

code2_contents=""
with open('code2.py') as f:
    code2_contents = f.read()


class toLower(ast.NodeTransformer):
    def visit_arg(self, node):
        return ast.arg(**{**node.__dict__, 'arg':str(0) })
    def visit_Name(self, node):
        return ast.Name(**{**node.__dict__, 'id':str(0)})
        # return ast.Name(**{**node.__dict__, 'id':node.id.lower()})

code1_final = ast.unparse(toLower().visit(ast.parse(code1_contents)))
code2_final = ast.unparse(toLower().visit(ast.parse(code2_contents)))
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


print("-------------")
if((program1 == program2) and  (code1_final==code2_final)):
    print("1.py and 2.py are same")
else:
    print("1.py and 2.py are not same")