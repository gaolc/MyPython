with open('foo.txt') as f:
    for line in f.readlines():
        line=line.replace('(','[').replace(')',']')
        with open('foo.csv','a') as l:
            print >> l, line
            
nohup ./sendmsg.py > python.log3 2>&1 &

import json
with open('foo.out') as f:
    for line in f.readline():
        data=json.load(line)
        print data[1]

  
  
with open('foo.out') as f:
    for line in f.readlines():
        print type(line)
        print line
        line=json.loads(line)
        print type(line)

d='{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}'
di=json.loads(d)



tuling = Tuling(api_key='b444e52bcc234ee39a345212af6ce080')

@bot.register()

def auto_reply(msg):

    tuling.do_reply(msg)
embed()

l+=s[0].upper()+(s[0].lower())*0+'-'

mysql> use PyDataBase
CREATE TABLE PyTable (username varchar (10),useradd varchar(10));
insert into PyTable (username) values ('员工1');
select * from PyTable;