def main():
    currtime = (int(token) for token in input().split(':'))
    currhour = next(currtime)
    currmin = next(currtime)
    currsec = next(currtime)

    exptime = (int(token) for token in input().split(':'))
    exphour = next(exptime)
    expmin = next(exptime)
    expsec = next(exptime)

    diffhour = exphour - currhour
    diffmin  = expmin - currmin
    diffsec = expsec - currsec

    secstr = str(diffsec % 60).zfill(2)

    minstr = diffmin % 60
    if (diffsec < 0): minstr = (minstr - 1) % 60
    minstr = str(minstr).zfill(2)

    hourstr = diffhour % 24
    if (diffmin < 0 or diffmin <= 0 and diffsec < 0):
        hourstr = (hourstr - 1) % 24
    hourstr = str(hourstr).zfill(2)

    if ("%s%s%s" % (hourstr, minstr, secstr) == "000000"):
        hourstr = "24"

    print("%s:%s:%s" % (hourstr, minstr, secstr))

if __name__ == "__main__":
    main()
