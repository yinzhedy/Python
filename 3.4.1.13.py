# step 1
beatles =[]
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
new_members = []
for i in range(2):
    new_member = (input("Please enter the new member's name, enter anything else to stop"))
    if new_member == "Stu Sutcliffe" or "Pete Best":
        beatles.append(new_member)
        new_members.append(new_member)
    else:
        break
print("Step 3:", beatles)

# step 4
for i in new_members:
    if i in beatles:
        beatles.remove(i)
    else:
        continue
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
