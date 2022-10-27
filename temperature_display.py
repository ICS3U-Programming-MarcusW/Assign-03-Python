#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 19th, 2022
# This program displays temperatures in a variety of temperature scales
# It displays temperature in a certain scale based on your occupation
# It displays temperature in very uncommon temperature scales


#potential option 1 - isinstance(var, int/float)
#potential option 2 - user_temp_input_string % 1 != 0
# if user_temp_input_string.isdigit():
#     print(" ")
# else:
#     print("Please enter a proper integer for the temperature.")
#     __name__ = 0


def main():
    # declare a variable that represents the users temperature in celsius
    user_temp_input_string = input(
        "Enter the temperature in degrees Celsius (°C) as an integer: "
    )
    
    try:
        
        user_temp_input_float = float(user_temp_input_string)
        

    except Exception:
        print("Please properly indicate your occupation.")

    else:
        
        # this function gets a temperature from the user, and converts it into different scales
        user_occupation = str(
            input(
                "What is your occupation (enter “s” if you are a scientist, or “o” if you are anything else):"
            )
        )

        # declare temperature scales and formulas
        deg_newton = user_temp_input_float * 0.33
        deg_rankine = user_temp_input_float + 493.47
        deg_fahrenheit = (user_temp_input_float * 1.8) + 32
        match user_occupation:
            case "s":
                print(
                    "Since you are scientist, you use the Newton (°N) and Rankine (°R) scale when dealing with temperatures: \n"
                )
                print(
                    "The temperature in degrees Rankine is: {0:,.2f} °R. The temperature in degrees Newton is: {1:,.2f} °N.".format(
                        deg_rankine, deg_newton
                    )
                )
            case "o":
                print(
                    "Since you are not a scientist, you use either degrees Fahrenheit, or Celsius. The temperature in degrees fahrenheit is: {}".format(
                        deg_fahrenheit
                    )
                )
            case _:
                print("Error, invalid occupation.")

        if user_temp_input_float <= 15:
            print("\033[1;34mThat is a cold temperature.\n")
        elif user_temp_input_float >= 30:
            print("\033[1;31mThat is a warm temperature.\n")
        else:
            print("\033[1;37mThat is a perfect temperature.\n")

        réaumur = user_temp_input_float * 0.8
        fun_fact = input("Do you want know a fun fact (enter 'yes' or 'no'): ")
        try:
            if fun_fact == "yes":
                print(
                    "The melting and boiling points of water are 0 degrees and 80 degrees, respectively, on the Réaumur scale, commonly referred to as the 'octogesimal division,' which measures temperature."
                )
                print("The temperature in degrees Réaumur is: {:,.2f} °Ré.".format(réaumur))
            else:
                print("You just missed out on a cool fact.")
        except Exception:
            print("Please answer with yes or no.")
        finally:
            print(" ")
    finally:
        print(" ")


def coohot():
    #user_temp_input_float = float(user_temp_input_string)
    # this function reads the temperature and says if it is hot, cold, or in between
    if user_temp_input_float <= 15:
        print("\033[1;34mThat is a cold temperature.\n")
    elif user_temp_input_float >= 30:
        print("\033[1;31mThat is a warm temperature.\n")
    else:
        print("\033[1;37mThat is a perfect temperature.\n")


def fact():
    #user_temp_input_float = float(user_temp_input_string)
    # this function gets a temperature from the user, and converts it into different scales
    réaumur = user_temp_input_float * 0.8
    fun_fact = input("Do you want know a fun fact (enter 'yes' or 'no'): ")
    try:
        if fun_fact == "yes":
            print(
                "The melting and boiling points of water are 0 degrees and 80 degrees, respectively, on the Réaumur scale, commonly referred to as the 'octogesimal division,' which measures temperature."
            )
            print("The temperature in degrees Réaumur is: {:,.2f} °Ré.".format(réaumur))
        else:
            print("You just missed out on a cool fact.")
    except Exception:
        print("Please answer with yes or no.")
    finally:
        print(" ")


if __name__ == "__main__":
    main()
    #coohot()
    #fact()
