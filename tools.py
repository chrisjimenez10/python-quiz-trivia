import os


def clear_console():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


logo = r"""
   ____              __               ____           __          __           
  F __ ]    _    _   LJ   _____      /_  _\  _ ___   LJ  _    _  LJ    ___ _  
 J |--| L  J |  | L      [__   F     [J  L] J '__ ",    J |  | L      F __` L 
 | | _| |  | |  | |  FJ  `-.'.'/      |  |  | |__|-J FJ J J  F L FJ  | |--| | 
 F L_F  J  F L__J J J  L .' (_(_      F  J  F L  `-'J  LJ\ \/ /FJ  L F L__J J 
J\_____  \J\____,__LJ__LJ_______L    J____LJ__L     J__L \\__// J__LJ\____,__L
 J_____\J] J____,__F|__||_______|    |____||__L     |__|  \__/  |__| J____,__F
       \J                                                                     
"""
