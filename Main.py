from LinkedListMaze import Path 


def main():
    allowed_items = {"Travelers Map", "Chosen 1 Sword", "Elite armor", "Supernatural Potions",}
    path = Path(allowed_items)
    
    path.append("Town", dialogue="Welcome Traveler!", npc = "Townsperson", required_items={"Travelers Map"})
    path.append("Forest", dialogue="The forest calls... You have a duty to fulfill", npc = "Forest Guardian", required_items={"Chosen 1 Sword"})
    path.append("Cave", dialogue="There is something ominous about this cave...but the treasure is sacred obtain it and you will do what needs to be done", npc = "Caveman", required_items={"Elite Armor"})
    path.append("Mountain", dialogue="The skyscraper mountain seems to be hiding something.. luckily I am not take this hero.", npc = "Mountain Wizard", required_items={"Supernatural Potion"})
    path.append("Lake", dialogue="The Final Destination.. Defeat the lake Spirit to win the game! \n My reign shall not end here to the likes of you!", npc = "Lake Spirit")

    # Start player at the town
    print("You wake up in the town square...")
    path.print_current_location()
    print("")

    # Display welcome message

    path.display_path()

    # Display options interface
    while True:
        print("\nOptions:")
        print("1. Move forward")
        print("2. Move backward")
        print("3. Talk to NPC")
        print("4. Show inventory")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path.move_forward()
        elif choice == "2":
            path.move_backward()
        elif choice == "3":
            path.talk_to_npc()
        elif choice == "4":
            path.show_inventory()
        elif choice == "5":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
        
        if not path.current_location.next:
            print("Congratulations! You have reached the end of the path.")
            print("You win the game!")
            break
        
        print("")
        
if __name__ == "__main__":
    main()
