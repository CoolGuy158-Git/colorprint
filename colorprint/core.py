###########################################################
# Colorprint- Python module that lets you print colorfully#
# With CSS-like chaining in terminal                      #
# MIT license CoolGuy158-Git                               #
###########################################################

class Colors:
    # Text colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    STRIKETHROUGH = "\033[9m"

def cprint(text, cstyle="RESET"):
    style_codes = cstyle.upper().split("+")
    codes = ""
    for style in style_codes:
        codes += getattr(Colors, style, "")
    print(f"{codes}{text}{Colors.RESET}")
