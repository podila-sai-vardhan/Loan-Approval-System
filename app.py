from flask import Flask,jsonify,request,render_template       
from convert import Numerical  
import pickle

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check',methods=['GET','POST'])
def check():
    if request.method=='POST':
        name=request.form.get('name')
        gender=request.form.get('gender')
        married=request.form.get('married')
        dependents=request.form.get('dependents')
        education=request.form.get('education')
        self_employed=request.form.get('self-employed')
        applicant_income=request.form.get('applicant-income')
        coapplicant_income=request.form.get('coapplicant-income')
        loan_amount=request.form.get('loan-amount')
        loan_term=request.form.get('loan-term')
        credit_history=request.form.get('credit-history')
        property_area=request.form.get('property-area')
        print(name,gender,married,dependents,education,self_employed,
              applicant_income,coapplicant_income,loan_amount,loan_term,
              credit_history,property_area)
        nt=Numerical()
        genn=nt.converted('Gender',gender)
        marn=nt.converted('Married',married)
        depn=int(dependents)
        edn=nt.converted('Education',education)
        sfn=nt.converted('Self_employed',self_employed)
        if credit_history=='Yes':
            crn=1
        else:
            crn=0
        prarea =nt.converted('Property_Area',property_area)
        with open('model.pickle','rb') as model:
            mlmodel=pickle.load(model)
        pred=mlmodel.predict([[gender,married,dependents,education,self_employed,
              applicant_income,coapplicant_income,loan_amount,loan_term,
              credit_history,property_area]])
        if pred[0]==1:
            status='Loan Approved'
        else:
            status='Not Approved'

        print(nt,genn,marn,edn,sfn,crn,prarea)
        return jsonify({'message':'successfull'})
    else:
        return render_template('check.html')

if __name__=='__main__':
    app.run()

