import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
from flask import Flask, request, session, render_template, redirect, url_for
from flask import Flask, render_template, Response
from camera import Camera
import sqlite3
import run_motor



app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def root():
    return redirect(url_for('main'))

@app.route('/video_feed')
def video_feed():
    if session['logFlag']:
        return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return "LOGIN!"

@app.route('/main')
def main():
    return render_template('main.html')


@app.route("/forward")
def forward():
    run_motor.forward()
    return render_template('main.html')


@app.route("/backward")
def backward():
    run_motor.backward()
    return render_template('main.html')
    
@app.route("/right")
def right():
    run_motor.right()
    return render_template('main.html')

@app.route("/left")
def left():
    run_motor.left()
    return render_template('main.html')
    
@app.route("/stop")
def stop():
    run_motor.stop()
    return render_template('main.html')
    

@app.route('/login_form')
def login_form():
    return render_template('login/login_form.html')

@app.route('/login_proc', methods=['POST'])
def login_proc():
    if request.method == 'POST':
        userId = request.form['id']
        userPwd = request.form['pwd']
        if len(userId) == 0 or len(userPwd) == 0:
            return 'userId, userPwd not found!!'
        else:
            conn = sqlite3.connect('python.db')
            cursor = conn.cursor()
            #sql = 'select idx, userId, userPwd, userEmail from member where userId = ?'
            #cursor.execute(sql, (userId, ))
            #rows = cursor.fetchall()
            if userId == "msc9533" and userPwd == "1234":
                session['logFlag'] = True
                return redirect(url_for('main'))
            else:
                return redirect(url_for('login_form'))
            #for rs in rows:
            #    if userId == rs[1] and userPwd == rs[2]:
            #        session['logFlag'] = True
            #        session['idx'] = rs[0]
            #        session['userId'] = userId
            #        return redirect(url_for('main'))
            #    else:
            #        return redirect(url_for('login_form'))
    else:
        return 'WRONG!'

@app.route('/user_info_edit/<int:edit_idx>', methods=['GET'])
def getUser(edit_idx):
    if session.get('logFlag') != True:
        return redirect('login_form')
    conn = sqlite3.connect('python.db')
    cursor = conn.cursor()
    sql = 'select userEmail from member where idx = ?'
    cursor.execute(sql, (edit_idx,))
    row = cursor.fetchone()

    edit_email = row[0]

    cursor.close()

    conn.close()

    return render_template('users/user_info.html', edit_idx=edit_idx, edit_email=edit_email)



@app.route('/user_info_edit_proc', methods=['POST'])
def user_info_edit_proc():

    idx = request.form['idx']
    userPwd = request.form['userPwd']
    userEmail = request.form['userEmail']
    if len('idx') == 0:
        return 'Edit Data Not Found'

    else:
        conn = sqlite3.connect('python.db')
        cursor = conn.cursor()
        sql = 'update member set userPwd = ?, userEmail = ? where idx = ?'
        cursor.execute(sql, (userPwd, userEmail, idx))

        conn.commit()

        cursor.close()

        conn.close()

        return redirect(url_for('main'))



@app.route('/logout')
def logout():

    session.clear()

    return redirect(url_for('main'))



if __name__ == '__main__':
    app.secret_key = '967905'
    app.debug = True
    app.run(host='0.0.0.0', debug=True, threaded=True)
