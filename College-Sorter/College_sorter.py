def get_entries():
    entries = []

    print("Enter college preferences. Type 'done' when finished.\n")

    while True:
        college = input("College Name (or 'done' to finish): ").strip()
        if college.lower() == 'done':
            break

        course = input("Course Name: ").strip()

        try:
            score = float(input("CUET Score: ").strip())
        except ValueError:
            print("Invalid score. Please enter a number.")
            continue

        entries.append((college, course, score))
        print("Entry added!\n")

    return entries

def sort_by_score(entries):
    return sorted(entries, key=lambda x: x[2])  # sort by CUET score (index 2)

def print_sorted_list(sorted_entries):
    print("\n--- Sorted Preference List (Lowest to Highest CUET Score) ---")
    for idx, (college, course, score) in enumerate(sorted_entries, start=1):
        print(f"{idx}. {college} - {course} | CUET Score: {score}")

# Main Program
if __name__ == "__main__":
    all_entries = get_entries()
    if not all_entries:
        print("No entries provided.")
    else:
        sorted_entries = sort_by_score(all_entries)
        print_sorted_list(sorted_entries)