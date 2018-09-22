#
# Name:           Gabriel Barney
# Student ID:   
# Date:           9/21/18
#
# Lab:            0
# Section:        6 (Hatalsky(Waitlist))/ 16 (Humer(Enrolled))
# Purpose of Lab: To use basic python code to calculate a person's weight on Mars and Jupiter, as well as take inputs and display outputs. A refresher in basic python coding.
# Additional Cmts:I did this lab first in Hatalsky's 10 AM lab (which I am waitlisted for) , and did it in about 5 minutes because I am very familiar with basic python. This lab was also assigned in Humer's 6PM lab, and I had already done it.


def weight_on_planets():
    earth_weight = int(input("What do you weigh on earth? "))
    mars_weight = earth_weight * 0.38
    jupiter_weight = earth_weight * 2.34
    print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(mars_weight, jupiter_weight))
   
   
if __name__ == '__main__':
   weight_on_planets()
