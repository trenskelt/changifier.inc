fortnite = {
    "BigPot": 50,
    "Minis": 25,
    "ChugBlug": 200,
}


print(fortnite)
print(fortnite["BigPot"])
print(fortnite["Minis"])
print(fortnite["ChugBlug"])

print(f"Health or shield for BigPot: {fortnite['BigPot']}")
print(f"Health or shield for Minis: {fortnite['Minis']}")
print(f"Health or shield for ChugBlug: {fortnite['ChugBlug']}")



Shield = fortnite.get("BigPot")
print(f"Shield for BigPot: {Shield}")


fortnite["BigPot"] = 45 
print(f"Reworked BigPot: {fortnite['BigPot']}")

fortnite["Minis"] = 30
print(f"Reworked Minis: {fortnite['Minis']}")

fortnite["ChugBlug"] = 250
print(f"Reworked ChugBlug: {fortnite['ChugBlug']}")