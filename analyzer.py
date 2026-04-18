import ast
from typing import List


class _CodeSmellVisitor(ast.NodeVisitor):
	def __init__(self) -> None:
		self.smells: List[str] = []

	def visit_Name(self, node: ast.Name) -> None:
		if isinstance(node.ctx, ast.Store) and len(node.id) == 1:
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
				name = getattr(node, "name", "<lambda>")
				self.smells.append(f"Long Method: '{name}' ({length} lines)")


def get_code_smells(source_code: str) -> List[str]:
	tree = ast.parse(source_code)
	visitor = _CodeSmellVisitor()
	visitor.visit(tree)
	return visitor.smells


__all__ = ["get_code_smells"]
