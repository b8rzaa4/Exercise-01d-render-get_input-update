#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "425C890A-DB29-4F1E-B5D5-571B525B9786",
  "name": "Zork",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631039870289,
  "passages": [
    {
      "name": "West of House",
      "tags": "",
      "id": "1",
      "text": "This is an openfied west of a white hose, with a boarded front door.\n[[NORTH->North of House]]\n[[SOUTH->South of House]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is an openfied west of a white hose, with a boarded front door."
    },
    {
      "name": "North of House",
      "tags": "",
      "id": "2",
      "text": "You are facing the north side of a white house. There is no door here, and all the windows are barred.\nExits:\n[[WEST->West of house]]\n[[EAST->East of house]]\n[[NORTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of house",
          "original": "[[WEST->West of house]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of house",
          "original": "[[EAST->East of house]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the north side of a white house. There is no door here, and all the windows are barred.\nExits:"
    },
    {
      "name": "South of House",
      "tags": "",
      "id": "3",
      "text": "You are facing the south side of a white house. There is no door here, and all the windows are barred. \nExits:\n[[WEST->West of House]]\n[[EAST->East of house]] \n[[SOUTH->Forest]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
          "original": "[[WEST->West of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East of house",
          "original": "[[EAST->East of house]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are facing the south side of a white house. There is no door here, and all the windows are barred. \nExits:"
    },
    {
      "name": "Forest",
      "tags": "",
      "id": "4",
      "text": "There is a forest, with trees in all directions around you.\nExits\n[[NORTH->Sunlit Forest]]\n[[EAST->Forest]]\n[[SOUTH->Forest]]\n[[WEST->Forest]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Sunlit Forest",
          "original": "[[NORTH->Sunlit Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Forest",
          "original": "[[WEST->Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is a forest, with trees in all directions around you.\nExits"
    },
    {
      "name": "West of house",
      "tags": "",
      "id": "5",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    },
    {
      "name": "East of house",
      "tags": "",
      "id": "6",
      "text": "You are behind the white house. A path leads into the forest in the east. In one corner of the house there is a small window which is slightly ajar.\nExits:\n[[NORTH->North of House]]\n[[SOUTH->South of House]] \n[[EAST->Sunlit Forest]] \n[[WEST->Kitchen]]\n[[ENTER->Kitchen]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
          "original": "[[NORTH->North of House]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South of House",
          "original": "[[SOUTH->South of House]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Sunlit Forest",
          "original": "[[EAST->Sunlit Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Kitchen",
          "original": "[[WEST->Kitchen]]"
        },
        {
          "linkText": "ENTER",
          "passageName": "Kitchen",
          "original": "[[ENTER->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are behind the white house. A path leads into the forest in the east. In one corner of the house there is a small window which is slightly ajar.\nExits:"
    },
    {
      "name": "Sunlit Forest",
      "tags": "",
      "id": "7",
      "text": "There is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.\nExits:\n[[NORTH->Forest]]\n[[SOUTH->Forest]] \n[[EAST->Forest]] \n[[WEST->East of house]] \n[[UP->Tree]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "Forest",
          "original": "[[NORTH->Forest]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Forest",
          "original": "[[SOUTH->Forest]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Forest",
          "original": "[[EAST->Forest]]"
        },
        {
          "linkText": "WEST",
          "passageName": "East of house",
          "original": "[[WEST->East of house]]"
        },
        {
          "linkText": "UP",
          "passageName": "Tree",
          "original": "[[UP->Tree]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is a dimly lit forest, with large trees all around. One particularly large tree with some low branches stands here.\nExits:"
    },
    {
      "name": "Kitchen",
      "tags": "",
      "id": "8",
      "text": "You are in the kitchen of the white house. A table seems to have been used recently for the prepatation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.\nExits:\n[[EAST->East of house]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "East of house",
          "original": "[[EAST->East of house]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are in the kitchen of the white house. A table seems to have been used recently for the prepatation of food. A passage leads to the west and a dark staircase can be seen leading upward. A dark chimney leads down and to the east is a small window which is open.\nExits:"
    },
    {
      "name": "Tree",
      "tags": "",
      "id": "9",
      "text": "You are about 10 feet above the ground and nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\nExits:\n[[DOWN->Sunlit Forest]]",
      "links": [
        {
          "linkText": "DOWN",
          "passageName": "Sunlit Forest",
          "original": "[[DOWN->Sunlit Forest]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are about 10 feet above the ground and nestled among some large branches. The nearest branch above you is above your reach. Beside you on the branch is a small bird's nest.\nExits:"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location):
	print("You are at the " = current_location["name"])
	print(current_location["cleanText"])
	pass

def get_input():
	response = input("What do you want to do? ")
	response = response.upper.strip
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label

	for link in current_location["links"]:
		if link["linkText"] == response:
			return link["psaageName"]

	print("I didn't understand that. Please try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "West of House"
current_location = {}
response = ""

while True:
	if response == "QUIT":
		break
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	render(current_location)
	response = get_input()


print("Thanks for playing!")