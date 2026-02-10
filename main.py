from fastapi import FastAPI

ap = FastAPI()

listt = [1,2,3,4]
@ap.get("/")
def pp():
    r=[]
    for a in listt:
        r.append(a)
    return r
    

    


