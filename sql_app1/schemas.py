from pydantic import BaseModel



class course(BaseModel):
    cid : str
    cname : str
    department : str
    credit : int

class student(BaseModel):
    stid : str
    fname : str
    lname : str
    father : str
    birth : int
    ids : int
    borncity : str
    address : str
    postalcode : int
    cphone : int
    hphone : int
    department : str
    major : str
    married : bool
    id : int
    cid : int
    lids : int

class lecturer(BaseModel):
    lid : str
    fname : str
    lname : str
    id : int
    department : str
    major : str
    birth : int
    borncity : str
    address : str
    postalcode : int
    cphone : int
    hphone : int
    cid : int