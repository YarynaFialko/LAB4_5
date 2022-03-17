"""Module with classes for the game."""


class Room():
    """Stores a data about the room."""
    defeated = []

    def __init__(self, room, character=None, item=None, description=None):
        """
        Receives data about the room.
        >>> kitchen = Room("Kitchen")
        >>> kitchen.room
        'Kitchen'
        """
        self.room = room
        self.character = character
        self.item = item
        self.direct = {}
        self.description = description

    def set_description(self, description):
        """
        Sets a description for the room.
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        >>> kitchen.description
        'A dank and dirty room buzzing with flies.'
        """
        self.description = description

    def link_room(self, linked_room, direction):
        """
        >>> kitchen = Room("Kitchen")
        >>> kitchen.link_room("Bedroom", "north")
        >>> kitchen.direct["north"]
        'Bedroom'
        """
        self.direct[direction] = linked_room

    def set_character(self, character):
        """
        Sets a charaacter to the room.
        >>> dining_hall = Room("Dining Hall")
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dining_hall.set_character(dave)
        >>> dining_hall.character.name
        'Dave'
        """
        self.character = character
        character.room = self

    def set_item(self, item):
        """
        >>> dining_hall = Room("Dining Hall")
        >>> dining_hall.set_item(Item("cheese"))
        >>> dining_hall.item.item
        'cheese'
        """
        self.item = item

    def get_details(self):
        """Provides a description of the room."""
        print(self.room)
        print("--------------------")
        print(self.description)
        for item in self.direct.items():
            print(f"The {item[1].room} is {item[0]}")

    def get_character(self):
        """
        >>> dining_hall = Room("Dining Hall")
        >>> dining_hall.set_character(Enemy("Dave", "A smelly zombie"))
        >>> dining_hall.get_character().name  == dining_hall.character.name
        True
        """
        return self.character

    def get_item(self):
        """
        Returns an item of the room.
        >>> dining_hall = Room("Dining Hall")
        >>> dining_hall.set_item(Item("cheese"))
        >>> dining_hall.item.item == dining_hall.get_item().item
        True
        """
        return self.item

    def move(self, direction):
        """
        Returns a room linked to a current one at a given direction.
        >>> dining_hall = Room("Dining Hall")
        >>> dining_hall.link_room(Room("Kitchen"), "south")
        >>> dining_hall.move("south").room
        'Kitchen'
        """
        return self.direct[direction]


class Enemy():
    """Stores a data about an enemy."""

    def __init__(self, name, tipe, conversation=None, weakness=None, room=None):
        """
        Receives input data of the enemy.
        >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
        >>> tabitha.name
        'Tabitha'
        >>> tabitha.tipe
        'An enormous spider with countless eyes and furry legs.'
        """
        self.name = name
        self.tipe = tipe
        self.conversation = conversation
        self.weakness = weakness
        self.room = room

    def set_conversation(self, conversation):
        """
        Defines a conversation of the enemy.
        >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
        >>> tabitha.set_conversation("Sssss....I'm so bored...")
        >>> tabitha.conversation
        "Sssss....I'm so bored..."
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """
        Defines a weakness of the enemy.
        >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
        >>> tabitha.set_weakness("book")
        >>> tabitha.weakness
        'book'
        """
        self.weakness = weakness

    def describe(self):
        """Prints a description of the enemy."""
        print(f"{self.name} is here!\n{self.tipe}")

    def talk(self):
        """Prints a conversation of the enemy."""
        print(self.conversation)

    def fight(self, fight_with):
        """
        Checks whether the fight_with is a a weakness of the enemy.
        >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
        >>> tabitha.set_weakness("book")
        >>> tabitha.fight('cheese')
        False
        >>> tabitha.fight('book')
        True
        """
        return fight_with == self.weakness

    def get_defeated(self):
        """Returns an amount of defeated enemies."""
        self.room.defeated.append(self.name)
        return len(self.room.defeated)


class Item():
    """Stores a data about an item."""

    def __init__(self, item, description = None):
        """
        Receives input data of the item.
        >>> book1 = Item("book")
        >>> book1.item
        'book'
        """
        self.item = item
        self.description = description

    def set_description(self, description):
        """
        Sets a description for the item.
        >>> book1 = Item("book")
        >>> book1.set_description("A really good book entitled 'Knitting for dummies'")
        >>> book1.description
        "A really good book entitled 'Knitting for dummies'"
        """
        self.description = description

    def describe(self):
        """Prints description of an item."""
        print(f"The [{self.item}] is here - {self.description}")

    def get_name(self):
        """
        Returns a name of the item.
        >>> book1 = Item("book")
        >>> book1.item == book1.get_name()
        True
        """
        return self.item
