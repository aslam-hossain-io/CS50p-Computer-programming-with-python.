def main():
    spacecraft1 = {"name": "voyager 1", "distance": 163}
    spacecraft2 = {"name": "James Webb Space Telescope", "distance": 0.01}
    spacecraft2.update({"orbit": "Sun"})
    print(create_report_1(spacecraft1))
    print(create_report_2(spacecraft2))


def create_report_1(spacecraft1):
    return f"""
    ========== Report ========

    Name: {spacecraft1["name"]}
    Distance: {spacecraft1["distance"]} AU

    ==========================
    """

def create_report_2(spacecraft2):
    return f"""
    ========== Report ========

    Name: {spacecraft2.get("name", "Unknown")}
    Distance: {spacecraft2.get("distance", "Unknown")} AU
    Orbit: {spacecraft2.get("orbit", "Unknown")}

    ==========================
    """

main()