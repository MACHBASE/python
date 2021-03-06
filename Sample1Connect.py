#******************************************************************************
# Copyright of this product 2013-2023,
# InfiniFlux Corporation(or Inc.) or its subsidiaries.
# All Rights reserved.
#******************************************************************************

# $Id:$

from machbaseAPI import machbase

def connect():
    db = machbase()
    if db.open('127.0.0.1','SYS','MANAGER',5656) is 0 :
        return db.result()

    if db.execute('select count(*) from m$tables') is 0 :
        return db.result()

    result = db.result()

    if db.close() is 0 :
        return db.result()

    return result

if __name__=="__main__":
    print connect()
