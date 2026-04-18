import ast
from typing import List


class _CodeSmellVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.smells: List[str] = []
        self._nesting_depth = 0

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, ast.Store) and len(node.id) == 1 and node.id not in {"i", "j", "k"}:
            self.smells.append(f"Ambiguous Variable Name: '{node.id}'")
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._check_function_length(node)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._check_function_length(node)
        self.generic_visit(node)

    def _check_function_length(self, node: ast.AST) -> None:
        start = getattr(node, "lineno", None)
        end = getattr(node, "end_lineno", None)
        if start is not None and end is not None:
            length = end - start + 1
            if length > 15:
                self.smells.append(f"Long Method: '{getattr(node, 'name', '<lambda>')}' ({length} lines)")

    def visit_If(self, node: ast.If) -> None:
        self._check_nesting(node)

    def visit_For(self, node: ast.For) -> None:
        self._check_nesting(node)

    def visit_While(self, node: ast.While) -> None:
        self._check_nesting(node)

    def _check_nesting(self, node: ast.AST) -> None:
        self._nesting_depth += 1
        if self._nesting_depth > 2:
            self.smells.append("Deep Nesting: block nested more than 2 levels")
        self.generic_visit(node)
        self._nesting_depth -= 1


def get_code_smells(source_code: str) -> List[str]:
    tree = ast.parse(source_code)
    visitor = _CodeSmellVisitor()
    visitor.visit(tree)
    return visitor.smells
