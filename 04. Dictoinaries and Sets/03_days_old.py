from datetime import date

PEOPLE = {
    "Mahdi": date.fromisoformat("1998-06-03"),
    "Reuven": date.fromisoformat("1970-07-14"),
    "Atara": date.fromisoformat("2000-12-16"),
    "Shikma": date.fromisoformat("2002-12-17"),
    "Amotz": date.fromisoformat("2005-10-31"),
}


def calculate_days():
    while True:
        name = input("Enter a person's name: ").strip()

        if not name:
            break

        today = date.today()

        if name in PEOPLE:
            print(f"{name} is {(today - PEOPLE[name]).days} days")
        else:
            print(f"{name} is not in the system.")


calculate_days()
