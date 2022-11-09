#coding:utf-8

#base class
from .race_base import CharCreationRace



#derived classes
class Human(CharCreationRace):
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    is derived from the `CharCreationRace` base class."""

    def __init__(self) -> None:
        self.name = "Human"
        self.symbol = 'U'

        self.racial_feats = [
            "No notable racial feats."
        ]

        self.info = "Homo Sapiens.\n\
        Their complex brain has enabled the development of advanced \
        tools, culture, and language.\n\
        Highly social, they tend to live in complex social structures \
        composed of many cooperating and competing groups."

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