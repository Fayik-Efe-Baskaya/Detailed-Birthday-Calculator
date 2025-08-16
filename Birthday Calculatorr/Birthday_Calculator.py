



def birthday():
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n"
          "Welcome to the birthday calculator! Enter the birthday information and see that:"
          " The age and how much time is left until the birthday based on the information you have entered.\n"
          "There is no case sensitivity.\n"
          "Everything has been included — from the options of After Christ (AC) and Before Christ (BC), "
          "to whether the month or day is known or not.\n"
          "┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")

    while(True):
        from datetime import date
        import calendar
        import time

        today = date.today()
        last_of_month_today = calendar.monthrange(today.year, today.month)[1]


        while (True):
            tcontinue = input("Press enter to continue\nPress x to exit the program ").lower()

            if (tcontinue == ""):
                break
            elif (tcontinue == "x"):
                return
            else:
                continue


        def info_and_nknown():
            while (True):
                try:
                    BAC = input("AFTER CHRIST(AC) or BEFORE CHRIST(BC)?: ").upper()
                    if (BAC not in ["AC", "AFTERCHRIST", "AFTER CHRIST", "BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                        print("AC OR BC!\n")
                        time.sleep(1)
                        continue

                    year = input("Please enter that what year were you born? (Enter x to restart): ").lower()
                    if (year == "x"):
                        time.sleep(1)
                        continue

                    if (BAC in ["BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                        if (int(year) < 0):
                            print("Please enter a valid year value!\n")
                            time.sleep(1)
                            continue
                    else:
                        if (int(year) > today.year or int(year) < 0):
                            print("Please enter a valid year value!\n")
                            time.sleep(1)
                            continue

                    mcontrol = input("Is the month information known? Yes(y) or no(n): (Enter x to restart): ").lower()
                    if (mcontrol == "x"):
                        time.sleep(1)
                        continue

                    if (mcontrol == "n" or mcontrol == "no"):
                        day = month = dcontrol = None

                        if (BAC in ["BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                            print(
                                f"\n----------------------------------\n{(today.year - int(year)) + int(year) * 2} years old\n\n")
                            return int(year), month, day, BAC, mcontrol, dcontrol

                        else:
                            if (today.year - int(year) <= 1):
                                print(f"\n----------------------------------\n{today.year - int(year)} year old\n\n")
                            else:
                                print(f"\n----------------------------------\n{today.year - int(year)} years old\n\n")
                            return int(year), month, day, BAC, mcontrol, dcontrol

                    elif (mcontrol == "y" or mcontrol == "yes"):
                        pass
                    else:
                        print("Yes or no!\n")
                        time.sleep(1)
                        continue

                    month = input("Please enter that in which month were you born? (Enter x to exit): ")
                    if (month == "x"):
                        time.sleep(1)
                        continue

                    if (int(month) <= 0 or int(month) > 12):
                        print("Please enter a valid month value!\n")
                        time.sleep(1)
                        continue

                    dcontrol = input("Is the day information known? Yes(y) or no(n) (enter x to restart): ").lower()
                    if (dcontrol == "x"):
                        time.sleep(1)
                        continue

                    if (dcontrol == "n" or dcontrol == "no"):
                        day = None

                        if (today.month == int(month)):
                            yage = (today.year - int(year))
                            mage = 0
                            if (BAC in ["BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                                print(
                                    f"\n----------------------------------\n{yage + int(year) * 2} years and {mage} months old\n\n")
                                return int(year), int(month), day, BAC, mcontrol, dcontrol

                            else:
                                if (yage <= 1):
                                    print(f"\n----------------------------------\n{yage} year and {mage} months old\n\n")
                                else:
                                    print(f"\n----------------------------------\n{yage} years and {mage} months old\n\n")
                                return int(year), int(month), day, BAC, mcontrol, dcontrol

                        elif (today.month < int(month)):
                            yage = today.year - int(year) - 1
                            mage = 12 - (int(month) - today.month)
                            if (BAC in ["BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                                if (mage <= 1):
                                    print(
                                        f"\n----------------------------------\n{yage + int(year) * 2} years and {mage} month old\n\n")
                                    return int(year), int(month), day, BAC, mcontrol, dcontrol

                                else:
                                    print(
                                        f"\n----------------------------------\n{yage + int(year) * 2} years and {mage} months old\n\n")
                                    return int(year), int(month), day, BAC, mcontrol, dcontrol

                            else:
                                if (yage <= 1 and mage <= 1):
                                    print(f"\n----------------------------------\n{yage} year and {mage} month old\n\n")
                                if (yage <= 1 and mage > 1):
                                    print(f"\n----------------------------------\n{yage} year and {mage} months old\n\n")
                                if (yage > 1 and mage <= 1):
                                    print(f"\n----------------------------------\n{yage} years and {mage} month old\n\n")
                                else:
                                    print(f"\n----------------------------------\n{yage} years and {mage} months old\n\n")
                                return int(year), int(month), day, BAC, mcontrol, dcontrol

                        else:
                            yage = today.year - int(year)
                            mage = today.month - int(month)
                            if (BAC in ["BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                                if (mage <= 1):
                                    print(
                                        f"\n----------------------------------\n{yage + int(year) * 2} years and {mage} month old\n\n")
                                else:
                                    print(
                                        f"\n----------------------------------\n{yage + int(year) * 2} years and {mage} months old\n\n")
                                return year, month, day, BAC, mcontrol, dcontrol

                            else:
                                if (yage <= 1 and mage <= 1):
                                    print(f"\n----------------------------------\n{yage} year and {mage} month old\n\n")
                                elif (yage <= 1 and mage > 1):
                                    print(f"\n----------------------------------\n{yage} year and {mage} months old\n\n")
                                elif (yage > 1 and mage <= 1):
                                    print(f"\n----------------------------------\n{yage} years and {mage} month old\n\n")
                                else:
                                    print(f"\n----------------------------------\n{yage} years and {mage} months old\n\n")
                                return int(year), int(month), day, BAC, mcontrol, dcontrol

                    elif (dcontrol == "y" or dcontrol == "yes"):
                        pass
                    else:
                        print("Yes or no!\n")
                        time.sleep(1)
                        continue

                    day = input("Please enter that what day of the month were you born? (Enter x to exit): ")
                    if (day == "x"):
                        time.sleep(1)
                        continue

                    global last_of_month_birthday
                    last_of_month_birthday = calendar.monthrange(int(year), int(month))[1]
                    first_of_month_birthday = date(year=int(year), month=int(month), day=1).day

                    if (int(day) <= 0 or int(day) > last_of_month_birthday):
                        print("Please enter a valid day value!\n")
                        time.sleep(1)
                        continue

                    return int(year), int(month), int(day), BAC, mcontrol, dcontrol

                except ValueError:
                    print("Please enter an integer value!!!\n")
                    time.sleep(1)
                    continue

        year, month, day, BAC, mcontrol, dcontrol = info_and_nknown()

        def calculating(year, month, day, BAC):
            if (dcontrol in ["no", "n"] or mcontrol in ["no", "n"]):
                return

            if (int(today.month) == month):
                if (today.day < day):
                    yage = (today.year - year) - 1
                    mage = 11
                    dage = today.day
                else:
                    yage = today.year - year
                    mage = 0
                    dage = today.day - day

            elif (today.month < month):
                if (today.day < day):
                    yage = today.year - year - 1
                    mage = 12 - (month - today.month - 1)
                    dage = (last_of_month_birthday - day) + today.day
                else:
                    yage = today.year - year - 1
                    mage = 12 - (month - today.month)
                    dage = today.day - day
            else:
                if (today.day < day):
                    yage = today.year - year
                    mage = today.month - month - 1
                    dage = (last_of_month_birthday - day) + today.day
                else:
                    yage = today.year - year
                    mage = today.month - month
                    dage = today.day - day

            if (month == today.month and day == today.day):
                if (BAC in ["BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                    print(
                        f"\n----------------------------------\nHappy birthday!!!!!\n\n{yage + year * 2} years {mage} month and {dage} day old\n\n")

                else:
                    if (year == today.year):
                        print(
                            f"\n----------------------------------\nWelcome to our world!!!\n\n{yage} years{mage} months and {dage} days old\n\n")
                    elif (mage <= 1 or dage <= 1):
                        print(f"\n----------------------------------\n\n{yage} years {mage} month and {dage} day old\n\n")
                    elif (mage > 1 or dage <= 1):
                        print(f"\n----------------------------------\n\n{yage} years {mage} months and {dage} day old\n\n")
                    elif (mage <= 1 or dage > 1):
                        print(f"\n----------------------------------\n\n{yage} years {mage} month and {dage} days old\n\n")
                    else:
                        print(f"\n----------------------------------\n\n{yage} years {mage} months and {dage} days old\n\n")


            elif (year == today.year and month == today.month and day == today.day):
                print(
                    f"\n----------------------------------\nWelcome to our world!!!\n\n{yage} years {mage} months and {dage} days old\n\n")


            else:
                if (BAC in ["BC", "BEFORECHRIST", "BEFORE CHRIST"]):
                    if (mage <= 1 or dage <= 1):
                        print(
                            f"\n----------------------------------\n\n{yage + year * 2} years {mage} month and {dage} day old\n\n")
                    elif (mage > 1 or dage <= 1):
                        print(
                            f"\n----------------------------------\n\n{yage + year * 2} years {mage} and months and {dage} day old\n\n")
                    elif (mage <= 1 or dage > 1):
                        print(
                            f"\n----------------------------------\n\n{yage + year * 2} years {mage} and month and { dage} days old\n\n")
                    else:
                        print(
                            f"\n----------------------------------\n\n{yage + year * 2} years {mage} and months and {dage} days old\n\n")


                else:
                    if (yage <= 1 and mage <= 1 and dage <= 1):
                        print(f"\n----------------------------------\n{yage} year {mage} month and {dage} day old\n\n")
                    elif (yage > 1 and mage > 1 and dage > 1):
                        print(f"\n----------------------------------\n{yage} years {mage} months and {dage} days old\n\n")
                    elif (yage > 1 and mage <= 1 and dage <= 1):
                        print(f"\n----------------------------------\n{yage} years {mage} month and {dage} day old\n\n")
                    elif (yage > 1 and mage > 1 and dage <= 1):
                        print(f"\n----------------------------------\n{yage} years {mage} months and {dage} day old\n\n")
                    elif (yage > 1 and mage <= 1 and dage > 1):
                        print(f"\n----------------------------------\n{yage} years {mage} month and {dage} days old\n\n")
                    elif (yage <= 1 and mage > 1 and dage <= 1):
                        print(f"\n----------------------------------\n{yage} year {mage} months and {dage}  day old\n\n")
                    elif (yage <= 1 and mage <= 1 and dage > 1):
                        print(f"\n----------------------------------\n{yage} year {mage} month and {dage} days old\n\n")
                    elif (yage <= 1 and mage > 1 and dage > 1):
                        print(f"\n----------------------------------\n{yage} year {mage} months and {dage} days old\n\n")
                    else:
                        print(f"\n----------------------------------\n{yage} year {mage} months and {dage} days old\n\n")

        calculating(year, month, day, BAC)

        def remaining_time(year, month, day, mcontrol, dcontrol):

            if (month is None):
                print("----------------------------------\n\n\n\nCannot be calculated\n\n")
                return

            elif (day is None):
                if (today.month == int(month)):
                    print("----------------------------------\n\n\n\nToday is the birth month!\n\n")

                elif (today.month < int(month)):
                    if (month - today.month <= 1):
                        print(f"----------------------------------\n\n\n\nTime is left until the birthday: {int(month) - today.month} month\n\n")
                    else:
                        print(f"----------------------------------\n\n\n\nTime is left until the birthday: {int(month) - today.month} months\n\n")

                else:
                    if (12 - (today.month - int(month)) <= 1):
                        print(
                            f"----------------------------------\n\n\n\nTime is left until the birthday: {12 - (today.month - int(month))} month\n\n")
                    else:
                        print(
                            f"----------------------------------\n\n\n\nTime is left until the birthday: {12 - (today.month - int(month))} months\n\n")
                return

            else:
                if (today.month == month):
                    if (today.day <= int(day)):
                        rmonth = 0
                        rday = int(day) - today.day
                    else:
                        rmonth = 11
                        rday = last_of_month_birthday - today.day + int(day)


                elif (today.month < int(month)):
                    if (today.day <= int(day)):
                        rmonth = int(month) - today.month
                        rday = int(day) - today.day
                    else:
                        rmonth = int(month) - today.month - 1
                        rday = (last_of_month_today - today.day) + int(day)


                else:
                    if (today.day <= int(day)):
                        rmonth = 12 - (today.month - int(month))
                        rday = int(day) - today.day
                    else:
                        rmonth = 11 - (today.month - int(month))
                        rday = (last_of_month_today - today.day) + int(day)

                if (rmonth > 1 and rday <= 1):
                    print(f"----------------------------------\n\n\n\nTime is left until the birthday: {rmonth} months {rday} and day\n\n")
                elif (rmonth <= 1 and rday > 1):
                    print(f"----------------------------------\n\n\n\nTime is left until the birthday: {rmonth} month {rday} and days\n\n")
                elif (rmonth <= 1 and rday <= 1):
                    print(f"----------------------------------\n\n\n\nTime is left until the birthday: {rmonth} month {rday} and day\n\n")
                else:
                    print(f"----------------------------------\n\n\n\nTime is left until the birthday: {rmonth} months {rday} and days\n\n")
                return

        remaining_time(year, month, day, mcontrol, dcontrol)



birthday()