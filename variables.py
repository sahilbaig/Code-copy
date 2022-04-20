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
print(code1_final==code2_final)