import csv

if __name__ == "__main__":

    # f = open('newfile.csv', 'w')
    # writer2=csv.writer(f)
    # str=[]
    #
    # with open('Python for QA - bugs list - Sheet1.csv', 'r') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     for rows in reader:
    #         str=[]
    #         for row in rows:
    #             if row =='critical':
    #                 row=row.replace('critical','HIGH')
    #             elif row =='high':
    #                 row=row.replace('high','MEDIUM')
    #             elif row =='medium':
    #                 row=row.replace('medium','LOW')
    #
    #             str.append(row)
    #         writer2.writerow(str)


    #  example 2

    csvfile = open('newfile.csv', 'w')
    header=['#','Priority','Description','Environment','Owner','Created At']

    writer2 = csv.DictWriter(csvfile, fieldnames=header)
    str=[]
    writer2.writeheader()
    with open('Python for QA - bugs list - Sheet1.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Priority'] =='critical':
                row['Priority']='HIGH'
                print 'ffff',row
            elif row['Priority']=='high':
                row['Priority']='MEDIUM'
            elif row['Priority']=='medium':
                row['Priority']='LOW'
            else:
                if row['Priority']=='low':
                    continue
            writer2.writerow(row)
