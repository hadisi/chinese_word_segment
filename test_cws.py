from cws import CWS

if __name__== "__main__":
    sent = '武大博士吴亦凡跪地施救老人'
    word_list = CWS.seg_sent(sent)
    print (' '.join(word_list))
