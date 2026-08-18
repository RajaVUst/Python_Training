import csv
 
def load_scores(path):
    scores = {}
 
    try:
        with open(path, "r") as f:
            reader = csv.DictReader(f)
 
            for row in reader:
                try:
                    scores[row["Name"]] = int(row["Score"])
                except ValueError:
                    print(f"Skipping bad score for {row['Name']}")
 
    except FileNotFoundError:
        print("File not found.")
        return {}
 
    return scores
 
 
scores = load_scores(r"Day_6\Ref doc\scores.csv")
print(scores)
 
# Output:
# {'Alice': 85, 'Bob': 90, 'Charlie': 78}
 