#coding:utf-8

#base class
from .race_base import CharCreationRace



#derived classes
class Human(CharCreationRace):
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    is derived from the `CharCreationRace` base class.
    
    Human class"""

    def __init__(self) -> None:
        self.name = "Human"
        self.symbol = 'U'

        self.racial_feats = [
            "No notable racial feats."
        ]

        self.info = """
\"Homo Sapiens\".

Their complex brain has enabled the development of advanced tools, culture, and language.

Highly social, they tend to live in complex social structures composed of many cooperating and competing groups."""

        self.artwork = """
██    ███   ██    ██   
█             ██  █    
██ █   ██   ██    ██ █ 
█████ █████ █████ █████
                       
   █                 █ 
                       
    █                 █
█████             █████
                       
██    ██    ███   ██   
█       █         █    
██ █    ██   ███  ██ █ 
█████ █████ █████ █████
                       
   █      ██         █ 
          ██           
    █     ██          █
█████     ██      █████
          ██           
  █        █        █  
   █      ██       █   
    ██    ██      █    
      ██   █    ██     
          ██  ██       
      ██   █    ██     
    ██    ██      █    
   █      █        █   
  █       ██        █  
 █        ██        █  
 █         █       █   
  █       █       █    
   █            ██     
    ██        ██       
  █   ███ █ ██         
  █       █            
  █     █████          
  █    █ ███ █  █ ██ ██
      █  ███  █  ██████
█ ███    ███     ██ ███
         █ █     ███ ██
  █      █ █     ██████
  █      █ █     ██    
  █     ██ ██          """



class Dwarf(CharCreationRace):
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    is derived from the `CharCreationRace` base class.
    
    Dwarven class"""

    def __init__(self) -> None:
        self.name = "Dwarf"
        self.symbol = '☺ | ☻'

        self.racial_feats = [
            "Cecity immunity"
        ]

        self.info = """
An entity that dwells in the mountains and in the earth.

They are associated with wisdom, smithing, mining, and crafting.

Dwarves are sometimes described as short and ugly. However, some scholars have questioned whether this is a later development stemming from comical portrayals of the beings."""

        self.artwork = """
██    ███   ██    ██   
█             ██  █    
██ █   ██   ██    ██ █ 
█████ █████ █████ █████
                       
   █                 █ 
                       
    █                 █
█████             █████
                       
██    ██    ███   ██   
█       █         █    
██ █    ██   ███  ██ █ 
█████ █████ █████ █████
                       
   █      ██         █ 
          ██           
    █     ██          █
█████     ██      █████
          ██           
  █        █        █  
   █      ██       █   
    ██    ██      █    
      ██   █    ██     
          ██  ██       
      ██   █    ██     
    ██    ██      █    
   █      █        █   
  █       ██        █  
 █        ██        █  
 █         █       █   
  █       █       █    
   █            ██     
    ██        ██       
  █   ███ █ ██         
  █       █            
  █     █████          
  █    █ ███ █  █ ██ ██
      █  ███  █  ██████
█ ███    ███     ██ ███
         █ █     ███ ██
  █      █ █     ██████
  █      █ █     ██    
  █     ██ ██          """