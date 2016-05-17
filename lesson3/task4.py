import csv

if __name__ == "__main__":

    f = open('newfile.csv', 'w')
    writer2=csv.writer(f)
    w=[]

    with open('Python for QA - bugs list - Sheet1.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            w=[]
            for r in row:
                if r =='critical':
                    r=r.replace('critical','HIGH')
                elif r =='high':
                    r=r.replace('high','MEDIUM')
                elif r =='medium':
                    r=r.replace('medium','LOW')

                w.append(r)
            writer2.writerow(w)
            print w


