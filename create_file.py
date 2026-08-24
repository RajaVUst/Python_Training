from pathlib import Path

folder = Path("Day10")

folder.mkdir(exist_ok=True)

for number in range(1, 7):
    file_path = folder / f"Task{number}.py"

    file_path.write_text(
        f"# Day 10 - Task {number}\n\n",
        encoding="utf-8"
    )

    print(f"Created: {file_path}")