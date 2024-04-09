#!/usr/bin/python3 

if __name__ == "__main__":
    import sys
    arg_sum = 0
    count = len(sys.argv) - 1
  
    if count  == 0 :
        print(count)
    else:
        for i in range(count):
            arg_sum += int(sys.argv[i+1])
        print(arg_sum)


    