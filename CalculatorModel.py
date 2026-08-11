class CalculatorModel:

    def bracket(values):
        global stop
        stop = False
        br_finder = []
        answer = None

        # this is for validating the brackets
        for m in range(0, len(values)):
            if values[m] == "(":
                br_finder.append(m)
            elif values[m] == ")":
                if len(br_finder) == 0:
                    stop = True
                    return
                else:
                    br_finder.pop()

        if len(br_finder) > 0:
            stop = True
            return

        # and here is where it is solved
        for m in range(0, len(values)):
            before = None
            after = None

            for m in range(0, len(values)):
                if values[m] == "(":
                    br_finder.append(m)

                    if m - 1 >= 0:
                        try:
                            before = float(values[m - 1])
                        except:
                            before = None

                elif values[m] == ")":
                    if m + 1 < len(values):
                        try:
                            after = float(values[m + 1])
                        except:
                            after = None

                    br = br_finder.pop()
                    values_br = values[br + 1:m]

                    if len(values_br) == 0:
                        stop = True
                        return
                    else:
                        answer = conversion(values_br)
                        answer = validation(answer)

                        if answer != None:
                            answer = normalization(answer)

                            if answer != None and len(answer) != 1:
                                answer = bidmas(answer)

                    if stop == False:
                        if after != None and before != None:
                            answer = answer[0] * float(after) * float(before)
                            values[br - 1:m + 2] = [answer]

                        if after != None and before == None:
                            answer = answer[0] * float(after)
                            values[br:m + 2] = [answer]

                        elif before != None and after == None:
                            answer = answer[0] * float(before)
                            values[br - 1:m + 1] = [answer]

                        # replace even the brackets
                        elif before == None and after == None:
                            values[br:m + 1] = answer

                        break


    def conversion(values):
        for m in range(0, len(values)):
            try:
                values[m] = float(values[m])
            except:
                pass

        return values


    def validation(values):
        global stop
        validate = True

        if len(values) == 1:
            if isinstance(values[0], float):
                return values
            else:
                screen.clear()
                screen.setPlaceholderText((en()))
                stop = True
                return

        else:
            for m in range(0, len(values)):

                if values[m] == 'x' or values[m] == '÷':

                    if m == 0:
                        validate = False

                    elif 0 < m < len(values) - 1:
                        if (values[m + 1] == 'x' or
                            values[m + 1] == '÷' or
                            values[m - 1] == 'x' or
                            values[m - 1] == '÷'):
                            validate = False

                    elif m == len(values) - 1:
                        validate = False

                    if m < len(values) - 1:
                        if values[m + 1] == 0:
                            validate = False

                elif values[m] == '-' or values[m] == '+':

                    if m == 0:
                        if values[m + 1] == '-' or values[m + 1] == '+':
                            validate = False
                            break

                    elif 0 < m < len(values) - 1:

                        if (isinstance(values[m - 1], float) and
                            values[m + 1] == '-') or values[m + 1] == '+':
                            validate = True

                        if (isinstance(values[m + 1], float) and
                            values[m - 1] == '-') or values[m - 1] == '+':
                            validate = True

                        elif ((values[m - 1] == '-' or values[m - 1] == '+') and
                              (values[m + 1] == '-' or values[m + 1] == '+')):
                            validate = False
                            break

                        elif not isinstance(values[m + 1], float):
                            validate = False
                            break

                    elif m == len(values) - 1:
                        validate = False
                        break

                elif not (isinstance(values[m], float) or
                          values[m] in ('+', '-', 'x', '÷')):
                    validate = False
                    break

            if validate:
                return values
            else:
                stop = True
                return


    def normalization(values):
        m = 0

        if len(values) == 1:
            return values

        else:
            while m < len(values):

                if m + 1 < len(values) and m >= 0:

                    if values[m] == "-" or values[m] == "+":

                        if ((m == 0 and isinstance(values[m + 1], float)) or
                            m > 0 and
                            (not isinstance(values[m - 1], float) and
                             isinstance(values[m + 1], float))):

                            if values[m] == "+":
                                values[m:m + 2] = [values[m + 1]]
                                m += 1
                                continue

                            if values[m] == "-":
                                values[m:m + 2] = [-values[m + 1]]
                                m += 1
                                continue

                        else:
                            m += 1
                            continue

                    else:
                        m += 1
                        continue

                else:
                    m += 1
                    continue

        return values


    def bidmas(values):
        global stop

        while len(values) != 1:

            for m in range(0, len(values)):

                if values[m] == 'x':
                    v = [float(values[m - 1]) * values[m + 1]]
                    values[m - 1:m + 2] = v
                    break

                elif values[m] == '÷':

                    if values[m + 1] == 0:
                        screen.clear()
                        screen.setPlaceholderText((en()))
                        stop = True
                        return

                    else:
                        v = [values[m - 1] / values[m + 1]]
                        values[m - 1:m + 2] = v
                        break

            for m in range(0, len(values)):

                if values[m] == '+':
                    v = [values[m - 1] + values[m + 1]]
                    values[m - 1:m + 2] = v
                    break

                elif values[m] == '-':
                    v = [values[m - 1] - values[m + 1]]
                    values[m - 1:m + 2] = v
                    break

        return values
