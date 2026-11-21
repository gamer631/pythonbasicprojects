"""A simple multiple-choice quiz."""

QUESTIONS = [
    ("Which data type stores True or False?", ["str", "bool", "list", "float"], "b"),
    ("Which keyword defines a function?", ["func", "method", "def", "make"], "c"),
    ("What does len([2, 4, 6]) return?", ["2", "3", "6", "None"], "b"),
    ("Which structure stores key-value pairs?", ["tuple", "set", "dict", "string"], "c"),
]


def main() -> None:
    score = 0
    print("\nPython Basics Quiz\n")
    for number, (question, options, answer) in enumerate(QUESTIONS, start=1):
        print(f"{number}. {question}")
        for letter, option in zip("abcd", options):
            print(f"  {letter}) {option}")
        choice = input("Answer: ").strip().lower()
        if choice == answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Not quite—the answer is {answer}.\n")
    print(f"Result: {score}/{len(QUESTIONS)}")
    print("Nice work. Run it again to practice.")


if __name__ == "__main__":
    main()
