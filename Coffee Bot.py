# Define functions
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the \ncorresponding letter for your response.")

def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  print(size)

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n')

# Call coffee_bot()!
coffee_bot()
