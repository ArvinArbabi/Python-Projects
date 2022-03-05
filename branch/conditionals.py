#The parameter weekday is True if it is
#a weekday, and the parameter vacation
#is True if we are on vacation. We sleep 
#in if it is not a weekday or
#we're on vacation. Return True if 
#we sleep in.

def main():
    x, y = 100, 100
    
    if x < y:
        result = "x is less than y" 
    elif x == y:
        result = "x is the same as y"
    else:
        result = "x is greater than y"

    print(result)

    result = "x is less than y" if x < y else "x is greater or equal to y"
    print(result)

    value = "three"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3, 4)
        case _:
            result = -1
    
    print(result)


if __name__ == "__main__":
    main()



def sleep_in(weekday, vacation):
  if not weekday or vacation:
      return True
  else:
      return False

#return true
print(sleep_in(False,False))

#return false
print(sleep_in(True,False))

#return true
print(sleep_in(False,True))

#return true
print(sleep_in(True,True))

