# -*- coding: utf8 -*-

#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    _map={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
    tmp=[]
    ans=[]
    for w in input_string:
        if w.isdigit():
            tmp.append(int(w))
    for i in tmp:
        ans.append(_map[i])
    return ' '.join(ans)



def to_camel_case(underscore_str):

    b=underscore_str.split('_')
    count=0
    ans=''
    if(len(b)==1):
        ans+=b[0]
    else:
        for w in b:
            if w:
                if count==0:
                    ans+=w.lower()
                    count+=1
                else:
                    ans+=w[0].upper()+w[1:].lower()
    return ans
