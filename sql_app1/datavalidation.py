from fastapi import FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel
import re
app=FastAPI()

class course(BaseModel):


    def __init__(self, cid, department, cname, credit):
        self.cid= cid
        self.department= department
        self.cname= cname
        self.credit= credit


    def check_cid(db: Session,self):
        cid_regix= "^[0-9]{5}$"
        if self.cid in cid_regix:
            return{"massage":"cid is valid"}
        else:
            return{"massage":"cid is not valid"}


    def check_department(db: Session,self):
        valid_department=["فنی و مهندسی","اقتصاد","علوم پایه","علوم انسانی","دامپزشکی","کشاورزی و منابع طبیعی"]
        if self.department in valid_department:
            return{"massage":"department is valid"}
        else:
            return{"massage":"department is not valid.please select one of the authorized colleges"}

    def check_cname(db: Session,self):
        if (self.cname) > 25 or (self.cname) not in ("^[آ-ی]+$"):
            return{"massage":"cname mustnt be more than 25 characters and out of persian"}
        else:
            return{"massage":"cname is valid"}

    def check_credit(db: Session,self):
        if self.credit > 4 or self.credit < 1 :
            return{"massage":"credit must be 1 to 4"}
        else:
            return{"massage":"credit is valid"}


class student(BaseModel):


    def __init__(self, stid, fname, lname, father, birth, ids, borncity, address, postalcode, cphone, hphone, department, major, married, id, cid, lids):
        self.stid= stid
        self.fname= fname
        self.lname= lname
        self.father= father
        self.birth= birth
        self.ids= ids
        self.borncity= borncity
        self.address= address
        self.postalcode= postalcode
        self.cphone= cphone
        self.hphone= hphone
        self.department= department
        self.major= major
        self.married= married
        self.id= id
        self.cid= cid
        self.lids= lids


    def check_stid(db: Session,self):
        year= int(self.stid // 100000000)
        middle= int((self.stid // 100)%1000000)
        index= int(self.stid % 100)
        if year < 300 or year > 404:
            return{"massage":"stid,year isnt valid"}
        if middle  != 114150:
            return{"massage":"stid.middle isnt valid"}
        if index < 1 or index > 99:
            return{"massage":"stid is not valid"}
            

    def check_fname(db: Session,self):
            if len(self.fname) > 10:
                return{"massage":"fname mustnt be more than 10 characters"}
            if not re.match("^[آ-ی]+$", self.fname):
                return{"massage":"fname must be persian"}
            else:
                return{"massage":"fname is valid"}
        

    def check_lname(db: Session,self):
            if len(self.lname) > 10:
                return{"massage":"lname mustnt be more than 10 characters"}
            if not re.match("^[آ-ی]+$", self.lname):
                return{"massage":"lname must be persian"}
            else:
                return{"massage":"lname is valid"}
        

    def check_father(db: Session,self):
            if len(self.father) > 10:
                return{"massage":"father mustnt be more than 10 characters"}
            if not re.match("^[آ-ی]+$", self.father):
                return{"massage":"father must be persian"}
            else:
                return{"massage":"father is valid"}
            

    def check_birth(db: Session,self):
        if not re.match("^([0-9]{2})/([0-9]{2})/([0-9]{4})$", self.birth):
            return{"massage":"self. must be in form day/month/year"}
        day, month, year = map(int, self.birth.split('/'))
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1300 or year > 1500:
            return{"massage":"birth isnt valid"}
        else:
            return{"massage":"birth is valid"}
        

    def check_ids(db: Session,self):
        if not re.match("^[0-9]{3}[آ-ی][0-9]{2}$", self.ids):
            return{"massage":"ids must has 3 numbers, one persian character, 2 numbers"}
        else:
            return{"massage":"ids is valid"}
        
    
    def check_borncity(db: Session,self):
        valid_cities=["اصفهان","اراک","تبریز","اردبیل","اهواز","ایلام","بجنورد","تهران","بندعباس","بوشهر","بیرجند","ارومیه","خرم اباد","زنچان","سمنان","رشت","زاهدان","ساری","سنندج","شهرکرد","شیراز","قزوین","قم","کرج","کرمانشاه","کرمان","گرگان","مشهد","یاسوج","همدان","یزد"]
        if self.borncity in valid_cities:
            return{"massage":"city is valid"}
        else:
            return{"massage":"city is not valid"}
            

    def check_adress(db: Session,self):
        if len(self.adress)<=100:
            return{"massage":"the maximum length of the address must be 100 characters"}
        else:
            return{"massage":"adress is valid"}


    def check_postalcode(db: Session,self):
        if len(self.postalcode)==10 and self.postalcode.isdigit():
            return{"massage":"postalcode is valid"}
        else:
            return{"massage":"postalcode is not valid.postalcode must be exactly 10 numbers"}
        

    def check_cphone(db: Session,self):
        if len(self.cphone)==11 and self.cphone.startswith("09") and self.cphone[2:].isdigit():
            return{"massage":"phonenumber is valid"}
        else:
            return{"massage":"phonenumber is not valid.phonenumber must starts with '09' and must be exactly 11 numbers"}
        

    def check_hphone(db: Session,self):
        valid_area_codes=["041","044","045","026","031","084","077","021","038","056","051","058","061","024","023","054","071","028","025","087","034","083","074","017","013","066","011","086","076","081","035"]
        if len(self.hphone)==11 and self.hphone[3:] in valid_area_codes and self.hphone[3:].isdigit():
            return{"massage":"phonenumber is valid"}
        else:
            return{"massage":"phonenumber is not valid.phonenumber must starts with right area codes and must be exactly 11 numbers"}
        

    def check_department(db: Session,self):
        valid_department=["فنی و مهندسی","اقتصاد","علوم پایه","علوم انسانی","دامپزشکی","کشاورزی و منابع طبیعی"]
        if self.department in valid_department:
            return{"massage":"department is valid"}
        else:
            return{"massage":"department is not valid.please select one of the authorized colleges"}    


    def check_major(db: Session,self):
        valid_majors=["مهندسی کامپیوتر","مهندسی انرژی ","مهندسی پلیمر ","مهندسی برق","مهندسی پزشکی","مهندسی صنایع","مهندسی عمران","مهندسی معدن","مهندسی معماری","مهندسی متالوژی","مهندسی نفت","مهندسی هوا فضا","مهندسی شیمی"]
        if self.major in valid_majors:
            return{"massage":"major is valid"}
        else:
            return{"massage":"major is not valid.please select one of the authorized major"}
    

    def check_married(db: Session, self):
        valid_married=["مجرد","متاهل"]
        if self.married in valid_married:
            return{"massage":"marriage status is valid"}
        else:
            return{"massage":"marriage status is not valid"}
        





    def check_cid(db: Session,self):
        cid_regix= "^[0-9]{5}$"
        if self.cid in cid_regix:
            return{"massage":"cid is valid"}
        else:
            return{"massage":"cid is not valid"}
        

    def check_lids(db: Session,self):
        if len(self.lids)==6 and self.lids.isdigit():
            return{"massage":"lids is valid"}
        else:
            return{"massage":"lids is not valid.it must be 6 numbers"}

        

    
class lecturer(BaseModel):


    def __init__(self, lids, fname, lname, id, department, major, birth, borncity, address, postalcode, cphone, hphone, cid):
        self.lids= lids
        self.fname= fname
        self.lname= lname
        self.id= id
        self.department= department
        self.birth= birth
        self.borncity= borncity
        self.address= address
        self.postalcode= postalcode
        self.cphone= cphone
        self.hphone= hphone
        self.major= major
        self.cid= cid
        

    def check_lids(db: Session,self):
        if len(self.lids)==6 and self.lids.isdigit():
            return{"massage":"lids is valid"}
        else:
            return{"massage":"lids is not valid.it must be 6 numbers"}
        


    def check_fname(db: Session,self):
        if len(self.fname) > 10:
            return{"massage":"fname mustnt be more than 10 characters"}
        if not re.match("^[آ-ی]+$", self.fname):
            return{"massage":"fname must be persian"}
        else:
            return{"massage":"fname is valid"}
        

    def check_lname(db: Session,self):
        if len(self.lname) > 10:
            return{"massage":"lname mustnt be more than 10 characters"}
        if not re.match("^[آ-ی]+$", self.lname):
            return{"massage":"lname must be persian"}
        else:
            return{"massage":"lname is valid"}






    def check_department(db: Session,self):
        valid_department=["فنی و مهندسی","اقتصاد","علوم پایه","علوم انسانی","دامپزشکی","کشاورزی و منابع طبیعی"]
        if self.department in valid_department:
            return{"massage":"department is valid"}
        else:
            return{"massage":"department is not valid.please select one of the authorized colleges"}    



    def check_major(db: Session,self):
        valid_majors=["مهندسی کامپیوتر","مهندسی انرژی ","مهندسی پلیمر ","مهندسی برق","مهندسی پزشکی","مهندسی صنایع","مهندسی عمران","مهندسی معدن","مهندسی معماری","مهندسی متالوژی","مهندسی نفت","مهندسی هوا فضا","مهندسی شیمی"]
        if self.major in valid_majors:
            return{"massage":"major is valid"}
        else:
            return{"massage":"major is not valid.please select one of the authorized major"}
    


    def check_birth(db: Session,self):
        if not re.match("^([0-9]{2})/([0-9]{2})/([0-9]{4})$", self.birth):
            return{"massage":"self. must be in form day/month/year"}
        day, month, year = map(int, self.birth.split('/'))
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1300 or year > 1500:
            return{"massage":"birth isnt valid"}
        else:
            return{"massage":"birth is valid"}
        


    def check_borncity(db: Session,self):
        valid_cities=["اصفهان","اراک","تبریز","اردبیل","اهواز","ایلام","بجنورد","تهران","بندعباس","بوشهر","بیرجند","ارومیه","خرم اباد","زنچان","سمنان","رشت","زاهدان","ساری","سنندج","شهرکرد","شیراز","قزوین","قم","کرج","کرمانشاه","کرمان","گرگان","مشهد","یاسوج","همدان","یزد"]
        if self.borncity in valid_cities:
            return{"massage":"city is valid"}
        else:
            return{"massage":"city is not valid"}
        

    def check_adress(db: Session,self):
        if len(self.adress)<=100:
            return{"massage":"the maximum length of the address must be 100 characters"}
        else:
            return{"massage":"adress is valid"}


    def check_postalcode(db: Session,self):
        if len(self.postalcode)==10 and self.postalcode.isdigit():
            return{"massage":"postalcode is valid"}
        else:
            return{"massage":"postalcode is not valid.postalcode must be exactly 10 numbers"}
        

    def check_cphone(db: Session,self):
        if len(self.cphone)==11 and self.cphone.startswith("09") and self.cphone[2:].isdigit():
            return{"massage":"phonenumber is valid"}
        else:
            return{"massage":"phonenumber is not valid.phonenumber must starts with '09' and must be exactly 11 numbers"}
        

    def check_hphone(db: Session,self):
        valid_area_codes=["041","044","045","026","031","084","077","021","038","056","051","058","061","024","023","054","071","028","025","087","034","083","074","017","013","066","011","086","076","081","035"]
        if len(self.hphone)==11 and self.hphone[3:] in valid_area_codes and self.hphone[3:].isdigit():
            return{"massage":"phonenumber is valid"}
        else:
            return{"massage":"phonenumber is not valid.phonenumber must starts with right area codes and must be exactly 11 numbers"}
        


    def check_cid(db: Session,self):
        cid_regix= "^[0-9]{5}$"
        if self.cid in cid_regix:
            return{"massage":"cid is valid"}
        else:
            return{"massage":"cid is not valid"}