import os
import pandas as pd

OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def export_txt(text):

    file_path = os.path.join(OUTPUT_FOLDER, "notes.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    return file_path


def export_csv(tasks):

    file_path = os.path.join(OUTPUT_FOLDER, "tasks.csv")

    df = pd.DataFrame({
        "Task": tasks,
        "Status": ["Pending"] * len(tasks)
    })

    df.to_csv(file_path, index=False)

    return file_path