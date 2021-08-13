# This is a sample Python script.
# Please install all requirement packages before running a program.

from loan_request_form import loan_form_generator

if __name__ == '__main__':
    loan_form_generator.create(data={
        "type": "การศึกษาของตนเอง", "date": "13", "month": "สิงหาคม", "year": "2564",
        "fullname": "นางสาวศรีตรัง สงขลานครินทร์",
        "position": "นักวิชาการคอมพิวเตอร์", "org": "สำนักนวัตกรรมดิจิทัลฯ", "campus": "วิทยาเขตหาดใหญ่",
        "salary_id": "123456", "salary": "25000", "net_salary": "5000",
        "internel_tel": "2110", "mobile": "0812345678",
        "loan_amount": "10000", "loan_amount_desc": "หนึ่งหมื่นบาทถ้วน",
        # "isGovStaff": "", "isRecStaff": "", "isUniStaff": "/", "isIncStaff": "",
    })