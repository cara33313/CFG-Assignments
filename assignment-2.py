import pokebase as pb

# Function which gets the user to input a number for which generation of pokemons they want to receive, then checks if it is between 1-9
def pokemon_gen_choice():
    pokemon_input = int(input("Choose a generation of pokemon from 1-9: "))
    if 1 <= pokemon_input <= 9:
        return pokemon_input
    else:
        print("This is not a number between 1 and 9, please try again!")
        return "x"

# Function which takes the first letter, and returns all the pokemons from that generation with that first letter
# If a character which is not a letter, or more than one character typed in, returns a value which prompts the user to try again
def pokemon_first_letter(user_choice, pokemon_list):
    first_letter_choice = input(f"Here is a list of all the pokemons from generation {user_choice}, pick a first letter: ")
    pokemon_first_letter_list = []

    if first_letter_choice.isalpha() and len(first_letter_choice) == 1:
        for i in pokemon_list:
            if i[0] == first_letter_choice.upper():
                pokemon_first_letter_list.append(i)
            else: ''
        return pokemon_first_letter_list

    else:
        print("This is not a single letter, please try again!")
        return "x"

# Prints the list of all the pokemons in the generation with that first letter, and asks the user to guess which one has the highest power score, if they type in a pokemon in the list it returns that name, if the pokemon
# is not in the list of the correct generation and first letter, returns x
def power_score(pokemon_first_letter_list_full):
    highest_score_choice = input(f"\nHere is the list of pokemons with that first letter: \n"
      f"{', '.join(pokemon_first_letter_list_full)}\n"
      f"Choose the pokemon you think has the highest power score! (this might take a few seconds): ").title()

    if highest_score_choice in pokemon_first_letter_list_full:
       return highest_score_choice
    else:
        while highest_score_choice not in pokemon_first_letter_list_full:
            print("This pokemon is not in the list :( PLease try again")
            return "x"

# Retrieving the number the user typed in
user_choice = pokemon_gen_choice()

# Checking if the function returned that a number between 1-9 was not typed in, getting the user to try again
while user_choice == "x":
    user_choice = pokemon_gen_choice()

# Retrieving the pokemons from the generation the user typed in
GENERATION = user_choice
gen_resource = pb.generation(GENERATION)

# Creating a list of the names of the pokemons in that generation
pokemon_list = []
for pokemon in gen_resource.pokemon_species:
    pokemon_list.append(pokemon.name.title())
    print(pokemon.name.title())

# Calling function to create a list of all pokemons in the generation beginning with that first letter
pokemon_first_letter_list_full = pokemon_first_letter(user_choice, pokemon_list)

# If a single letter not typed in, calls the function for the user to try again (done as a while loop so this can be repeated until the user types in a letter correctly)
while pokemon_first_letter_list_full == "x":
    pokemon_first_letter_list_full = pokemon_first_letter(user_choice, pokemon_list)

# If the letter the user typed in returns an empty list (if there are no pokemons in that generation with that first letter), recalls the function for the user to try again
while not pokemon_first_letter_list_full:
    print("There are no pokemons in the generation with that first letter, please try again!")
    pokemon_first_letter_list_full = pokemon_first_letter(user_choice, pokemon_list)

# Calls function which gets the user to unput a pokemon from the list to get the power score
score_choice = power_score(pokemon_first_letter_list_full)

# If the function return x which means the user typed in a pokemon not in the generation and first name list, prompts the user to try again (in a while loop so will keep repeating until the user types in a pokemon
# in the list
while score_choice == "x":
    score_choice = power_score(pokemon_first_letter_list_full)

# Prints out the power score for the pokemon the user typed in
print(f"The power score for{score_choice} is {pb.pokemon(score_choice.lower()).base_experience}!")