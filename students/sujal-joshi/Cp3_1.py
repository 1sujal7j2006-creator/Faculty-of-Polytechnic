def collect_all_subjects():
    subjects = []

    while True:
        subject = collect_one_subject()
        subjects.append(subject)

        if not ask_yes_no("Add another subject? (y/n): "):
            break

    return subjects
