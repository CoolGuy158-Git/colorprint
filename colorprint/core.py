###########################################################
# Colorprint- Python module that lets you print colorfully#
# Under MIT license CoolGuy158-Git                        #
###########################################################

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

def cprint(text, color="RESET"):
    color_code = getattr(Colors, color.upper(), Colors.RESET)
    print(f"{color_code}{text}{Colors.RESET}")
