a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a) # use 3 "" to print multiple lines
print(len(a)) # length of the string


txt = "The best things in life are free!"
if "fr" in txt:   # searching in a string in a string
  print("Yes, 'fr' is present.")

print("expensive" not in txt) # returns a boolean value

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")