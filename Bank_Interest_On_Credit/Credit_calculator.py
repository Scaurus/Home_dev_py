__author__ = 'Zhuravskiy'
# coding: utf8
def maiin ():
    sum = input("Input Total Sum: ")
    month = input("Input month credit: ")
    interest = input("Input interest on credit: ")
    P = float (1)/12 / interest
    X = sum * (P + P/ ((1+P)**month -1))
    print "==== Result ===="
    print "Monthly Рayment:", round(X,2)
    overpayment = round(X,2) * 6 - sum
    print "Overpayment will be:",overpayment
if __name__ == "__main__":
    maiin()
