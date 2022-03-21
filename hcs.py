from tool import Student
import pandas as pd
import schedule
import time

error_list = list()

def do_hcs(name, birth, pw):
    student = Student(name, birth, pw)
    try:
        student.hcs()
        print(f'{student.name} 자가진단 완료')
    except:
        global error_list
        print(f'{student.name} 오류 발생')
        error_list.append({'name':name, 'birth':birth, 'pw':pw})

def job():
    students = pd.read_csv('students.csv', encoding='cp949')
    try:
        for i in students.loc:
            name = i['name']
            birth = str(i['birth'])
            if len(birth) != 6:
                birth = '0'*(6-len(birth))+birth
            pw = str(i['pw'])
            if len(pw) != 4:
                pw = '0'*(4-len(pw))+pw
            do_hcs(name, birth, pw)
    except:
        pass
    for person in error_list:
        do_hcs(person['name'], person['birth'], person['pw'])
    print(error_list)
    
schedule.every().monday.at("07:30").do(job)
schedule.every().tuesday.at("07:30").do(job)
schedule.every().wednesday.at("07:30").do(job)
schedule.every().thursday.at("07:30").do(job)
schedule.every().friday.at("07:30").do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(0.5)