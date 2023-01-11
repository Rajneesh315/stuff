import mysql.connector as sql
import random
from getpass import getpass

a = input("Database User: ")
b = getpass("Enter Database password: ")

db = sql.connect(host='localhost', user=a,
                 passwd=b)
cur = db.cursor()

cur.execute("Show Databases")
dbs = []
for x in cur:
    dbs += x

if ('movi' not in dbs):
    print('\n ⚠️  The Database is missing. ⚠️ \n', '〰️'*15)
    print('Creating Database...')
    cur.execute("CREATE DATABASE movi")
    cur.execute("Show Databases")
    dbs = []
    for x in cur:
        dbs += x
    if 'movi' in dbs:
        print('Database created successfully!...')
    else:
        print("Unable to create Database...")

else:
    print('Database Found...')

cur.execute("use movi")
if db.is_connected():
    print('Connected to Database...')

else:
    print('Couldn\'t connect to database...')

cur.execute("Show tables")
tbs = []
for x in cur:
    tbs += x
if 'movie' not in tbs:
    print('\n ⚠️  A Table is missing. ⚠️ \n', '〰️'*13)
    print('Creating Table...')
    cur.execute('create table movie(naam varchar(15), phno bigint(11), tic int(2), fnam varchar(20), lnam varchar(20), pswd varchar(20), usrid varchar(10));')

    cur.execute("Show tables")
    tbs = []
    for x in cur:
        tbs += x
    if 'movie' not in tbs:
        print('unable to create table...')
    else:
        print('Table Created!')
else:
    print("table found...")

if 'frow' not in tbs:
    print('\n ⚠️  A Table is missing. ⚠️ \n', '〰️'*13)
    print('Creating Table...')
    cur.execute('create table frow(naam varchar(15), phno bigint(11), tic int(2), fnam varchar(20), lnam varchar(20), pswd varchar(20), usrid varchar(10));')

    cur.execute("Show tables")
    tbs = []
    for x in cur:
        tbs += x
    if 'frow' not in tbs:
        print('unable to create table...')
    else:
        print('Table Created!')
else:
    print("table found...")

if 'upcb' not in tbs:
    print('\n ⚠️  A Table is missing. ⚠️ \n', '〰️'*13)
    print('Creating Table...')
    cur.execute('create table upcb(naam varchar(15), phno bigint(11), tic int(2), fnam varchar(20), pswd varchar(20), usrid varchar(10));')

    cur.execute("Show tables")
    tbs = []
    for x in cur:
        tbs += x
    if 'upcb' not in tbs:
        print('unable to create table...')
    else:
        print('Table Created!')
else:
    print("table found...")


print('''
░█████╗░
██╔══██╗
███████║
██╔══██║
██║░░██║ditya Gautam
╚═╝░░╚═╝

██████╗░
██╔══██╗
██████╔╝
██╔══██╗
██║░░██║ajneesh Kumar
╚═╝░░╚═╝

██╗░░░██╗
╚██╗░██╔╝
░╚████╔╝░
░░╚██╔╝░░
░░░██║░░░ash Mishra
░░░╚═╝░░░'''
      )
print('\n'*100)
print('''
┏┓┏┓┏┳━━━┳┓╋╋┏━━━┳━━━┳━┓┏━┳━━━┓
┃┃┃┃┃┃┏━━┫┃╋╋┃┏━┓┃┏━┓┃┃┗┛┃┃┏━━┛
┃┃┃┃┃┃┗━━┫┃╋╋┃┃╋┗┫┃╋┃┃┏┓┏┓┃┗━━┓
┃┗┛┗┛┃┏━━┫┃╋┏┫┃╋┏┫┃╋┃┃┃┃┃┃┃┏━━┛
┗┓┏┓┏┫┗━━┫┗━┛┃┗━┛┃┗━┛┃┃┃┃┃┃┗━━┓
╋┗┛┗┛┗━━━┻━━━┻━━━┻━━━┻┛┗┛┗┻━━━┛
╋┏┓
┏┛┗┓
┗┓┏╋━━┓
╋┃┃┃┏┓┃
╋┃┗┫┗┛┃
╋┗━┻━━┛
┏━━━┳━━━┳┓╋╋┏┓
┃┏━┓┃┏━┓┃┗┓┏┛┃
┃┃╋┃┃┗━┛┣┓┗┛┏┛
┃┗━┛┃┏┓┏┛┗┓┏┛
┃┏━┓┃┃┃┗┓╋┃┃
┗┛╋┗┻┛┗━┛╋┗┛''')


def sup():
    naam = str(input("Enter the movie name :"))
    phno = int(input("Enter phone number :"))
    tic = input("Enter total tickets :")
    fnam = str(input("Enter your first name :"))
    lnam = str(input("Enter your last name :"))
    pswd = input("Enter your passwd :")
    idd = [0]
    usrid = 0
    cur.execute('select usrid from movie')
    for x in cur:
        idd += x
    iddd = 0
    while iddd in idd:
        iddd = random.randint(1000, 3000)
        usrid = iddd
    else:
        print("User ID is: ", usrid)

    v_ins = "insert into movie values( '{}','{}','{}','{}','{}','{}','{}')".format(
        naam, phno, tic, fnam, lnam, pswd, usrid)
    cur.execute(v_ins)
    db.commit()
    print("🌟️ General Ticket Booked 🌟️\n\n")
    mnu()


def frt():
    print("Front Row Booking")
    aa = input("Enter your movie name : ")
    bb = input("Enter your first name : ")
    ee = input("Enter your last name: ")
    cc = int(input("Enter total tickets : "))
    dd = int(input("Enter your ph_no : "))
    pswd = input("Enter the password : ")
    idd = [0]
    usrid = 0
    cur.execute('select usrid from frow')
    for x in cur:
        idd += x
    iddd = 0
    while iddd in idd:
        iddd = random.randint(1, 1000)
        usrid = iddd
    else:
        print("User ID is: ", usrid)

    v_ins = "insert into frow values( '{}','{}','{}','{}','{}','{}','{}')".format(
        aa, dd, cc, bb, ee, pswd, usrid)
    cur.execute(v_ins)
    db.commit()
    print("🎟️**TICKET BOOKED**🎟️\n\n")
    mnu()


def upcb():
    print("Upper Circle booking")
    a = input("Enter your name : ")
    b = input("Enter your movie name : ")
    c = int(input("Enter your ph_no : "))
    d = int(input("Enter total tickets : "))
    pswd = input("Enter the password : ")
    idd = [0]
    usrid = 0
    cur.execute('select usrid from upcb')
    for x in cur:
        idd += x
    iddd = 0
    while iddd in idd:
        iddd = random.randint(3000, 9999)
        usrid = iddd
    else:
        print("User ID is: ", usrid)
    v_ins = "insert into upcb values( '{}','{}','{}','{}','{}','{}')".format(
        b, c, d, a, pswd, usrid)
    cur.execute(v_ins)
    db.commit()
    print("🎦️ ENJOY THE MOVIE AND HAVE FUN 🎦️\n\n")
    mnu()


def delt():
    d = int(input('''What ticket is to be deleted:
    1. General ticket
    2. Front row ticket
    3. Upper circle ticket
    0. Abort
    [1/2/3] : '''))

    t = ''
    if d == 1:
        e = int(input("Enter the User ID: "))
        l = input("Enter Password : ")
        t = 'movie'
    elif d == 2:
        e = int(input("Enter the User ID: "))
        l = input("Enter Password : ")
        t = 'frow'
    elif d == 3:
        e = int(input("Enter the User ID: "))
        l = input("Enter Password : ")
        t = 'upcb'
    elif d == 0:
        mnu()
    else:
        print('Invalid Input\n')
        mnu()
    cur.execute(
        "delete from {t} where usrid=\'{e}\' and  pswd=\'{l}\'".format(t=t, e=e, l=l))
    db.commit()
    mnu()


def com():
    co = input('''
    ______________________________
            🚫️ WARNING 🚫️
    You may end up loosing data if
       wrong command is entered
                   *
    do not terminate your commands
    ______________________________
: ''')
    cur.execute(co)
    om = cur.fetchall()
    for x in om:
        print(x)
    print("\n\n\n")
    mnu()


def mnu():
    print('\n♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪')
    print("\n1. General Ticket")
    print("2. Front row ticket booking")
    print("3. Upper circle booking")
    print("4. see table")
    print("5. Cancel ticket")
    print("6. Enter command")
    print("7. Exit\n")

    ch = input("Enter your choice [1/2/3/4/5/6/7] :")
    if ch == '1':
        sup()
    elif ch == '2':
        frt()
    elif ch == '3':
        upcb()
    elif ch == '5':
        delt()
    elif ch == '6':
        com()
    elif ch == '7':
        print('''
▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█

█▀▀ █▀█ █▀█   █░█ █ █▀ █ ▀█▀ █ █▄░█ █▀▀ ░
█▀░ █▄█ █▀▄   ▀▄▀ █ ▄█ █ ░█░ █ █░▀█ █▄█ ▄''')
        quit()
    elif ch == '4':
        tbs = []
        cur.execute("Show tables")
        for x in cur:
            tbs += x
        print("What table you want to view ", tbs)
        a = input("Enter Table name : ")
        if a in tbs:
            cur.execute("select * from {}".format(a))
            select = cur.fetchall()
            for x in select:
                print('\n', x)
            print("\n")
        else:
            print('Wrong Input\n')
        mnu()
    else:
        print('Invalid Input.\nQuitting')
        quit()


mnu()
