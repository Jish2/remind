import json
from datetime import datetime
import subprocess


def main():
    # get reminders
    process = subprocess.Popen(
        "reminders show Reminders -f json".split(" "),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()

    reminders = stdout.decode("utf-8")
    reminders = json.loads(reminders)

    # reminders to show
    upcoming_reminders = []

    for reminder in reminders:
        if "dueDate" in reminder:
            date = datetime.strptime(reminder["dueDate"], "%Y-%m-%dT%H:%M:%SZ")
            today = datetime.now()

            if today.date() == date.date():
                upcoming_reminders.append(reminder)

        elif reminder["priority"] == 0:
            upcoming_reminders.append(reminder)

    # sort so reminders with due date come first
    upcoming_reminders.sort(
        key=lambda x: x["dueDate"] if "dueDate" in x else "", reverse=True
    )

    for reminder in upcoming_reminders:
        print("○ ", end="")

        print(reminder["title"], end="")

        if "dueDate" in reminder:
            # print to the format 7:00 AM
            date = datetime.strptime(reminder["dueDate"], "%Y-%m-%dT%H:%M:%SZ")
            formatted_date = date.strftime("%-I:%M %p")

            print(f" - {formatted_date}", end="")

        print()


if __name__ == "__main__":
    main()
