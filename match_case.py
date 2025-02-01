day= int(input("enter the day "))

def day_of_week(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is monday"
        case 3:
            return "It is tuesday"
        case 4:
            return "It is wednesday"
        case 5:
            return "It is thursday"
        case 6:
            return "It is friday"
        case 7:
            return "It is saturday"
        case _:
            return "Invalid day"

print(day_of_week(day))

def ISweek_end(day):
    match day:
        case "Saturady" | "Sunday":
            return True
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return False

print(ISweek_end("Saturady"))
