#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
menu_example.py
Provides an example for using the menu
"""

__author__ = 'Jack Vaughn'
__license__ = '0BSD'
__version__ = '0.1.0'
__maintainer__ = 'Jack Vaughn'
__email__ = 'jack.vaughn0523@gmail.com'
__status__ = 'Production'


from menu import Menu, MenuOption


def play():
    pass


if __name__ == '__main__':

    # CREATES A MENU AND MENU OPTIONS, THE NAMED ARGUMENTS SHOULD BE SELF EXPLANATORY
    app_name = 'Python Matrix'
    menu = Menu(
        prompt=f'********* Welcome to the  {app_name} Application*********\n'
               f'   Do you want to play the Matrix Game?\n'
               f'   Enter Y for Yes or N for No',
        menu_options={
            'Y': MenuOption(
                menu_text='Yes, I do want to play the game',
                confirmation_text='',
                alternatives=['y', 'Yes', 'yes'],
                function=lambda: play()
            ),

            'N': MenuOption(
                menu_text='No, I do not want to play the game',
                confirmation_text=f'Thanks for trying the {app_name} Application.',
                alternatives=['n', 'No', 'no'],
                exit_option=True
            )
        }
    )
    # CONTINUE LOOPING THROUGH THE MENU UNTIL THE USER EXITS
    while not menu.should_exit:
        menu.show_prompt()
        menu.show()
        menu.choose_option()
