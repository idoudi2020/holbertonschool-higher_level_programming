#!/usr/bin/python3
def multiple_returns(sentence):
    return(len(sentence), sentence[0] if sentence else None)

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))