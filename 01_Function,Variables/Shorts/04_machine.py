emoticon = "v.v"


def main():
    global emoticon
    say("IS anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)

main()