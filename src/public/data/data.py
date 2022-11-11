#coding:utf-8

#type hinting
from typing import Any


#modules
import json


#variables
player_data = {
    "race":"sampleTxt",
    "bio":{
        "name":"sampleTxt",
        "gender":"sampleTxt"
    },
    "class":"sampleTxt",
    "traits":{
        "CON":"sampleTxt",
        "DEX":"sampleTxt",
        "INT":"sampleTxt",
        "SPD":"sampleTxt",
        "STR":"sampleTxt",
        "WIS":"sampleTxt",
    },
    "gift":"sampleTxt"
}


#functions
#def save_char_data(player_data:dict, field:str="race"|"bio"|"class"|"traits"|"gift", value:Any=None):
def save_char_data(player_data:dict, field:str, value:Any=None) -> None:
    """Sets a specified character data (`field`) to a `value` if it is present \
    in the parsed `player_data` dictionary.\n
    Returns nothing (`None`)."""

    #if field in player_data and type(value) == type(player_data[field]):
    if field in player_data:
        player_data[field] = value
    else:
        raise KeyError()


def export_json_char(player_data:dict) -> None:
    """
    Exports the saved character data to a json file.\n
    Returns nothing (`None`).
    """
    #player_json = json.loads(player_data)

    with open("public/elements/player/character_creation.json", "w") as json_file:
    #with open("character_creation.json", "w") as json_file:
        json.dump(player_data, json_file, indent=4)