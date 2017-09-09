#******************************************************************************
# Copyright of this product 2013-2023,
# InfiniFlux Corporation(or Inc.) or its subsidiaries.
# All Rights reserved.
#******************************************************************************

# $Id:$

import re
import json
from machbaseAPI import machbase

def append():
#init,columns start
    db = machbase()
    if db.open('127.0.0.1','SYS','MANAGER',5656) is 0 :
        return db.result()

    db.execute('drop table sample_table')
    db.result()
    if db.execute('create table sample_table(d1 short, d2 integer, d3 long, f1 float, f2 double, name varchar(20), text text, bin binary, v4 ipv4, v6 ipv6, dt datetime)') is 0:
        return db.result()
    db.result()

    tableName = 'sample_table'
    db.columns(tableName)
    result = db.result()

    if db.close() is 0 :
        return db.result()
#init, colums end

#append start
    db2 = machbase()
    if db2.open('127.0.0.1','SYS','MANAGER',5656) is 0 :
        return db2.result()

    types = []
    for item in re.findall('{[^}]+}',result):
        types.append(json.loads(item).get('type'))

    values = []
    with open('data.txt','r') as f:
        for line in f.readlines():
            v = []
            i = 0
            for l in line[:-1].split(','):
                t = int(types[i])
                if t == 4 or t == 8 or t == 12 or t == 104 or t == 108 or t == 112:
                    #short   integer    long       ushort      uinteger     ulong
                    v.append(int(l))
                elif t == 16 or t == 20:
                    #float      double
                    v.append(float(l))
                else:
                    v.append(l)
                i+=1
            values.append(v)

    db2.append(tableName, types, values, 'YYYY-MM-DD HH24:MI:SS')
    result = db2.result()

    if db2.close() is 0 :
        return db2.result()
#append end

    return result

if __name__=="__main__":
    print append()
