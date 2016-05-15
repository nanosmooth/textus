from flask import Flask, jsonify, request, session, redirect, url_for, \
     render_template, flash, Response


import calendar, time
from time import gmtime, strftime

globalmc=0
import sqlite3
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")



mainrt='<div style="float:right;padding:7px;margin:3px 8px 3px 0px;background-color:#BEE1FF;clear:both;max-width:290px;border-radius: 10px;border-bottom: 1px solid #61B6FF;word-wrap: break-word">'
mainlt='<div style="float:left;padding:7px;margin:3px 0px 3px 8px;background-color:#FEFEFE;clear:both;max-width:290px;border-radius: 10px;border-bottom: 1px solid #BEBEBE;word-wrap: break-word">'

subrt='<div style="color: #82C4FD;    font-size: small;    font-family: serif;">'
sublt='<div style="color: #BBBBBB;    font-size: small;    font-family: serif;">'

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'tihishastobeaC!0n%^$@<>;;;}}}:)'

def colorizeSublt(who):
  global sublt
  if who == 'tejus':
      subltt=sublt.replace('#BBBBBB','#337ab7')
  elif who == 'madhur':
      subltt=sublt.replace('#BBBBBB','#FF9800;')
  elif who == 'akaash':
      subltt=sublt.replace('#BBBBBB','#9C27B0')
  elif who == 'manjax':
      subltt=sublt.replace('#BBBBBB','#F44336')
  elif who == 'nikhil':
      subltt=sublt.replace('#BBBBBB','#E91E63')
  elif who == 'ajay':
      subltt=sublt.replace('#BBBBBB','#673AB7')
  elif who == 'abhijith':
      subltt=sublt.replace('#BBBBBB','#427fED')
  elif who == 'prajwal':
      subltt=sublt.replace('#BBBBBB','#00CA81')
  elif who == 'karthik':
      subltt=sublt.replace('#BBBBBB','#B90000')

  return subltt




def writeToLoggedIn( str ):
  htmlstr=str.replace('\n','<br />')


  utc_sec_since_epoch=calendar.timegm(time.gmtime())
  utc_sec_since_epoch=utc_sec_since_epoch+19800
  post_time=strftime("%I:%M %p %a %d-%b-%Y", gmtime(utc_sec_since_epoch))
  conn = sqlite3.connect(db_path)
  conn.execute("INSERT INTO MESSAGES (NAME,TEXT,ROU,POSTTIME) \
      VALUES (?,?,?,?)",(session['username'],htmlstr,','+session['username']+',',post_time));
  conn.commit()
  conn.close()

def emoApple(msgtxt):
    #url fix
    msgtxt=msgtxt.replace("p:&#x2F;&#x2F;", 'pcolonslashslash')
    msgtxt=msgtxt.replace("s:&#x2F;&#x2F;", 'scolonslashslash')
    #unsure
    msgtxt=msgtxt.replace(":&#x2F;", '<img src="http://unicode.org/reports/tr51/images/android/android_1f615.png" class="emoji">')
    msgtxt=msgtxt.replace(":&#x27;", '<img src="http://unicode.org/reports/tr51/images/android/android_1f615.png" class="emoji">')
    msgtxt=msgtxt.replace(":-&#x2F;", '<img src="http://unicode.org/reports/tr51/images/android/android_1f615.png" class="emoji">')
    msgtxt=msgtxt.replace(":-&#x27;", '<img src="http://unicode.org/reports/tr51/images/android/android_1f615.png" class="emoji">')
    #url fix
    msgtxt=msgtxt.replace('pcolonslashslash',"p:&#x2F;&#x2F;")
    msgtxt=msgtxt.replace('scolonslashslash',"s:&#x2F;&#x2F;")
    #smile
    msgtxt=msgtxt.replace(":)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60a.png" class="emoji">')
    msgtxt=msgtxt.replace(":-)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60a.png" class="emoji">')
    msgtxt=msgtxt.replace(":]", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60a.png" class="emoji">')
    msgtxt=msgtxt.replace("=)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60a.png" class="emoji">')
    #grin
    msgtxt=msgtxt.replace(":D", '<img src="http://unicode.org/reports/tr51/images/android/android_1f600.png" class="emoji">')
    msgtxt=msgtxt.replace(":-D", '<img src="http://unicode.org/reports/tr51/images/android/android_1f600.png" class="emoji">')
    msgtxt=msgtxt.replace("=D", '<img src="http://unicode.org/reports/tr51/images/android/android_1f600.png" class="emoji">')
    #tongue
    msgtxt=msgtxt.replace(":p", '<img src="http://unicode.org/reports/tr51/images/android/android_1f61b.png" class="emoji">')
    msgtxt=msgtxt.replace(":-p", '<img src="http://unicode.org/reports/tr51/images/android/android_1f61b.png" class="emoji">')
    msgtxt=msgtxt.replace(":P", '<img src="http://unicode.org/reports/tr51/images/android/android_1f61b.png" class="emoji">')
    msgtxt=msgtxt.replace(":-P", '<img src="http://unicode.org/reports/tr51/images/android/android_1f61b.png" class="emoji">')
    #kiss
    msgtxt=msgtxt.replace(":*", '<img src="http://unicode.org/reports/tr51/images/android/android_1f61a.png" class="emoji">')
    msgtxt=msgtxt.replace(":-*", '<img src="http://unicode.org/reports/tr51/images/android/android_1f61a.png" class="emoji">')
    #love
    msgtxt=msgtxt.replace("&lt;3", '<img src="http://unicode.org/reports/tr51/images/android/android_2764.png" class="emoji">')
    #wink
    msgtxt=msgtxt.replace(";)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f609.png" class="emoji">')
    msgtxt=msgtxt.replace(";D", '<img src="http://unicode.org/reports/tr51/images/android/android_1f609.png" class="emoji">')
    msgtxt=msgtxt.replace(";-)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f609.png" class="emoji">')
    msgtxt=msgtxt.replace(";-D", '<img src="http://unicode.org/reports/tr51/images/android/android_1f609.png" class="emoji">')
    #sunglass
    msgtxt=msgtxt.replace("B)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60e.png" class="emoji">')
    msgtxt=msgtxt.replace("B-)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60e.png" class="emoji">')
    msgtxt=msgtxt.replace("8)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60e.png" class="emoji">')
    msgtxt=msgtxt.replace("8-)", '<img src="http://unicode.org/reports/tr51/images/android/android_1f60e.png" class="emoji">')
    #gasp
    msgtxt=msgtxt.replace(":o", '<img src="http://unicode.org/reports/tr51/images/android/android_1f62e.png" class="emoji">')
    msgtxt=msgtxt.replace(":O", '<img src="http://unicode.org/reports/tr51/images/android/android_1f62e.png" class="emoji">')
    msgtxt=msgtxt.replace(":-o", '<img src="http://unicode.org/reports/tr51/images/android/android_1f62e.png" class="emoji">')
    msgtxt=msgtxt.replace(":-O", '<img src="http://unicode.org/reports/tr51/images/android/android_1f62e.png" class="emoji">')
    #sad
    msgtxt=msgtxt.replace(":(", '<img src="http://unicode.org/reports/tr51/images/android/android_2639.png" class="emoji">')
    msgtxt=msgtxt.replace(":-(", '<img src="http://unicode.org/reports/tr51/images/android/android_2639.png" class="emoji">')
    #cry
    msgtxt=msgtxt.replace(":'(", '<img src="http://unicode.org/reports/tr51/images/android/android_1f622.png" class="emoji">')
    #upsidedown
    msgtxt=msgtxt.replace("(:", '<img src="http://unicode.org/reports/tr51/images/android/android_1f643.png" class="emoji">')
    msgtxt=msgtxt.replace("(-:", '<img src="http://unicode.org/reports/tr51/images/android/android_1f643.png" class="emoji">')



    return msgtxt


@app.route('/')
def index():
 if not session.get('logged_in'):
  return redirect(url_for('login'))
 else:
  return redirect(url_for('welcome'))

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
 session['prev']=0
 if not session.get('logged_in'):
    return redirect(url_for('index'))
 else:
    conn = sqlite3.connect(db_path)
    msgarr=[]
    tot_rows=conn.execute('SELECT count(*) FROM messages').fetchone()[0]
    sql="SELECT * FROM MESSAGES WHERE ROU like '%%,%s,%%' or NAME='%s' LIMIT 50 OFFSET %d-50" % (session.get('username'),session.get('username'),tot_rows)
    cursor=conn.execute(sql);

    for row in cursor:
        if row[3] is None:
            post_time='Few days back'
        else:
            post_time=row[3]

        msgtxt = emoApple(row[1])

        if row[0] == session.get('username'):
            msg='%s%s%s</div>%s%s%s</div></div>' % (mainrt,subrt,row[0],msgtxt,subrt,post_time)
        else:
            subltt=colorizeSublt(row[0])
            msg='%s%s%s</div>%s%s%s</div></div>' % (mainlt,subltt,row[0],msgtxt,sublt,post_time)
        msgarr.append(msg)
    prev_read_chats = ''.join(msgarr)


    return render_template('welcome.html',title='adda',page_title='adda',username=session.get('username'),init_prev_chats=prev_read_chats)







@app.route('/_send')
def send():
    toPut = request.args.get('textfeed')
    print toPut
    writeToLoggedIn(toPut)
    utc_sec_since_epoch=calendar.timegm(time.gmtime())
    utc_sec_since_epoch=utc_sec_since_epoch+19800
    post_time=strftime("%I:%M %p %a %d-%b-%Y", gmtime(utc_sec_since_epoch))
    msgtxt = emoApple(toPut)
    toPut = '%s%s%s</div>%s%s%s</div></div>' % (mainrt,subrt,session.get('username'),msgtxt,subrt,post_time)
    return jsonify(result=toPut)

@app.route('/_receive')
def receive():

   msgarr=[]
   conn = sqlite3.connect(db_path)
   sql="SELECT * FROM MESSAGES WHERE ROU not like '%%%s%%' and NAME!='%s'" % (session.get('username'),session.get('username'))
   cursor=conn.execute(sql);
   for row in cursor:
       msgtxt = emoApple(row[1])
       subltt=colorizeSublt(row[0])
       msg='%s%s%s</div>%s%s%s</div></div>' % (mainlt,subltt,row[0],msgtxt,sublt,row[3])
       msgarr.append(msg)
       sql="UPDATE MESSAGES SET ROU=ROU||',%s,' where TEXT='%s' and NAME!='%s'" % (session.get('username'),row[1],session.get('username'))
       conn.execute(sql);
   conn.commit()
   conn.close()

   def eventStream():
       str1 = ''.join(msgarr)
       strlength = len(str1)
       if strlength > 0:
           yield "data: {}\n\n".format(str1)



   return Response(eventStream(), mimetype="text/event-stream")

@app.route('/_receive_poll')
def receive_poll():

   msgarr=[]
   conn = sqlite3.connect(db_path)
   sql="SELECT * FROM MESSAGES WHERE ROU not like '%%%s%%' and NAME!='%s'" % (session.get('username'),session.get('username'))
   cursor=conn.execute(sql);
   for row in cursor:
       msgtxt = emoApple(row[1])
       subltt=colorizeSublt(row[0])
       msg='%s%s%s</div>%s%s%s</div></div>' % (mainlt,subltt,row[0],msgtxt,sublt,row[3])
       msgarr.append(msg)
       sql="UPDATE MESSAGES SET ROU=ROU||',%s,' where TEXT='%s' and NAME!='%s'" % (session.get('username'),row[1],session.get('username'))
       conn.execute(sql);
   conn.commit()
   conn.close()
   print("i am in poll")

   str1 = ''.join(msgarr)
   print str1
   strlength = len(str1)

   print strlength
   if int(strlength) == 0:
       print('no new updates')
       return 'ok'
   else:
       return jsonify(result=str1)


@app.route('/_load_prev_msgs')
def load_prev_msgs():
    conn = sqlite3.connect(db_path)
    msgarr=[]
    tot_rows=conn.execute('SELECT count(*) FROM messages').fetchone()[0]
    session['prev']=50+session.get('prev')
    session['offset_val']=50+session.get('prev')
    if int(session.get('offset_val'))-50 > int(tot_rows):
        print 'it was greater'
        return '<div style="display:none;"></div>'
    sql="SELECT * FROM MESSAGES WHERE ROU not like ',%s,' or NAME='%s' LIMIT 50 OFFSET %d-%d" % (session.get('username'),session.get('username'),tot_rows,session.get('offset_val'))
    print session.get('offset_val')
    cursor=conn.execute(sql)
    prev_read_chats=None
    for row in cursor:
        if row[3] is None:
            post_time='Few days back'
        else:
            post_time=row[3]
        msgtxt = emoApple(row[1])
        if row[0] == session.get('username'):
            msg='%s%s%s</div>%s%s%s</div></div>' % (mainrt,subrt,row[0],msgtxt,subrt,post_time)
        else:
            subltt=colorizeSublt(row[0])
            msg='%s%s%s</div>%s%s%s</div></div>' % (mainlt,subltt,row[0],msgtxt,sublt,post_time)
        msgarr.append(msg)
    prev_read_chats = ''.join(msgarr)

    return prev_read_chats




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':


        print(request.form['inputUsername'])
        if request.form['inputUsername'] == 'tejus':

            app_pass = 'tejus'
        elif request.form['inputUsername'] == 'nikhil':

            app_pass = 'nikhil'
        elif request.form['inputUsername'] == 'manjax':

            app_pass = 'manjax'
        elif request.form['inputUsername'] == 'karthik':

            app_pass = 'karthik'
        elif request.form['inputUsername'] == 'akaash':

            app_pass = 'akaash'
        elif request.form['inputUsername'] == 'abhijith':

            app_pass = 'abhijith'
        elif request.form['inputUsername'] == 'prajwal':

            app_pass = 'prajwal'
        elif request.form['inputUsername'] == 'ajay':

            app_pass = 'ajay'
        elif request.form['inputUsername'] == 'madhur':

            app_pass = 'madhur'

        else:
            error = 'You have no access'
            return render_template('login.html',title='Login to adda',page_title='adda',error=error)

        if request.form['inputPassword'] != app_pass:
            error = 'Invalid password - or - I have changed it :p, will let you know later'
        else:

            session['logged_in'] = True
            session['username'] = request.form['inputUsername']

            return redirect(url_for('index'))
    return render_template('login.html',
                         title='Login to adda',
                                                 page_title='adda',error=error)

@app.route('/logout',methods=['GET', 'POST'])
def logout():
    print "logging out: "+session['username']

    session.pop('logged_in', None)
    session.pop('prev',None)

    flash('You were logged out')
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.run()
  #socketio.run(app)
