#coding:utf-8

#modules
from tcod import *

from .events import *

from assets import color_tokens



#functions
def main_char_creation(context:context.Context, console:Console, screen_width:int, screen_height:int):
    """Main character creation segment function."""

    char_creator_event_handler = CharacterCreatorEventHandler()

    while True:
        console.clear()

        #console.print_frame(0,0, screen_width,screen_height, "Character creation")
        #console.draw_frame(0,0, screen_width,screen_height,
        #                    #"Character creation",
        #                    clear=False,
        #                    fg=color_tokens.PEARL.rgb, bg=color_tokens.BLACK.rgb,
        #                    decoration="████ ████")


        console.print(3,3,
                    "Select your character's fantasy race:",
                    color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)
        console.print(3,5,
                    "Human",
                    color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)

        console.print_frame(screen_width-113,15, 35,37, "Info")
        console.print_frame(screen_width-76,15, 35,37, "Racial Feats")

        console.print_frame(screen_width-84,3, 15,10, "Race Symbol")
        console.print(55+15//2,10,
                    "U",
                    color_tokens.WHITE.rgb, color_tokens.BLACK.rgb)

        #little ASCII-art related to the race
        console.print_frame(screen_width-38,3, 35,49)
        console.print(screen_width-32,4, """
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
  █     ██ ██          """)


        context.present(console)

        for current_event in event.wait():
            context.convert_event(current_event)
            print(current_event)
            action = char_creator_event_handler.dispatch(current_event)

            if action is None:
                continue
            elif isinstance(current_event, event.Quit):
                raise SystemExit()