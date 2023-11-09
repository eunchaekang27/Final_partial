gryffindor_score = 0
slytherin_score = 0
counter = 0

num_match = int(input("Enter the number of events in the Quidditch match:"))

while counter < num_match:
  counter += 1
  event = str(input("Enter an event (goal/snitch/foul):"))
  team = str(input("Which team scored (Gryffindor or Slytherin):"))
  if event == "goal" and team == "Gryffindor":
      gryffindor_score += 10
  elif event == "goal" and team == "Slytherin":
    slytherin_score += 10
  elif event == "snitch" and team == "Gryffindor":
    gryffindor_score += 150
  elif event == "snitch" and team == "Slytherin":
    slytherin_score += 150
  elif event == "foul" and team == "Gryffindor":
    gryffindor_score -= 30
  elif event == "foul" and team == "Slytherin":
    slytherin_score -= 30

print(f"Gryffindor: {gryffindor_score} points")
print(f"Slytherin: {slytherin_score} points")
if gryffindor_score < slytherin_score:
  print("Slytherin wins!")
elif gryffindor_score > slytherin_score:
  print("Gryffindor wins!")
