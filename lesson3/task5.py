# 5.Write a script to automatically generate directories and files
# (empty 6 files with names task*.py where * is task number between 1 and 6) structure for python-for-qa course.
# Result should look the following way:
import os

def creating_files (main_path):
    main_path=main_path+'\Python_for_qa'
    if not os.path.exists(main_path):
        os.makedirs(main_path)
        python_for_qa=os.path.dirname(main_path)
        print python_for_qa
        print "Directory Python_for_qa is created"
    else:
        python_for_qa=main_path
        print python_for_qa

    fold=['lesson1','lesson2']

    for folders in fold:
        python_for_qa_lesson=main_path+"\{}".format(folders)
        if not os.path.exists(python_for_qa_lesson):
                 os.makedirs(python_for_qa_lesson)
                 os.path.dirname(python_for_qa_lesson)
                 print 'Folders',folders,'have been created'
        else:
            print 'Folders',folders,'exist'
        for i in range(1,7):
            with open(python_for_qa_lesson+"\\task_{}.py".format(i),"w") as f:
                f.close()
    print "Files have been created"


if __name__ == "__main__":
    creating_files("C:\Users\Natalia_Chorna\Desktop")