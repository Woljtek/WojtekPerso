import os
import sys

#constants
VIRT_SOFT = ['KVM', 'VBOX']

def askIntFromUser(question):
    """
    Ask user for an int
    :param question: Question to user
    :return:
    """
    while True:
        try:
            i_value = int(input(question))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    print("i_value: " + str(i_value))

def askStrFromUser(question):
    """
    Ask user for a string information
    :param question: Question to user
    :return:
    """
    while True:
        try:
            str_value = str(input(question))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    print("str_value: " + str(str_value))

def askVirtualSoftWareFromUser(question):
    """
    Ask user for KVM and VBOX
    :param question: Question to user
    :return:
    """
    while True:
        try:
            str_value = str(input(question)).upper()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if str_value in VIRT_SOFT:
            break
        else:
            print("Les seules valeurs acceptées sont VBOX et KVM, réessayez\n")
    print("VS_value: " + str(str_value))

def askPathFromUser(question):
    """
    Ask user for a path
    :param question: Question to user
    :return:
    """
    while True:
        try:
            path = str(input(question))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if os.path.exists(path):
            break
        else:
            print("Le chemin n'existe pas, réessayez\n")
    print("str_value: " + str(path))

askIntFromUser('Donne moi un integer ?')

askStrFromUser('Donne moi du texte ?')

askVirtualSoftWareFromUser('KVM ou VBOX')

askPathFromUser('Donne moi un chemin ?')

sys.exit(0)
