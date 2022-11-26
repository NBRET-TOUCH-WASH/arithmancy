#coding:utf-8

#base class
from .race_base import CharCreationRace
from .racial_feat import *



#derived classes
class Dwarf(CharCreationRace):
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    is derived from the `CharCreationRace` base class.
    
    Dwarven class"""

    def __init__(self) -> None:
        self.name = "Dwarf"
        self.symbol = '☺ | ☻'

        self.racial_feats = [
            CecityImmunity(),
            Alcoholism()
        ]

        self.info = """
An entity that dwells in the mountains and in the earth.

They are associated with wisdom, smithing, mining, and crafting.

Dwarves are sometimes described as short and ugly. However, some scholars have - under Dwarven Armed Psychological Advantage (DAPA) - questioned whether this is a later development stemming from comical portrayals of the beings."""

        #! ascii art by Stef ( https://www.asciiart.eu/miscellaneous/candles )
        self.artwork = R"""
                                
                                
                                
                                
                                
            __,---.__           
         ,-'         `-.        
       ,'               `.      
      /                   \     
     /         .           \    
    ;           )           :   
    |          ((           |   
    |          ) \          |   
    :         ( , )         ;   
     \       _ `|'__       /    
      \     ( \"""\"_ )   /     
       `.    )/(/( \|   ,'      
         `- ()  )()|| -'        
             | ()  ||           
             |     ||           
             |     ()           
             |     |            
             |     |            
             |     |            
             |     |            
         ____|_____|____        
        (________    ___)       
           \___     _/          
           (_____  __)          
            \       /           
             )__   (            
            (____  _)           
              |   |             
              |   |             
              |   |             
              |   |             
              |   |             
              |   |             
              |   |             
            _/     \_           
        .--'_________`--.       
                                
                                
                                
                                
                                """


#==========#


class Elf(CharCreationRace):
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    is derived from the `CharCreationRace` base class.
    
    Elven class"""

    def __init__(self) -> None:
        self.name = "Elf"
        self.symbol = 'e'

        self.racial_feats = [
            BiologicalImmortality(),
            Cuteness(),
            ProtectorOfNature()
        ]

        self.info = """
Pointy-eared beings with magical powers and supernatural beauty, ambivalent towards everyday people and capable of either helping or hindering them.

Their key traits include being friendly with nature and animals (oftentimes being able to communicate with some facet of nature), immortal or long-lived in comparison to humans, more beautiful and wiser, with sharper senses, perceptions and abilities or crafts that seem alien or magical.

They most often appear tall, slim and androgynous."""

        #! ascii art by Stef ( https://www.asciiart.eu/miscellaneous/candles )
        self.artwork = R"""
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                * *             
             *    *  *          
        *  *    *     *  *      
       *     *    *  *    *     
   * *   *    *    *    *   *   
   *     *  *    * * .#  *   *  
   *   *     * #.  .# *   *     
    *     "#.  #: #" * *    *   
   *   * * "#. ##"       *      
     *       "###               
               "##              
                ##.             
                .##:            
                :###            
                ;###            
              ,####.            
  /\/\/\/\/\/.######.\/\/\/\/\  
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                """


#==========#


class Human(CharCreationRace):
    """Represents a race in the character creation segment. \
    Is not used in the main gameplay section.\n
    is derived from the `CharCreationRace` base class.
    
    Human class"""

    def __init__(self) -> None:
        self.name = "Human"
        self.symbol = 'U'

        self.racial_feats = []
        self.handle_no_feats()

        self.info = """
\"Homo Sapiens\".

Their complex brain has enabled the development of advanced tools, culture, and language.

Highly social, they tend to live in complex social structures composed of many cooperating and competing groups.

Genes and the environment influence human biological variation in visible characteristics, physiology, disease susceptibility, mental abilities, body size and life span."""

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
       █     ██ ██               
                                 """