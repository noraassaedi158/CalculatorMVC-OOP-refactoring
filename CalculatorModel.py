class CalculatorModel:
    def __init__(self):
        self.stop = False

    def bracket(self, values):
        self.stop = False
        if values is None:
            self.stop = True
            self.conversion(values)
        else:
            br_finder = []
            answer = None

            # this is for validating the brackets
            for m in range(0, len(values)):
                if values[m] == "(":
                    br_finder.append(m)
                elif values[m] == ")":
                    if len(br_finder) == 0:
                        stop = True
                        return answer
                    else:
                        br_finder.pop()


            if len(br_finder) > 0:
                self.stop = True
                self.stopping(values)



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
                            answer = self.conversion(values_br)
                            answer = self.validation(answer)

                            if answer != None:
                                answer = self.normalization(answer)

                                if answer != None and len(answer) != 1:
                                    answer = self.bidmas(answer)

                        if self.stop == False:
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

    def conversion(self, values):
        if values is None:
            self.validation(values)
        else:
            for m in range(0, len(values)):
                try:
                    values[m] = float(values[m])
                except:
                    pass

        return values

    def validation(self, values):
        if values is None:
            self.normalization(values)
        else:
            validate = True
            if len(values) == 1:
                if isinstance(values[0], float):
                    return values
                else:
                    self.stop = True
                    self.stopping(values)
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
                            if values[m + 1] == 0 and values[m]== "÷":
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
                    self.stop = True
                    self.stopping(values)

    def normalization(self, values):
        if values is None:
            self.bidmas(values)
        else:
            m = 0
            if len(values) == 1:
                return values
            else:
                while m < len(values):
                    if m + 1 < len(values) and m >= 0:
                        if values[m] == "-" or values[m] == "+":
                            if m == 0 and isinstance(values[m + 1], float):
                                if values[m] == "+":
                                    values[m:m + 2] = [values[m + 1]]
                                    print (values)
                                    m += 1
                                    continue
                                if values[m] == "-":
                                    values[m:m + 2] = [-values[m + 1]]
                                    m += 1
                                    continue
                            elif m > 0 and not isinstance(values[m - 1], float) and isinstance(values[m + 1], float):
                                if values[m] == "+":
                                    values[m:m + 2] = [values[m + 1]]
                                    print(values)
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

    def bidmas(self, values):
        if values is None:
            self.stopping(values)
        elif len(values) == 1:
            self.stopping(values)
            return values
        else:
            while len(values) != 1:
                for m in range(0, len(values)):
                    if values[m] == 'x':
                        v = [float(values[m - 1]) * values[m + 1]]
                        values[m - 1:m + 2] = v
                        break
                    elif values[m] == '÷':

                        if values[m + 1] == 0:
                            self.stop = True
                            self.stopping(values)
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
            self.stopping(values)
            return values
    def stopping(self, values):
        if self.stop:
            return
        else:
            return values
