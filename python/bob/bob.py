#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):


    if what.strip() == "":
        return 'Fine. Be that way!'
    elif what.isupper() == True:
        return 'Whoa, chill out!'
    #split sentence into words and get last char of last word 
    elif what.split()[-1][-1] == "?":
        return 'Sure.'

    return 'Whatever.'

