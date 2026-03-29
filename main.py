from utils.pdf_handler import extract_questions
from utils.ml_model import predict
from utils.storage import save, load

questions_data = []
total_time = 0


def analyze():
    global questions_data, total_time

    print("\nUpload and Analyze PDF\n")

    path = input("Enter PDF path: ").strip().strip('"')
    subject = input("Enter subject: ").strip()

    questions = extract_questions(path)

    if not questions:
        print("No questions extracted. Please check the PDF.")
        return

    print(f"\n{len(questions)} questions extracted.\n")

    questions_data = []

    for i, q in enumerate(questions, 1):
        print("\n--------------------------------")
        print(f"Q{i}: {q[:100]}")
        print("--------------------------------")

        try:
            marks = int(input("Enter marks (2/5/10): "))
            freq = int(input("Enter frequency (1-3): "))
        except:
            print("Invalid input. Skipping question.")
            continue

        label, time = predict(marks, freq)

        questions_data.append({
            "question": q,
            "label": label,
            "time": time,
            "marks": marks,
            "frequency": freq
        })

    total_time = sum(q["time"] for q in questions_data)

    save(subject, {
        "questions": questions_data,
        "total_time": total_time
    })

    print("\nAnalysis complete and saved.")


def load_data():
    global questions_data, total_time

    print("\nLoad Previous Data\n")

    subject = input("Enter subject to load: ")
    data = load(subject)

    if data:
        questions_data = data["questions"]

        # Update time using latest logic
        for q in questions_data:
            marks = q.get("marks", 2)
            freq = q.get("frequency", 1)

            _, new_time = predict(marks, freq)
            q["time"] = new_time

        total_time = sum(q["time"] for q in questions_data)

        print("Data loaded and updated successfully.")
    else:
        print("No saved data found.")


def show_questions():
    if not questions_data:
        print("\nNo data available.")
        return

    print("\nImportant Questions:\n")

    for i, q in enumerate(questions_data, 1):
        print(f"{i}. {q['question'][:80]}")
        print(f"   Priority: {q['label']}")
        print(f"   Time: {q['time']} minutes")
        print(f"   Marks: {q['marks']} | Frequency: {q['frequency']}\n")


def show_time():
    if total_time == 0:
        print("\nNo data available.")
        return

    print(f"\nTotal Study Time Required: {total_time} minutes")


def menu():
    print("\n" + "=" * 40)
    print("        PYQ Analyzer")
    print("=" * 40)
    print("1. Upload and Analyze PDF")
    print("2. Load Previous Data")
    print("3. Show Questions")
    print("4. Show Total Time")
    print("5. Exit")


# Main loop
while True:
    menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        analyze()
    elif choice == "2":
        load_data()
    elif choice == "3":
        show_questions()
    elif choice == "4":
        show_time()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")