c = "true"
num_clients = 0
b_customers = 0
n_b_customers = 0
e_w = 0
h_w = 0
w_w = 0
ho_w = 0
wands = ["Elder Wand [1]","Hawthorn Wand [2]","Willow Wand [3]","Holly Wand [4]"]
while c == "true":
  client = str(input("Does a client come in? (yes/no):")) 
  if client == "yes":
    num_clients += 1
    buys = str(input("Do they buy something? (yes/no):"))
    if buys == "yes":
      b_customers += 1
      print(wands)
      wand = int(input("What wand did they buy? (1,2,3 or 4):"))
      if wand == 1:
        e_w += 1
      elif wand == 2:
        h_w += 1
      elif wand == 3:
        w_w += 1
      elif wand == 4:
        ho_w += 1
    elif buys == "no":
      n_b_customers += 1

  if client == "no":
    print(f"Total clients: {num_clients}")
    print(f"Customers who bought: {b_customers}")
    print(f"Customers who didn't buy: {n_b_customers}")
    print(f"Today {e_w} Elder Wand(s), {h_w} Hawthorn Wand(s), {w_w} Willow Wand(s) and {ho_w} Holly Wand(s) were sold.")
    if b_customers == 0 and num_clients == 0:
      print("What a bad day for Ollivanders.")
    else: 
      print("What a great day for Ollivanders!")
    break
