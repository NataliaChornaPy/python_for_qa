#1.Write a program to calculate expression:
a=32
b=37.2
c=-102.345
d=45
e=11
f=3
g=0.002
h=11
exp=(1+2*a)/3+(4*(b+c)*(5-d-e))/f-(7/g+h )**2
print exp

# 2.Print this ASCII graphic using 4 different string literal types:
print " _ _ _ _ _ _ "
print '--------------'
print'''\           /'''
print "|   ^___^   |"
print '/  (.)  (.) \\'
print "|   ( t  )  | Miaowww"
print"""\     ==/   /
|           |
'''''''''''''\n"""
#3 Print unique elements from any given list or tuple.
a=['hi','hello','hi','hello','1']
print set(a), type(a),"\n"


#4 Write a program to calculate the number of times that the string 'hi'
# appears anywhere in the given string and change 'hi' to 'bye'. Case should be ignored.
a="hi girls,hi boys"
print a.count('hi'),"times appears word 'hi'\n"

# 5.Unite three lists to one and print it in reverse order:
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
b=list1+list2+list3
print b[::-1],'\n'

# 6 Having tuple  ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
# -with production database connection properties (dialect, host, port, database name, user name, password), program should:
# -create  prod_config  dictionary, where dict keys are connection properties names and dict values are
# -appropriate values from the input tuple;
# -create  staging_config  dictionary with the same keys and values as  prod_config ;
# -in  staging_config  change host to 'semantic.amazonaws-staging.com' and password to 'root';
# -for  prod_config  and  staging_config  print connection strings in the following format  {dialect}://{user name}:{password}@{host}:{post}/{database name}
#


tupl = ('postgresql', 'semantic.amazonaws-prod.com', 5432, 'semantic', 'admin', '12345')
print tupl[1],"dd"
prod_config={'dialect':tupl[0],'host':tupl[1],'port':tupl[2],'database name':tupl[3],'user name':tupl[4],'password':tupl[5]}
staging_config=prod_config.copy()
staging_config['host']='semantic.amazonaws-staging.com'
staging_config['password']='root'

conn_prod="{}://{}:{}@{}:{}/{}".format(prod_config['dialect'],prod_config['user name'],prod_config['password'],prod_config['host'],prod_config['port'],prod_config['database name'])
print conn_prod

conn_prod="{}://{}:{}@{}:{}/{}".format(staging_config['dialect'],staging_config['user name'],staging_config['password'],staging_config['host'],staging_config['port'],staging_config['database name'])
print conn_prod
