#!/usr/bin/env python3

def main():

    char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk)\n")
    char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)\n")

    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

    char_stat_result = marvelchars[char_name][char_stat]

    if char_stat == "real name":
        char_stat_result = char_stat_result.title()

    print(f"{char_name}'s {char_stat} is: {char_stat_result}")

if __name__ == "__main__":
    main()
