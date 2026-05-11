#pip install helper_functions
from helper_functions import print_llm_response

adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun (person, place, thing): ")
adj2 = input("Enter another adjective: ")
verb1 = input("Enter a verb ending in 'ing': ")
adj3 = input("Enter a descriptive adjcetive: ")

prompt = f"create a madlib game using [{adj1}, {noun1}, {adj2}, {verb1}, {adj3}]"

print_llm_response(prompt)

'''
pip install opencv-python
sudo apt-get update
sudo apt-get install -y libgl1
'''