import sys

from analyzer import get_code_smells
from generator import describe_code


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python main.py <path-to-file>")
        return 1

    target_path = sys.argv[1]
    try:
        with open(target_path, "r", encoding="utf-8") as handle:
            source_code = handle.read()
    except OSError as exc:
        print(f"Error reading file: {exc}")
        return 1

    summary = describe_code(source_code)
    smells = get_code_smells(source_code)

    print("NLP CODE ANALYSIS REPORT")
    print("=" * 25)
    print("Summary:")
    print(summary)
    print("\nCode Smells:")
    if smells:
        for smell in smells:
            print(f"- {smell}")
    else:
        print("- None")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
