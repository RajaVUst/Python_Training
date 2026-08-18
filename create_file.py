from pathlib import Path

folder = Path("Day6")

folder.mkdir(exist_ok=True)

for number in range(1, 31):
    file_path = folder / f"exercise{number}.py"

    file_path.write_text(
        f"# Day 6 - Exercise {number}\n\n",
        encoding="utf-8"
    )

    print(f"Created: {file_path}")