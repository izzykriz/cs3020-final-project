import ast

from .python_ast import *

# ==================================================
# Pretty printer (concrete syntax)
# ==================================================


def print_program(p):
    def print_type(a):
        if a == bool:
            return "bool"
        elif a == int:
            return "int"
        elif isinstance(a, str):
            return a
        elif isinstance(a, tuple):
            return "(" + ", ".join([print_type(t) for t in a]) + ")"
        elif a is None:
            return "None"
        else:
            raise Exception("print_type", a)

    def print_stmt(s, indent=0):
        match s:
            case Call():
                return print_expr(s)
            case Print(e):
                return " " * indent + f"print({print_expr(e)})"
            case Return(e):
                return " " * indent + f"return {print_expr(e)}"
            case Assign(x, e):
                if not isinstance(x, str):
                    x = print_expr(x)
                return " " * indent + f"{x} = {print_expr(e)}"
            case If(e1, stmts1, stmts2):
                b1 = "\n".join([print_stmt(s, indent + 4) for s in stmts1])
                b2 = "\n".join([print_stmt(s, indent + 4) for s in stmts2])
                return "\n".join(
                    [
                        " " * indent + f"if {print_expr(e1)}:",
                        b1,
                        " " * indent + "else:",
                        b2,
                    ]
                )
            case While(e1, stmts):
                b = "\n".join([print_stmt(s, indent + 4) for s in stmts])
                return "\n".join([" " * indent + f"while {print_expr(e1)}:", b])
            case For(x, e1, stmts):
                b = "\n".join([print_stmt(s, indent + 4) for s in stmts])
                return "\n".join([" " * indent + f"for {x} in {print_expr(e1)}:", b])
            case FunctionDef(name, params, body, return_type):
                b = "\n".join([print_stmt(s, indent + 4) for s in body])
                params_s = ", ".join([f"{x}: {print_type(t)}" for x, t in params])
                decl = f"def {name}({params_s}) -> {print_type(return_type)}:"
                return decl + "\n" + b
            case ClassDef(name, superclass, body):
                decl = f"class {name}({superclass}):\n"
                indent += 4
                fields = ""
                for field in body:
                    fields += " " * indent
                    if type(field) is tuple:
                        fields += field[0] + ": " + print_type(field[1])
                    else:
                        fields += print_stmt(field, indent)
                    fields += "\n"
                # fields = '\n'.join([f'    {x}: {print_type(t)}' for x, t in body])
                return decl + fields
            case _:
                raise Exception("print_stmt", s)

    def print_expr(e):
        match e:
            case ast.Name(s):
                return s
            case ast.Attribute(name):
                return print_expr(name)
            case Prim(op, args):
                args_str = ", ".join([print_expr(a) for a in args])
                return f"{op}({args_str})"
            case Constant(c):
                return str(c)
            case Var(x):
                return str(x)
            case Begin(stmts, exp):
                stmts_str = "; ".join([print_stmt(s) for s in stmts])
                return f"begin({stmts_str}; {print_expr(exp)})"
            case Call(e1, args):
                args_str = ", ".join([print_expr(a) for a in args])
                return f"{print_expr(e1)}({args_str})"
            case FieldRef(e1, f):
                return f"{print_expr(e1)}.{f}"
            case _:
                raise Exception("print_expr", e)

    match p:
        case Program(stmts):
            return "\n".join([print_stmt(s) for s in stmts])
        case _:
            raise Exception("print_program", p)
