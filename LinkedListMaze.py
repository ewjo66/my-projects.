from Node import Node 

class Path:
  def __init__(self,allowed_items = NotImplemented):
      self.head = None
      self.current_location = None
      self.inventory = set()
      self.allowed_items = allowed_items if allowed_items else set()

  def append(self, data, dialogue = None, item = None, obstacle = False, npc = None, required_items = None ):
      new_node = Node(data, item, obstacle, npc)
      new_node.dialogue = dialogue
      new_node.required_items = required_items
      if not self.head:
          self.head = new_node
          self.current_location = new_node
      else:
          current = self.head
          while current.next:
              current = current.next
          current.next = new_node

  def move_forward(self):
         if self.current_location and self.current_location.next:
            next_location = self.current_location.next

            if self.current_location.required_items:
                current_required_item = next(iter(self.current_location.required_items))
                if current_required_item not in self.inventory:
                    print(f"You cannot proceed without the required items: {current_required_item}")
                    return
                else:
                    self.current_location.required_items.remove(current_required_item)

            
            if next_location.npc == "Lake Spirit":
                required_previous_items = {"Travelers Map", "Chosen 1 Sword", "Elite Armor", "Supernatural Potion"}
                if not required_previous_items.issubset(self.inventory):
                    print("You cannot proceed to the Lake Spirit without collecting all required items from previous paths.")
                    return
                
                if "Sacred Amulet" not in self.inventory:
                    print("You need to acquire the Sacred Amulet before facing the Lake Spirit.")
                    return
            
            
            self.current_location = next_location
            print("You have arrived at", self.current_location.data)
            if self.current_location.dialogue:
               print("Path Message:", self.current_location.dialogue)
            self.display_path()

            if self.current_location.item:
                self.insert_item(self.current_location.item)

            if self.current_location.npc == "Lake Spirit":
                self.puzzle_battle()                
                    
         else:
             print("Nowhere to go forward!")

     


  def move_backward(self):
     if self.current_location and self.current_location != self.head:
        prev = self.head
        while prev.next != self.current_location:
           prev = prev.next
        self.current_location = prev
        print("Moved backward to", self.current_location.data)
        self.display_path()

        if self.current_location.npc == "Forest Guardian" and "Sacrede Amulet" not in self.inventory:
            print("You must obtain the Sacred Amulet from the Forest Guardian before proceeding to the Lake Spirit.")
        
     else:
        print("Nowhere to go backward!")


  def display_path(self):
      print("Path:")
      current = self.head
      while current:
         if current == self.current_location:
            if current.npc:
               print(f"[{current.data} - NPC: {current.npc}]", end=" -> ")
            else:
              print(f"[{current.data}]", end=" -> ")
         else:
            if current.npc:
               print(f"{current.data} - NPC: {current.npc}", end=" -> ")
            else:
               print(current.data, end=" -> ")
         current = current.next
      print("End")
               
  def insert_item(self, item):
         self.append(item)
         self.inventory.add(item)  # Item insertion
         print("Added", item, "to inventory.")


  def print_current_location(self):
      if self.head:
          print("Current location:", self.head.data)
      else:
          print("No current location.")


  
  def show_inventory(self):   #show inventory
    print("\nInventory:")
    if self.inventory:
       for item in self.inventory:
          print("-", item)
    else:
       print("Inventory is empty.")

  def talk_to_npc(self):
    if self.current_location and self.current_location.npc:
        npc = self.current_location.npc
        npc_dialogue = self.current_location.dialogue
        offered_item = None

      
        if self.current_location.npc == "Townsperson":
            npc_dialogue = "Welcome, traveler! I have something that may aid you on your journey. Would you like to accept the Map?"
            offered_item = "Travelers Map"
        elif self.current_location.npc == "Forest Guardian":
            required_previous_items = {"Travelers Map", "Chosen 1 Sword", "Elite Armor", "Supernatural Potion"}
            if required_previous_items.issubset(self.inventory):
                npc_dialogue = "Ah you've collected all the items needed to face the Lake Spirit. However, to defeat it, you will also need the Sacred Amulet."
                offered_item = "Sacred Amulet"
            else:
                npc_dialogue = "Greetings, seeker of the forest. I offer you the Sword of the Ancient Trees. Will you accept it?"
                offered_item = "Chosen 1 Sword"
        elif self.current_location.npc == "Caveman":
           npc_dialogue = "This armor is sacred,but I see you hold the Chosen ones sword......take these for you will need them. Will you accept?"
           offered_item = "Elite Armor"
        elif self.current_location.npc == "Mountain Wizard":
           npc_dialogue = "Your destiny has almost been fulfilled....take these for without it you stand no chance."
           offered_item = "Supernatural Potion"
        
        print("NPC:", self.current_location.npc, "says:")
        print(npc_dialogue)

        if offered_item:
            response = input(f"Will you accept the offered {offered_item}? (yes/no): ")
            if response.lower() == "yes":
                self.insert_item(offered_item)
                print(f"You received {offered_item}.")
            else:
                print(f"You declined the offered {offered_item}.")
        else:
            print("There is no item offered by this NPC.")
    else:
        print("There is no NPC in this area.")

  def puzzle_battle(self):
        print("You have encountered the Lake Spirit!")
        print("Prepare for a puzzle battle.")

        max_attempts = 3
        for attempt in range(1,max_attempts + 1):
            print("\nAttempt", attempt)

            puzzles = [
                ("apple", "pplea"),
                ("banana", "anaban"),
                ("orange", "ngorea")
        ]

            for i, (word, scrambled) in enumerate(puzzles, start=1):
                print(f"\n--- Puzzle {i} ---")
                print("Unscramble the word:", scrambled)
                guess = input("Your guess: ").lower()
                if guess == word:
                    print("Correct!")
                else:
                    print("Incorrect. Try again.")
                    break
            else:
                print("\nCongratulations! You have solved all the puzzles and defeated the Lake Spirit.")
                print("You win the game!")
                return True

        print("\nYou Failed to solve the puzzle. The Lake Spirit overwhelms you.")
        return False 