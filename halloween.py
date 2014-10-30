for i in xrange(input()):
    num = input()
    
    half = (int)(num/2)
    if num%2 == 0:
        print half*half
    else:
        print half*(half+1)
