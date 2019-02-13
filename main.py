import datetime

import conversions

def main():
    print('Welcome.')
    print('Please choose one of the following measuring systems to convert from:\n(a) Metric System\n'
          '(b) Standard System(US)\n(c) Imperial System(UK)')

    answer1 = input()

    if answer1 == 'a':
        waiting = True

        while waiting:
            print('Please choose one of the following measuring systems to convert to:\n(a) Standard System(US)\n'
                  '(b) Imperial System(UK)')
            answer2a = input()

            if answer2a == 'a':
                print('Enter the volume of fluid in mL:')
                fluid_amt = float(input())
                conversions.metric_to_std(fluid_amt)
                waiting = False

            elif answer2a == 'b':
                print('Enter the volume of fluid in mL:')
                fluid_amt = float(input())
                conversions.metric_to_imp(fluid_amt)
                waiting = False
            else:
                print('Invalid entry')

    elif answer1 == 'b':
        print('Please choose one of the following measuring systems to convert to:\n(a) Metric System\n'
              '(b) Imperial System(UK)')
        answer2b = input()

        if answer2b == 'a':
            print('Enter the volume of fluid in oz:')
            fluid_amt = float(input())
            conversions.std_to_metric(fluid_amt)

        elif answer2b == 'b':
            print('Enter the volume of fluid in oz:')
            fluid_amt = float(input())
            conversions.std_to_imp(fluid_amt)

        else:
            print('No match')

    elif answer1 == 'c':
        print('Please choose one of the following measuring systems to convert to:\n(a) Metric System\n'
              '(b) Standard System(US)')
        answer2c = input()

        if answer2c == 'a':
            print('Enter the volume of fluid in oz:')
            fluid_amt = float(input())
            conversions.imp_to_metric(fluid_amt)

        elif answer2c == 'b':
            print('Enter the volume of fluid in oz:')
            fluid_amt = float(input())
            conversions.imp_to_std(fluid_amt)

        else:
            print('No match')
    else:
        print('No match')


main()

# Assume that you have created a mechanical robot that can perform the following tasks:
#
#     Stand up.
#     Sit down.
#     Turn left 90 degrees.
#     Turn right 90 degrees.
#     Take a step.
#
# Additionally, the robot can determine the answer to one test condition:
#
#     Am I touching something?
#
# a. Place two chairs 20 feet apart, directly facing each other. Draw a structured flowchart or write pseudocode describing
# the logic that would allow the robot to start from a sitting position in one chair, cross the room, and end up sitting
# in the other chair. Have a fellow student act as the robot and carry out your instructions.
#
# b. Draw a structured flowchart or write pseudocode describing the logic that would allow the robot to start from a sitting
# position in one chair, stand up and circle the chair, cross the room, circle the other chair, return to the first chair, and sit.
#
# Have a fellow student act as the robot and carry out your instructions.

# stand_up()
# while not is_touching_something():
#   step()
#
# turn_left() 90
# turn_left() 90
# sitDown()
