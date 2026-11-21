"""Calculate a tip and split a bill."""
def main():
    try:
        bill=float(input('Bill total (NPR): ')); rate=float(input('Tip percent: ')); people=int(input('People: '))
        if bill<=0 or rate<0 or people<1: raise ValueError
    except ValueError:
        print('Enter a positive bill, non-negative tip, and at least one person.'); return
    total=bill*(1+rate/100)
    print(f'Tip: NPR {bill*rate/100:.2f}\nTotal: NPR {total:.2f}\nPer person: NPR {total/people:.2f}')
if __name__=='__main__': main()
