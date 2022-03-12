from tool import Student
import pandas as pd
import schedule
import time

def do_hcs(name, birth, pw):
    student = Student(name, birth, pw)
    try:
        student.hcs()
        print(f'{student.name} 자가진단 완료')
    except:
        print(f'{student.name} 오류 발생')

def job():
    students = pd.read_csv('students.csv')
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
schedule.every().monday.at("08:00").do(job)
schedule.every().tuesday.at("08:00").do(job)
schedule.every().wednesday.at("08:00").do(job)
schedule.every().thursday.at("08:00").do(job)
schedule.every().friday.at("08:00").do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)