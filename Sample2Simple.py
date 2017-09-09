#******************************************************************************
# Copyright of this product 2013-2023,
# InfiniFlux Corporation(or Inc.) or its subsidiaries.
# All Rights reserved.
#******************************************************************************

# $Id:$

import re
import json
from machbaseAPI import machbase

def insert():
    db = machbase()
    if db.open('127.0.0.1','SYS','MANAGER',5656) is 0 :
        return db.result()

    db.execute('drop table sample_table')
    db.result()
    if db.execute('create table sample_table(d1 short, d2 integer, d3 long, f1 float, f2 double, name varchar(20), text text, bin binary, v4 ipv4, v6 ipv6, dt datetime)') is 0:
        return db.result()
    db.result()

    for i in range(1,10):
        sql = "INSERT INTO SAMPLE_TABLE VALUES ("
        sql += str((i - 5) * 6552) #short
        sql += ","+ str((i - 5) * 42949672) #integer
        sql += ","+ str((i - 5) * 92233720368547758L) #long
        sql += ","+ "1.234"+str((i-5)*7) #float
        sql += ","+ "1.234"+str((i-5)*61) #double
        sql += ",'id-"+str(i)+"'" #varchar
        sql += ",'name-"+str(i)+"'" #text
        sql += ",'aabbccddeeff'" #binary
        sql += ",'192.168.0."+str(i)+"'" #ipv4
        sql += ",'::192.168.0."+str(i)+"'" #ipv6
        sql += ",TO_DATE('2015-08-0"+str(i)+"','YYYY-MM-DD')" #date
        sql += ")";

        if db.execute(sql) is 0 :
            return db.result()
        else:
            print db.result()

        print str(i)+" record inserted."

    query = "SELECT d1, d2, d3, f1, f2, name, text, bin, to_hex(bin), v4, v6, to_char(dt,'YYYY-MM-DD') as dt from SAMPLE_TABLE";

    if db.execute(query) is 0 :
        return db.result()

    result = db.result()

    for item in re.findall('{[^}]+}',result):
        res = json.loads(item)
        print "d1 : "+res.get('d1')
        print "d2 : "+res.get('d2')
        print "d3 : "+res.get('d3')
        print "f1 : "+res.get('f1')
        print "f2 : "+res.get('f2')
        print "name : "+res.get('name')
        print "text : "+res.get('text')
        print "bin : "+res.get('bin')
        print "to_hex(bin) : "+res.get('to_hex(bin)')
        print "v4 : "+res.get('v4')
        print "v6 : "+res.get('v6')
        print "dt : "+res.get('dt')

    if db.close() is 0 :
        return db.result()

    return result

if __name__=="__main__":
    print insert()
