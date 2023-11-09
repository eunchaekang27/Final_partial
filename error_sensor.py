counter = 0
t_readings = int(input("How many temperature readings do you have?:"))
wrong = 0

while counter < t_readings:
  counter += 1
  temperature = float(input("Insert temperature:"))
  if temperature not in range(10,41):
    wrong += 1

e_rate = (wrong/t_readings)*100
print(f"The sensor went wrong {wrong} times.")
print(f"The sensor error rate is {e_rate}")
