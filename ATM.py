###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################

print('Welcome to Ali Askari bank ATM')

restart = ('Y')

chances = 3

balance = 999.12

###############################################################################################################################################

while chances >= 0:

    Pin = int (input('Please Enter you 4 Digit Pin: '))

    if Pin == (1234):

        print('You entered you pin Correctly')

        print('Please Press 1 For your Balance')

        print('Please Press 2 To Make a Withdrawl')

        print('Please Press 3 To Pay in')

        print('Please Press 4 To Return Card\n')

###############################################################################################################################################        

        while restart not in ('n', 'No', 'no', 'N'):

            print('You entered you pin Correctly')

            print('Please Press 1 For your Balance')

            print('Please Press 2 To Make a Withdrawl')

            print('Please Press 3 To Pay in')

            print('Please Press 4 To Return Card')

            option = int(input('What Would you like to choose? '))

###############################################################################################################################################           

            if option == 1 :

                print('Your Balance is $',balance)

                restart = input('Wwould You you like to go back?')

                if restart in ('n', 'No', 'no', 'N'):

                    print('Thank You')

                    break

###############################################################################################################################################              

                elif option == 2:

                    option2 = ('y')

                    Withdrawl = float(input('How Much Would you like to Withdrawl?,10,20,40,60,80,100 for other enter 1:'))

                if Withdrawl in [10,20,40,60,80,100]:

                   balance = balance - Withdrawl

                   print('\nYour Balance is now $',balance)

                   restart = input('Would You you like to go back?')

                   if restart in ('n','No','no','N'):

                      print('Thank You')

                      break

###############################################################################################################################################                 

                   elif Withdrawl != [10,20,40,60,80,100] :

                        print('Invalid Amount , Please Re-try\n')

                        restart = ('y')

                   elif Withdrawl == 1:

                        Withdrawl = float(input('Please Enter Desired amount:'))


                   elif option == 3:

                      Pay_in = float(input('How Much Would you like to Pay In?'))

                      balance = balance + Pay_in

                      print('\nYour Balance is now $',balance)

                      restart = input('Would You you like to go back?')

                if restart in ('n','No','no','N'):

                    print('Thank You')

                    break

###############################################################################################################################################                

            elif option == 4:

                print('Please wait whilst your card is Returned...\n')

                print('Thank you for you service ')

                break

###############################################################################################################################################            

            else:

                print('Please Enter a correct number. \n')

                restart = ('y')

            if pin!= ('1234'):

                print('Incorrect Password')

                chances = chances - 1

            elif chances == 0:

                print('\nNo more tries')

                break

            
###############################################################################################################################################
###############################################################################################################################################
###############################################################################################################################################

                

                        

                                            

                                                
