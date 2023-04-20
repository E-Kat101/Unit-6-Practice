def main():
    print("1. Butterfly")
    print("2. Elephant")
    print("3. Teddy Bear")
    print("4. Snake")

    choice = int(input("\nWhich animal to draw? "))
    print()

	
# Change the code in the if statement for choice 1 so that it calls the ‘butterfly’ function twice instead of just once. What happens now when you run the program and choose option 1? 
    if choice == 1:
        for i in range(2):
            butterfly()
# Now when I run the program and choose option 1, two drawings of the butterfly show up instead of one, followed by one "Goodbye!" message printed after the second butterfly.
    
    elif choice == 2:
        elephant()
		
# Add the two missing function calls for menu options 3 and 4.
    elif choice == 3:
        teddybear()
    elif choice == 4:
        snake()
    else:
        print("Sorry, that wasn't one of the choices.")

    print("\nGoodbye!")
	
	
def butterfly():
    print("  .==-.                   .-==.     ")
    print("   \\()8`-._  `.   .'  _.-'8()/     ")
    print("   (88\"   ::.  \\./  .::   \"88)     ")
    print("    \\_.'`-::::.(#).::::-'`._/      ")
    print("      `._... .q(_)p. ..._.'         ")
    print("        \"\"-..-'|=|`-..-\"\"       ")
    print("        .\"\"' .'|=|`. `\"\".       ")
    print("      ,':8(o)./|=|\\.(o)8:`.        ")
    print("     (O :8 ::/ \\_/ \\:: 8: O)      ")
    print("      \\O `::/       \\::' O/       ")
    print("       \"\"--'         `--\"\"   hjw")
	
	
def elephant():
    print("       _..--\"\"-.                  .-\"\"--.._ ")
    print("   _.-'         \\ __...----...__ /         '-._")
    print(" .'      .:::...,'              ',...:::.      '.")
    print("(     .'``'''::;                  ;::'''``'.     )")
    print(" \\             '-)              (-'             /")
    print("  \\             /                \\             /")
    print("   \\          .'.-.            .-.'.          /")
    print("    \\         | \\0|            |0/ |         /")
    print("    |          \\  |   .-==-.   |  /          |")
    print("     \\          `/`;          ;`\\`          /")
    print("      '.._      (_ |  .-==-.  | _)      _..'")
    print("          `\"`\"-`/ `/'        '\\` \\`-\"`\"`")
    print("               / /`;   .==.   ;`\\ \\")
    print("         .---./_/   \\  .==.  /   \\ \\")
    print("        / '.    `-.__)       |    `\"")
    print("       | =(`-.        '==.   ;")
    print(" jgs    \\  '. `-.           /")
    print("         \\_:_)   `\"--.....-'")

	
def teddybear():
    print("            ___   .--. ")
    print("      .--.-\"   \"-' .- |")
    print("     / .-,`          .'")
    print("     \\   `           \\")
    print("      '.            ! \\")
    print("        |     !  .--.  |")
    print("        \\        '--'  /.____")
    print("       /`-.     \\__,'.'      `\\")
    print("    __/   \\`-.____.-' `\\      /")
    print("    | `---`'-'._/-`     \\----'    _")
    print("    |,-'`  /             |    _.-' `\\")
    print("   .'     /              |--'`     / |")
    print("  /      /\\              `         | |")
    print("  |   .\\/  \\      .--. __          \\ |")
    print("   '-'      '._       /  `\\         /")
    print("      jgs      `\\    '     |------'`")
    print("                 \\  |      |")
    print("                  \\        /")
    print("                   '._  _.'")
    print("                      ``")

	
def snake():
    print("         ,,'6''-,.")
    print("        <====,.;;--.")
    print("        _`---===. \"\"\"==__")
    print("      //\"\"@@-\\===\\@@@@ \"\"\\\\")
    print("     |( @@@  |===|  @@@  ||")
    print("      \\\\ @@   |===|  @@  //")
    print("        \\\\ @@ |===|@@@ //")
    print("         \\\\  |===|  //")
    print("___________\\\\|===| //_____,----\"\"\"\"\"\"\"\"\"\"-----,_")
    print("  \"\"\"\"---,__`\\===`/ _________,---------,____    `,")
    print("             |==||                           `\\   \\")
    print("            |==| |          pb                 )   |")
    print("           |==| |       _____         ______,--'   '")
    print("           |=|  `----\"\"\"     `\"\"\"\"\"\"\"\"         _,-'")
    print("            `=\\     __,---\"\"\"-------------\"\"\"''")
    print("                \"\"\"\"		")


if __name__ == "__main__":
    main()
