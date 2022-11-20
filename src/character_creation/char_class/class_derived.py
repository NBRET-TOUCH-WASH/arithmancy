#coding:utf-8

#modules
from assets import color_tokens


#base class
from .class_base import CharCreationClass



#derived classes
class Mage(CharCreationClass):
    def __init__(self) -> None:
        self.name = "Mage"

        self.color = color_tokens.TEAL.rgb
        self.info = "Someone who uses or practices magic derived from arcane sources.\n\nThey can also be capable of great magic, both good or evil; which draws on various schools of philosophical and occult thought as well as the magic of various grimoires.\n\nThe practice of arcane magic often requires tools made or consecrated specifically for this use, which are required for a particular ritual or series of rituals. They may be a symbolic representation of psychological elements of the mage or of metaphysical concepts."
        self.attributes_modifiers = {'TXT':'?'}

        self.artwork = R"""
                                 
                                 
                                 
                                 
                                 
                                 
      ______________________     
     (0RGSDOFCJftli;:.:. .  )    
      T''''''''''''''''''''T     
      |.;....,..........;..|     
      |;;:: .  .    .      |     
      l;;;:. :   .     ..  ;     
      `;;:::.: .    .     .'     
       l;;:. ..  .     .: ;      
       `;;::.. .    .  ; .'      
        l;;:: .  .    /  ;       
         \;;:. .   .,'  /        
          `\;:.. ..'  .'         
            `\;:.. ..'           
              \;:. /             
               l; f              
               `;f'              
                ||               
                ;l.              
               ;: l              
              / ;  \             
            ,/  :   `.           
          ./' . :     `.         
         /' ,'  :       \        
        f  /  . :        i       
       ,' ;  .  :        `.      
       f ;  .   :      .  i      
      .'    :   :       . `.     
      f ,  .    ;       :  i     
      |    :  ,/`.       : |     
      |    ;,/;:. `.     . |     
      |___,/;;:. . .`._____|     
     (QB0ZDOLC7itz!;:.:. .  )    
      ''''''''''''''''''''''     
                                 
                                 
                                 
                                 
                                 
                                 
"""




class Necromancer(CharCreationClass):
    def __init__(self) -> None:
        self.name = "Necromancer"

        self.color = color_tokens.FUSCHIA.rgb
        self.info = "Someone who uses or practices magic derived from occult sources.\n\nTheir practice of black magic involves communication with the dead, discovery of hidden knowledge; returning a person to life, or to use the dead as a weapon.\n\nThe act of performing necromancy usually involves magic circles, conjurations, and sacrifices."
        self.attributes_modifiers = {'TXTT':'??'}

        #based on this kanji (done by me ^^) : 死
        #previously used a skull but i think this is a little neater
        self.artwork = R"""
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
       ████████████████████      
           █         █           
          ████████   █   █       
         ██      █   █  █        
        █ █     █    █ █         
       █   █  ██     ██          
            ███      █           
           ██        █    █      
          ██         █    █      
         █           █████       
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
"""

#        self.artwork = R"""
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
#          _,.-------.,_          
#      ,;~'             '~;,      
#    ,;                     ;,    
#   ;                         ;   
#  ,'                         ',  
# ,;                           ;, 
# ; ;      .           .      ; ; 
# | ;   ______       ______   ; | 
# |  `/~"     ~" . "~     "~\'  | 
# |  ~  ,-~~~^~, | ,~^~~~-,  ~  | 
#  |   |        }:{        |   |  
#  |   l       / | \       !   |  
#  .~  (__,.--" .^. "--.,__)  ~.  
#  |     ---;' / | \ `;---     |  
#   \__.       \/^\/       .__/   
#    V| \                 / |V    
#     | |T~\___!___!___/~T| |     
#     | |`IIII_I_I_I_IIII'| |     
#     |  \,III I I I III,/  |     
#      \   `~~~~~~~~~~'    /      
#        \   .       .   /        
#          \.    ^    ./          
#            ^~~~^~~~^            
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
#"""



class Priest(CharCreationClass):
    def __init__(self) -> None:
        self.name = "Priest"

        self.color = color_tokens.GOLDEN_YELLOW.rgb
        self.info = "Someone who uses or practices magic derived from sacred sources.\n\nIntermediaries between the mortal world and the distant planes of the gods, and as varied as the gods they serve. They strive to embody the handiwork of their deities.\n\nNo ordinary priest, a cleric is imbued with divine magic, the power of their spells directly linked to the intensity of the devotion to their deity."
        self.attributes_modifiers = {'TXTTT':'???'}

        self.artwork = R"""
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                  ,              
               ,-`;              
        ,      ; ;      ,        
       ,  `'"""   """'`  ,       
      , ,-'````, ,````'-, ,      
      ``    ,'`` ``',    ``      
           ' ,`; ;`, '           
           `,`,; ;,',`           
           ,'` ,  ,`             
      -, '`,-'`; ;',`, ,         
      `,,'`    ; ;  `,`,`        
               ; ;    `          
               ;  '-             
               ; '`              
               ` `               
              , '                
             ,'`:, '             
              , - `              
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
"""



class Warrior(CharCreationClass):
    def __init__(self) -> None:
        self.name = "Warrior"

        self.color = color_tokens.CRIMSON.rgb
        self.info = "Someone who shares an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat.\n\nWell acquainted with death, both meting it out and staring it defiantly in the face, they focus themselves on combat abilities, most often at the expense of magical abilities.\n\nDuring training, they gradually adopt a particular style of fighting as their specialty, and use rage as a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength."
        self.attributes_modifiers = {'TXTTTT':'????'}

        self.artwork = """
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
           ,:\      /:.          
          //  \_()_/  \\         
         ||   |    |   ||        
         ||   |    |   ||        
         ||   |____|   ||        
          \\  / || \  //         
           `:/  ||  \;'          
                ||               
                ||               
                XX               
                XX               
                XX               
                XX               
                OO               
                `'               
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
"""