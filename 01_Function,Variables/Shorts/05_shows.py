SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possibe",
    "Jimmy Neutron",
    "The Proud Family"
]



def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    
    print(' , '.join(cleaned_shows))


main()