from pathlib import Path
import random

from .dataset_templates import (
    AI_EXAMPLES,
    CORRECTION_EXAMPLES,
    DEBUGGING_EXAMPLES,
    EXPLANATION_EXAMPLES,
    MATH_EXAMPLES,
    PROGRAMMING_EXAMPLES,
    PYTHON_EXAMPLES,
    REASONING_EXAMPLES,
)


OUTPUT_DIR = Path("data/raw")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


DATASETS = {

    "ai": AI_EXAMPLES,

    "python": PYTHON_EXAMPLES,

    "programming": PROGRAMMING_EXAMPLES,

    "mathematics": MATH_EXAMPLES,

    "reasoning": REASONING_EXAMPLES,

    "debugging": DEBUGGING_EXAMPLES,

    "corrections": CORRECTION_EXAMPLES,

    "explanations": EXPLANATION_EXAMPLES,

}


# ============================================================
# Write individual datasets
# ============================================================

for name, examples in DATASETS.items():

    path = (
        OUTPUT_DIR
        /
        f"{name}.txt"
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        for item in examples:

            file.write(
                item
            )

            file.write(
                "\n"
            )

    print(
        f"Created {path}"
    )


# ============================================================
# Combine
# ============================================================

combined = []

for examples in DATASETS.values():

    combined.extend(
        examples
    )


random.seed(1337)

random.shuffle(
    combined
)


training_file = (
    OUTPUT_DIR / "train.txt"
)


with open(
    training_file,
    "w",
    encoding="utf-8"
) as file:

    for item in combined:

        file.write(
            item
        )

        file.write(
            "\n"
        )


print()

print(
    f"Created {training_file}"
)

print(
    f"Total examples: {len(combined)}"
)

print(
    f"Total characters: "
    f"{len(training_file.read_text(encoding='utf-8')):,}"
)

print()

print(
    "Dataset generation complete."
)