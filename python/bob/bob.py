#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
    what = what.strip()

    if what == "":
        return 'Fine. Be that way!'
    elif what.isupper():
        return 'Whoa, chill out!'
    #split sentence into words and get last char of last word 
    elif what.endswith("?"):
        return 'Sure.'

    return 'Whatever.'

