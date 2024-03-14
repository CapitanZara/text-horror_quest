# Let's develop the text-based horror quest game in Python.

# Import necessary modules
import sys

# Define the game's rooms and objects
rooms = {
    "Гостиная": {
        "description": "Вы находитесь в гостиной. Комната кажется пустой, но вы чувствуете чей-то взгляд.",
        "items": ["старый дневник", "зажигалка"],
        "danger": False,
        "next_rooms": ["Кухня", "Спальня"]
    },
    "Кухня": {
        "description": "Вы в кухне. Странно, но здесь чувствуется запах свежего хлеба.",
        "items": ["нож", "хлеб"],
        "danger": True,  # Пример комнаты, где игрок может встретиться с злым духом
        "next_rooms": ["Гостиная"]
    },
    "Спальня": {
        "description": "Это ваша спальня. Здесь должно быть безопасно... Надеюсь.",
        "items": [],
        "danger": False,
        "next_rooms": ["Гостиная"]
    }
}

# Update items to include descriptions and potential effects
items_descriptions = {
    "старый дневник": "Старый пыльный дневник, на обложке которого выгравированы странные символы. Возможно, в нем есть подсказки.",
    "зажигалка": "Старинная зажигалка. Может пригодиться в темноте.",
    "нож": "Острый кухонный нож. Кажется, недавно им пользовались.",
    "хлеб": "Свежий, еще теплый хлеб. Странно находить его здесь."
}


# Initialize game state
current_room = "Гостиная"
inventory = []


# Define functions for game actions
def move_to_room(room):
    """Move the player to a different room."""
    global current_room
    if room in rooms[current_room]["next_rooms"]:
        current_room = room
        print("Вы переместились в:", room)
        describe_room(room)
    else:
        print("Вы не можете туда пойти.")


def describe_room(room):
    """Describe the current room to the player."""
    print(rooms[room]["description"])
    if rooms[room]["items"]:
        print("В комнате вы видите:", ", ".join(rooms[room]["items"]))


# Update the examine_item function to provide more information and interact with the game state
def examine_item(item):
    """Examine an item in the room, providing details and triggering any effects."""
    if item in rooms[current_room]["items"]:
        print(f"Вы осмотрели {item}. {items_descriptions[item]}")
        # Here you can add conditional statements to change the game state based on item examination
        # For example, finding a clue in the diary might unlock a new room or reveal a hidden object
    else:
        print("Здесь нет такого предмета.")



def take_item(item):
    """Take an item from the room."""
    if item in rooms[current_room]["items"]:
        inventory.append(item)
        rooms[current_room]["items"].remove(item)
        print(f"Вы взяли {item}.")
    else:
        print("Здесь нет такого предмета.")


def check_danger():
    """Check if the current room is dangerous."""
    if rooms[current_room]["danger"]:
        print("В комнате появился злой дух! Вы погибли.")
        sys.exit()


# Game introduction
game_intro_text = """Добро пожаловать в текстовый квест ужасов. 
Ваша задача - исследовать дом и выжить. Удачи!
Доступные команды 
идти
осмотреть-название предмета
взять
"""
print(game_intro_text)
describe_room(current_room)


while True:
    command = input("> ").split("-")
    print(command)
    action = command[0]
    if action == "идти":
        if len(command) > 1:
            move_to_room(command[1])
            check_danger()
        else:
            print("Куда идти?")
    elif action == "осмотреть":
        if len(command) > 1:
            examine_item(command[1])
        else:
            print("Что осмотреть?")
    elif action == "взять":
        if len(command) > 1:
            take_item(command[1])
        else:
            print("Что взять?")
    else:
        print("Неизвестная команда.")
