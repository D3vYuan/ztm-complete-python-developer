def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return "Please enter number" 
    except ValueError as err:
        return err
    