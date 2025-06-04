print("Welcome to SRM Info Bot!")
query = input("Ask me something: ").lower()

if "course" in query:
    print("SRM offers B.Tech in AI, CSE, ECE, and more.")
elif "club" in query:
    print("SRM has coding, robotics, dance and drama clubs.")
elif "fees" in query:
    print("Fees depend on the branch. Please visit the official website.")
else:
    print("Sorry, I don't have information on that.")
