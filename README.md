# cli_menu_python

An single file, easy to use Python CLI menu.

Example below

`
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
 `
