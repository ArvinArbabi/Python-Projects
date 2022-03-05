from calendar import TUESDAY
from unittest import result


def main():
    x = 0

    # while(x < 5):
    #     print(x)
    #     x = x + 1

    # for x in range(5, 10):
    #     print(x)

    # days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # for weekday in days:
    #     print(weekday)
    
    for x in range(5, 10):   
        # if (x==7):
        #     break
        if x % 2 == 0:
            continue 
        print(x)


    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    
    for i,d in enumerate(days):
        print(i + 1, d)

if (__name__ == "__main__"):
    main()

