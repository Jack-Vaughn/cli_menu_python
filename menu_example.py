#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
data_analysis.py
Jack Vaughn
SDEV 300 - 6380
Building Secure Python Applications
Professor Khan
09 Jun 2020

LOAD ONE OF TWO PROVIDED CSV FILES AND PERFORM HISTOGRAM ANALYSIS AND PLOTS FOR SELECTING
VARIABLES ON THE DATASET
"""

__author__ = 'Jack Vaughn'
__license__ = '0BSD'
__version__ = '0.1.0'
__maintainer__ = 'Jack Vaughn'
__email__ = 'jack.vaughn0523@gmail.com'
__status__ = 'Production'

import csv

import pandas as pd
import matplotlib.pyplot as plt

from menu import *
from population_change import PopulationChange
from house import House


def get_stats(df: pd.DataFrame, column_name: str) -> None:
    """
    PRINT THE REQUIRED STATES OF THE COLUMN IN THE DATAFRAME
    THE WHOLE DATAFRAME IS REQUIRED FOR GRAPHING PURPOSES
    :param df: DataFrame
    :param column_name: DataFrame Column Name
    :return: None
    """
    df_slice = df[column_name]
    print(f'Count: {df_slice.count()}')
    print(f'Mean: {round(df_slice.mean(), 1)}')
    print(f'Standard Deviation: {round(df_slice.std(), 1)}')
    print(f'Min: {round(df_slice.min(), 1)}')
    print(f'Max: {round(df_slice.max(), 1)}')

    # LOAD AND SAVE THE HISTOGRAM
    df.hist(column=column_name)
    filename = f'{column_name}.svg'
    plt.savefig(filename)
    print(f'Histogram saved as "{filename}"')


def population_data() -> None:
    """
    HANDLE THE POPULATION_DATA MENU WHEN THE USER SELECTS POPULATION
    :return: None
    """
    # population = pd.read_csv('PopChange.csv')
    # I AM ALL FOR OOP, AND SOMETIMES BELIEVE I DO IT TOO MUCH, HOWEVER,
    # THE CODE BETWEEN THE LINES SEEMS LIKE A FAR OVERCOMPLICATED WAY OF DOING
    # WHAT THE COMMENTED CODE ABOVE DOES, BUT IT HAD TO MEET
    # SYLLABUS REQUIREMENTS
    # ----------------------------------------------------------------------
    population_changes = []
    with open('PopChange.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            population_changes.append(PopulationChange(*line))
    population = pd.DataFrame([p.to_dict() for p in population_changes])
    # ----------------------------------------------------------------------

    population_menu = Menu(
        prompt='Select the Column you want to analyze:',
        menu_options={
            'a': MenuOption(
                menu_text='Pop Apr 1',
                confirmation_text='You selected Pop Apr 1',
                alternatives=['A'],
                function=lambda: get_stats(population, PopulationChange.Columns.pop_apr_1)
            ),

            'b': MenuOption(
                menu_text='Pop Jul 1',
                confirmation_text='You selected Pop Jul 1',
                alternatives=['B'],
                function=lambda: get_stats(population, PopulationChange.Columns.pop_jul_1)
            ),

            'c': MenuOption(
                menu_text='Change Pop',
                confirmation_text='You selected Change Pop',
                alternatives=['C'],
                function=lambda: get_stats(population, PopulationChange.Columns.change_pop)
            ),

            'd': MenuOption(
                menu_text='Exit Column',
                confirmation_text='You selected to exit the column population_menu',
                alternatives=['D'],
                exit_option=True
            )
        }
    )
    # CONTINUE LOOPING THROUGH THE MENU UNTIL THE USER EXITS
    while not population_menu.should_exit:
        population_menu.show_prompt()
        population_menu.show()
        population_menu.choose_option()


def housing_data() -> None:
    """
    HANDLE THE HOUSING_DATA MENU WHEN THE USER SELECTS POPULATION
    :return: None
    """
    # housing = pd.read_csv('Housing.csv')
    # I AM ALL FOR OOP, AND SOMETIMES BELIEVE I DO IT TOO MUCH, HOWEVER,
    # THE CODE BETWEEN THE LINES SEEMS LIKE A FAR OVERCOMPLICATED WAY OF DOING
    # WHAT THE COMMENTED CODE ABOVE DOES, BUT IT HAD TO MEET
    # SYLLABUS REQUIREMENTS
    # ----------------------------------------------------------------------
    houses = []
    with open('Housing.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            houses.append(House(*line))
    housing = pd.DataFrame([p.to_dict() for p in houses])
    # ----------------------------------------------------------------------

    housing_menu = Menu(
        prompt='Select the Column you want to analyze:',
        menu_options={
            'a': MenuOption(
                menu_text='AGE',
                confirmation_text='You selected AGE',
                alternatives=['A'],
                function=lambda: get_stats(housing, House.Columns.age)
            ),

            'b': MenuOption(
                menu_text='BEDRMS',
                confirmation_text='You selected BEDRMS',
                alternatives=['B'],
                function=lambda: get_stats(housing, House.Columns.bedrms)
            ),

            'c': MenuOption(
                menu_text='BUILT',
                confirmation_text='You selected BUILT',
                alternatives=['C'],
                function=lambda: get_stats(housing, House.Columns.built)
            ),

            'd': MenuOption(
                menu_text='ROOMS',
                confirmation_text='You selected ROOMS',
                alternatives=['D'],
                function=lambda: get_stats(housing, House.Columns.rooms)
            ),

            'e': MenuOption(
                menu_text='UTILITY',
                confirmation_text='You selected UTILITY',
                alternatives=['E'],
                function=lambda: get_stats(housing, House.Columns.utility)
            ),

            'f': MenuOption(
                menu_text='Exit Column',
                confirmation_text='You selected to exit the column housing_menu',
                alternatives=['F'],
                exit_option=True
            )
        }
    )
    # CONTINUE LOOPING THROUGH THE MENU UNTIL THE USER EXITS
    while not housing_menu.should_exit:
        housing_menu.show_prompt()
        housing_menu.show()
        housing_menu.choose_option()


if __name__ == '__main__':

    # CREATES A MENU AND MENU OPTIONS, THE NAMED ARGUMENTS SHOULD BE SELF EXPLANATORY
    app_name = 'Python Data Analysis'
    menu = Menu(
        prompt=f'********* Welcome to the  {app_name} Application*********',
        menu_options={
            '1': MenuOption(
                menu_text='Population Data',
                confirmation_text='You have entered Population Data.',
                function=lambda: population_data()
            ),

            '2': MenuOption(
                menu_text='Housing Data',
                confirmation_text='You have entered Housing Data',
                function=lambda: housing_data()
            ),

            '3': MenuOption(
                menu_text='Exit the Program',
                confirmation_text=f'Thanks for trying the {app_name} Application.',
                exit_option=True
            )
        }
    )
    # CONTINUE LOOPING THROUGH THE MENU UNTIL THE USER EXITS
    while not menu.should_exit:
        menu.show_prompt()
        menu.show()
        menu.choose_option()
