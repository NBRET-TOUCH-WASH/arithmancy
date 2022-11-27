#coding:utf-8

#module
import argparse



#modules init
#argparse
arg_parser = argparse.ArgumentParser(prog="Arithmancy", description="\"Arithmancy\" | OOP-based ASCII-graphics RPG created by NBRET-TOUCH-WASH | Licensed under [CC-BY-NC-SA 4.0]", exit_on_error=True)
sub_parsers = arg_parser.add_subparsers(title="Sub-commands", description="Available sub-commands when launching Arithmancy.")
#arg_parser.add_argument("-d","--debug", action='store_true', required=False, help="Activates debug mode.")
#arg_parser.add_argument("-t", "--tag", action="store_true", required=False, help="Prints the version tag to the console and exits.")


debug_mode_parser = sub_parsers.add_parser("debug", description="Debug mode commands")
debug_parsers = debug_mode_parser.add_subparsers(title="Debug sub-commands", description="Debugging sub-commands")
debug_mode_parser.add_argument("-a", "--activate", action="store_true", required=False, help="Activates debug mode (has no real effect other than adding a little note on the main screen).")
debug_mode_parser.add_argument("-v", "--verbose", action="store_true", help="Increases output verbosity (prints events to console).")

character_parser = debug_parsers.add_parser("char", description="Character creation debug commands")
char_group = character_parser.add_mutually_exclusive_group(required=True)
char_group.add_argument("-l", "--load", type=str, help="Loads a predefined character `.json` file.")
char_group.add_argument("-c", "--create", nargs=9, help="Creates a new character `.json` file. Requires a RACE, NAME, CLASS, five ATTRIBUTES values and finally a file name (without extension).")

location_parser = debug_parsers.add_parser("loc", description="(TO BE IMPLEMENTED) Character spawn location debug commands")
#char_group = character_parser.add_mutually_exclusive_group(required=True)
#char_group.add_argument("-l", "--load", type=str, help="Loads a predefined character `.json` file.")
#char_group.add_argument("-c", "--create", nargs=9, help="Creates a new character `.json` file. Requires a RACE, NAME, CLASS, five ATTRIBUTES values and finally a file name (without extension).")



cli_args = arg_parser.parse_args()

try:
    DEBUG_ENABLED = cli_args.activate
except AttributeError:
    DEBUG_ENABLED = False

#if DEBUG_ENABLED:
#    print("[DEBUG MODE is enabled.]")
#    try:
#        print(cli_args.load)
#    except AttributeError:
#        pass
#    try:
#        print(cli_args.create)
#    except AttributeError:
#        pass