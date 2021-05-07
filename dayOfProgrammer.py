# of programmer is 256th day
def dayOfProgrammer(year) :
    if year == 1917:
        return "14.10.1917"
    # if not leap year
    elif not (year % 4 == 0) :
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'

if __name__ == "__main__":
    print(dayOfProgrammer(2017))