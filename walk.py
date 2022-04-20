import ast

source="""
def myFunc(Variable):
   Tmp = Sin(Variable)
   return Tmp * 2
"""
root = ast.parse(source)
names = sorted({node.id for node in ast.walk(root) if isinstance(node, ast.Name)})
print(names)