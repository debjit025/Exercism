"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers to be baked.
    :return: int - total time required to bake the layers.

    Function that takes the number of layers thats going to be in the lasagna as
    an argument and returns how many minutes the layers will need to bake
    based on the `number_of_layers`.
    """
    return PREPARATION_TIME * number_of_layers
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int - number of layers to be baked.
    :param elapsed_bake_time: int - baking time that has already elapsed.
    :return: int - total time baking in the kitchen.

    Function that takes the number of layers thats going to be in the lasagna and takes the elapsed bake time as
    arguments and returns how many minutes I have spent in the kitchen cooking
    based on the `number_of_layers` and 'elapsed_bake_time'.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

#  (you can copy and then alter the one from bake_time_remaining.)
