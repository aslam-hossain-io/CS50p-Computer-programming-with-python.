def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "babu"]
    for name in range(len(names)):
        print(write_letter(names, "princess peach"))


    


def write_letter( receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to ball at
        Peach's Castle this evening, 7:00 PM.


        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()