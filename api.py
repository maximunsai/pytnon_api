from flask import Flask,url_for, redirect, render_template,request

app= Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return 'The person has failed and scored' + str(score)

# @app.route('/result/<int:marks>')
# def result(marks):
#     if marks<50:
#         return redirect(url_for('fail',score=marks))    
#     else:
#         return redirect(url_for('success',score=marks))

@app.route('/result/<int:marks>')
def result(marks):
    result =''
    if marks<50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=marks))        

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        history=float(request.form['history'])
        literature=float(request.form['literature'])
        total_score=(science+math+history+literature)/4
    #res=''       
    return redirect(url_for('success', score=total_score))    


if __name__=='__main__':
    app.run(debug=True)