#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 19th, 2022
# This program displays temperatures in a variety of temperature scales
# It displays temperature in a certain scale based on your occupation
# It displays temperature in very uncommon temperature scales


def main():
    # declare a variable that represents the users temperature input in celsius
    user_temp_input_string = input(
        "Enter the temperature in degrees Celsius (°C) as an integer: "
    )
    # use try catch to make sure user properly enters their occupation
    try:
        # convert the input to an integer
        user_temp_input_float = float(user_temp_input_string)
    # use exception if user does not properly input a temperature
    except Exception:
        print("Please properly input a temperature.")

    else:

        # otherwise, carry on with the program if no input errors are met
        # get the users occupation
        user_occupation = str(
            input(
                "What is your occupation (enter “s” if you are a scientist, or “o” if you are anything else): "
            )
        )
        # declare temperature scales and formulas to convert between scales
        deg_newton = user_temp_input_float * 0.33
        deg_rankine = user_temp_input_float * 1.8 + 491.67
        deg_fahrenheit = (user_temp_input_float * 1.8) + 32
        # carriage return for organization
        print(" ")
        # switch case to display the temp scale based on the users occupation
        match user_occupation:
            case "s":
                # display in the rankine and newton scale for a scientist
                print(
                    "Since you are a scientist, you use the Newton (°N) and Rankine (°R) scale when dealing with temperatures: \n"
                )
                print(
                    "The temperature in degrees Rankine is: {0:,.2f} °R. The temperature in degrees Newton is: {1:,.2f} °N.".format(
                        deg_rankine, deg_newton
                    )
                )
            case "o":
                # display in fahrenheit if they have any other occupation
                print(
                    "Since you are not a scientist, you use either degrees Fahrenheit, or Celsius. The temperature in degrees fahrenheit is: {:,.2f} °F".format(
                        deg_fahrenheit
                    )
                )
            case _:
                # default case
                print("Error, invalid occupation.")
        # carriage return for organization
        print(" ")
        # display whether the temperature is cold, warm, or perfect
        # change color depending on which it is:
        # (cold=blue, warm=red, perfect=white)
        if user_temp_input_float <= 15:
            print("\033[1;34mThat is a cold temperature.\n")
        elif user_temp_input_float >= 30:
            print("\033[1;31mThat is a warm temperature.\n")
        else:
            print("\033[1;37mThat is a perfect temperature.\n")
        # convert temperatur in another scale
        réaumur = user_temp_input_float * 0.8
        # input to see if user wants to know a fun fact
        fun_fact = input("Do you want know a fun fact (enter 'yes' or 'no'): ")
        # carriage return for organization
        print(" ")
        # use a try catch to make sure the user validly says yes or no
        try:
            # if yes, display temp in another scale and information about it
            if fun_fact == "yes":
                print(
                    "The melting and boiling points of water are 0 degrees and 80 degrees, respectively, on the Réaumur scale, commonly referred to as the 'octogesimal division,' which measures temperature."
                )
                print(
                    "The temperature in degrees Réaumur is: {:,.2f} °Ré.".format(
                        réaumur
                    )
                )
            else:
                # do not show fact
                print("You just missed out on a cool fact.")
        except Exception:
            # exception for invalid input
            print("Please answer with yes or no.")
        finally:
            print(" ")
    finally:
        print(" ")


if __name__ == "__main__":
    main()
