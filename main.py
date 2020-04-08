import os
os.system('cls')

# colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
print(f"""

                {bcolors.FAIL}███████╗██╗  ██╗███████╗██╗     ██╗         ██████╗ ██╗███████╗
                ██╔════╝██║  ██║██╔════╝██║     ██║         ██╔══██╗██║██╔════╝
                ███████╗███████║█████╗  ██║     ██║         ██║  ██║██║███████╗
                ╚════██║██╔══██║██╔══╝  ██║     ██║         ██║  ██║██║╚════██║
                ███████║██║  ██║███████╗███████╗███████╗    ██████╔╝██║███████║
                ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚═════╝ ╚═╝╚══════╝{bcolors.ENDC}
                                {bcolors.WARNING}Akila Bandara 2020 (c)shell dis{bcolors.ENDC}
                    \n {bcolors.OKGREEN}[*]Author: Akila Bandara
 [*]Follow: www.twitter.com/akilaontweet
 [*]Github: www.github.com/akilaongit{bcolors.ENDC}
""")

file_name = input(" [>]Enter file name: ")
print(" [*]Opening file...")
os.system(f"\ntype {file_name}")
