import random

def sample():
    return random.randint(0, 100)

def main():
    moisture = sample()
    days = 1
    print(f"Day {days}: Moisture is {moisture}%")
    while moisture > 20:
        moisture = sample()
        days +=1
        print(f"Day {days}: Moisture is {moisture}%")

    print("Time to water!")

main()
