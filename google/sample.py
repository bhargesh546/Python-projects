import time
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
        time.sleep(1)
    print("Done")

attempts(5)

"""
1. 
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        new_filenames.append(filename.replace(filename[-4:], ".h"))
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

2.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

new_filenames = [filename.replace(filename[-4:], ".h") if filename.endswith(".hpp") else filename for filename in filenames ]


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

3.
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say += word[1:] + word[0] + "ay "
    # Turn the list back into a phrase
  return say.strip()
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

4.

"""

"""
1.
def email_list(domains):
	emails = []
	for domain_name, users in domains.items():
	  for user in users:
	    emails.append(user + "@" + domain_name)
	return(emails)

2.
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group_name, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			if user in user_groups:
				user_groups[user].append(group_name)
			else:
				user_groups[user] = [group_name]
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

5.
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item in basket:
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += basket[item]
	# Limit the return value to 2 decimal places
	return round(total, 2)  

"""