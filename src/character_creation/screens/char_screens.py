#coding:utf-8

#possible_screens = [
#    "RACE_SCREEN",
#    "BIO_SCREEN"
#]

def switch_screen(current_screen:str) -> None:
    """Switches the screen to the next one based on a parsed `current_screen` (`str`).\n
    Returns nothing (`None`).\n
    Currently inplemented"""

    if current_screen == "RACE_SCREEN":
        return "BIO_SCREEN"
    elif current_screen == "BIO_SCREEN":
        return "CLASS_SCREEN"
    elif current_screen == "CLASS_SCREEN":
        return "TRAITS_SCREEN"
    elif current_screen == "TRAITS_SCREEN":
        return "GIFTS_SCREEN"
    #if current_screen == "GIFTS_SCREEN":
    #    return "STATUS_SCREEN"