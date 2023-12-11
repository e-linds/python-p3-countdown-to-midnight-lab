def countdown(item):
    while item > 0:
        print (f"{item} SECOND(S)!")
        item -= 1
    print("HAPPY NEW YEAR!")

    
def countdown_with_sleep(item):
    countdown(item)
    import time
    time.sleep(1)





