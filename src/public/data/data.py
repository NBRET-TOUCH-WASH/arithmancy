#coding:utf-8

#type hinting
from typing import Any, List


#modules
import json


#variables
player_data:dict = {
    "race":"sampleTxt",
    "bio":{
        "name":"sampleTxt"
        #"gender":"sampleTxt"
    },
    "class":"sampleTxt",
    "traits":{
        "CON":10,
        "DEX":10,
        "INT":10,
        #"SPD":"sampleTxt",
        "STR":10,
        "WIS":10,
    },
    #"gift":"sampleTxt"
}

#values for the character attributes modifiers, in alphabetical order
player_attributes:List[int] = [10, 10, 10, 10, 10]
player_mods:List[int] = [0, 0, 0, 0, 0]


#functions
#def save_char_data(player_data:dict, field:str="race"|"bio"|"class"|"traits"|"gift", value:Any=None):
#def save_char_data(player_data:dict, field:str, value:Any=None) -> None:
#    """Sets a specified character data (`field`) to a `value` if it is present \
#    in the parsed `player_data` dictionary.\n
#    Returns nothing (`None`)."""

#    #if field in player_data and type(value) == type(player_data[field]):
#    if field in player_data:
#        player_data["bio"] = value
#    else:
#        raise KeyError()

def load_char_data(path:str):
    f = open(path, 'r')
    player_dict:dict = json.load(f)

    with open("public/elements/player/player.json", "w") as json_file:
        json.dump(player_dict, json_file, indent=4)


def create_char_data(creation_args:list):
    player_dict:dict = {
        "race":creation_args[0],
        "bio":{
            "name":creation_args[1]
            #"gender":"sampleTxt"
        },
        "class":creation_args[2],
        "traits":{
            "CON":creation_args[3],
            "DEX":creation_args[4],
            "INT":creation_args[5],
            #"SPD":"sampleTxt",
            "STR":creation_args[6],
            "WIS":creation_args[7],
        },
        #"gift":"sampleTxt"
    }

    with open(f"public/user/char/{creation_args[8]}.json", "w") as json_file:
        json.dump(player_dict, json_file, indent=4)


#def export_json_char(created_player:dict) -> None:
#    """
#    Exports the saved character data to a json file.\n
#    Returns nothing (`None`).
#    """
#    #player_json = json.loads(player_data)

def export_player_attributes(player_attribs:list):
    """
    Exports the saved character data to a json file.\n
    Returns nothing (`None`).
    """
    with open("public/elements/player/player_attributes.json", "w") as json_file:
        json.dump(player_attribs, json_file, indent=4)

def export_player_mods(player_modifiers:list):
    """
    Exports the saved character data to a json file.\n
    Returns nothing (`None`).
    """
    with open("public/elements/player/attributes_modifiers.json", "w") as json_file:
        json.dump(player_modifiers, json_file, indent=4)


def beget_player(player_dict:dict):
    f = open("public/elements/player/player_attributes.json", 'r')
    player_attributes = json.load(f)

    #shitty name but whatev
    player_final_dict:dict = {
    "race":player_dict["race"],
    "bio":{
        "name":player_dict["bio"]["name"]
    },
    "class":player_dict["class"],
    "traits":{
        "CON":player_attributes[0],
        "DEX":player_attributes[1],
        "INT":player_attributes[2],
        "STR":player_attributes[3],
        "WIS":player_attributes[4],
    },
}

    with open("public/elements/player/player.json", "w") as json_file:
        json.dump(player_final_dict, json_file, indent=4)