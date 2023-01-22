def comp(r, i):
    if r.isdigit() and i.isdigit():
        n = complex(int(r), int(i))
        return n
    else:
        return 'Err, try again '
