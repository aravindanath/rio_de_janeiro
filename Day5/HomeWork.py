"""
Exercise

Tax in US based on states:


"""



def calculateNetIncome(gross,state):
    """
    Calculate the net income after federal and state tax

    :param gross: gross income
    :param state: state name
    :return: net income
    """
    state_tax = {'CA': 10, 'NY':11, 'TX':13,'BO':12, 'NJ':6}

    # Calculate net income after federal tax

    net = gross-(gross*.10)

    # Calculate net income after state tax

    if state in state_tax:
        net = net-(gross*state_tax[state]/100)
        print("Your net income after all the heavy taxes is : " + str(net))
        return net
    else:
        print("State not in the list")
        return None

calculateNetIncome(100000,'TX')