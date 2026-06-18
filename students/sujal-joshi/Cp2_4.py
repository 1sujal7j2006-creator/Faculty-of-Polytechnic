def collect_one_subject():
    name = ask_text("Subject name:")
    m1 = ask_mark("Mark 1 (0-100):")
    m2 = ask_mark("Mark 2 (0-100):")
    m3 = ask_mark("Mark 3 (0-100):")

    return (name, m1, m2, m3)
