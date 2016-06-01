    # Print a number of sentences in a file alice_in_wonderland.txt (a sentence shall end in either a dot . or a tripple-dot ...)
import re
if __name__ == "__main__":
    pattern_abbr = re.compile('[0-9].|[A-Z][a-z][.]|[A-Z][.]') # To exclude abbreviation like U.S. or U. or 5.


    with open('alice_in_wonderland.txt','r') as f:

        file=f.read().replace('...','. ')
        # print file
        set1 = file
        set2 = file
        assert set1 == set2
        abbr=re.findall(pattern_abbr,file)
        print 'ABREVIATION to exclude',abbr
    # To exclude sentences like 1.A.1., U.S.
        if abbr:
            for not_sent in abbr:
                file_without_abbr=file.replace(not_sent,not_sent.replace('.',''))
                file=file_without_abbr
            # print file_without_abbr

        else:
            pass
        dots=file_without_abbr.count ('. ')
        paragraph=file_without_abbr.count('.\n')
        count_sentences=dots+paragraph
        print 'COUNT of Sentences is',count_sentences



