# Basic Flow of Money Model

import sys

MODEL_NUMBER = 1
INPUT_STRING = """
                    MAIN MENU:

            Input amount to loan (integer).
            Input 'q' to quit program.
            """
EXIT_STRING = """
                Thank you, goodbye!

    By Ben Shields <https://github.com/iamrobinhood12345>
        copyright 2017
               """


def issue_money(val, money_circulating, debt_to_central_bank, contracts):
    """Issue money."""
    money_circulating[0] += val
    print("Issuing " + str(val) + " units")
    if val != 0:
        debt_to_add = val + 1
        debt_to_central_bank[0] += debt_to_add
        print("Adding " + str(debt_to_add) + " to total debt to central bank")
        contract = debt_to_add
        contracts.append(contract)
        print("Creating contract for " + str(contract) + " units")
    else:
        print("No contract created, no money issued.")


def remove_debt(money_circulating, debt_to_central_bank, contracts):
    """Remove debt."""
    for i in range(len(contracts)):
        if money_circulating[0] >= contracts[i]:
            print("Paying off debt of contract of " + str(contracts[i]) + " units")
            money_circulating[0] -= contracts[i]
            print("Removing " + str(contracts[i]) + " units from money circulating")
            debt_to_central_bank[0] -= contracts[i]
            print("Removing " + str(contracts[i]) + " units from debt to central bank")
            print("Removing contract of " + str(contracts[i]) + " units")
            del contracts[i]
            break


def main():
    """Handle menus and input."""
    money_circulating = [0]
    debt_to_central_bank = [0]
    contracts = []
    print("""
                    Economic Model """ + str(MODEL_NUMBER) + """
        Turn based flow of money model.
        Constituents:
            Central Bank
            Other (Entities that do not issue money)
        """)
    while True:
        loan = input(INPUT_STRING)
        try:
            loan_val = int(loan)
        except ValueError:
            if loan == 'q':
                print(EXIT_STRING)
                sys.exit()
            print("WARNING: Loan input must be an integer!")
            continue
        issue_money(loan_val, money_circulating, debt_to_central_bank, contracts)
        remove_debt(money_circulating, debt_to_central_bank, contracts)
        print("Money circulating: " + str(money_circulating[0]))
        print("Total debt to central bank: " + str(debt_to_central_bank[0]))
        print("Contracts: " + str(contracts))


if __name__ == "__main__":
    """Entry point. Calls main function."""
    main()
