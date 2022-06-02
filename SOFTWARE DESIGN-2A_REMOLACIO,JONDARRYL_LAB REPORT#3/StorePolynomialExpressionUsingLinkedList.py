class node:
    def __init__(self,co=None,exp=None):
     self.co=co
     self.exp=exp
     self.next=None

p1=None
p2=None
Sum=None

def create(head,co,exp):
    if head == None:
        temp=node(co,exp)
        head=temp
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        flag = node(co, exp)
        temp.next = flag
    return head

def display(poly):
    temp=poly
    while temp!=None:
        print(temp.co, '^',temp.exp,' + ',end='')
        temp = temp.next
    print()

loop=True
while loop:
    print('1.Enter Polynomial 1')
    print('2.Enter Polynomial 2')
    print('3.Print stored Polynomial Functions')
    print('4.Exit')

    ch = int(input())

    if ch == 1:
        co=int(input('Enter co-efficient\n'))
        exp=int(input('Enter exponent\n'))
        p1 = create(p1, co, exp)

    elif ch == 2:
        co=int(input('Enter co-efficient\n'))
        exp=int(input('Enter exponent\n'))
        p2=create(p2, co, exp)

    elif ch == 3:
        print('\nPolynomial1')
        display(p1)
        print('\nPolynomial2')
        display(p2)

    elif ch == 4:
        loop = False
    else:
        print('Wrong Choice!Re-enter')