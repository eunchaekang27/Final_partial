user_input = str(input())
alexa = user_input.split()
num_alexa = alexa.count("Alexa")

while num_alexa > 1:
  print("Hey, just say my name once.")
  break

while num_alexa == 1:
  print("Tell me, how can I help you?")
  break
