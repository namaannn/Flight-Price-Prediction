from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import webio_view
from flask import Flask,send_from_directory
from pywebio import STATIC_PATH, start_server
import pandas as pd
import numpy as np
import pickle
import argparse
app=Flask(__name__)
model=pickle.load(open('model3.pkl','rb')) 
def predict():
    put_markdown("# Welcome. Let us predict the price for you")
    date_dep=input("Journey date",type=DATE)
    time=input("Time for departure",type=TIME)
    journey_day=int(pd.to_datetime(date_dep).day)
    journey_month=int(pd.to_datetime(date_dep).month)
    dept_hr=int(pd.to_datetime(time).hour)
    dept_min=int(pd.to_datetime(time).minute)
    arr=input("Arrival Date",type=DATE)
    time1=input("Arrival Time",type=TIME)
    arr_hr=int(pd.to_datetime(time1).hour)
    arr_min=int(pd.to_datetime(time1).minute)
    dur_hr=abs(arr_hr-dept_hr)
    dur_min=abs(arr_min-dept_hr)
    flight=select("Choose the airways",['Jet Airways','IndiGo','Air India','Multiple carriers','SpiceJet'
                                        ,'Vistara','Air Asia','GoAir','Multiple carriers Premium economy'
                                        ,'Jet Airways Business','Vistara Premium economy','Trujet'])
    if flight=='Jet Airways':
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
    elif flight=='IndiGo':
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
    elif flight=='Air India':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
    elif flight=='Multiple carriers':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
    elif flight=='SpiceJet':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0     
                   
    elif flight=='Vistara':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0    
                        
    elif flight=='GoAir':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
    elif flight=='Multiple carriers Premium economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            
    elif flight=='Jet Airways Business':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0       
    elif flight=='Vistara Premium economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
    else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
    sc=radio("Choose the source",['Delhi','Kolkata','Mumbai','Chennai'])
    if sc=='Delhi':
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0
        
    elif sc=='Kolkata':
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0
       
    elif sc=='Mumbai':
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0
        
    elif sc=='Chennai':
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1
        
    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0
 
    dis=radio("Choose the destination",['Cochin','Delhi','New Delhi','Hyderabad','Kolkata'])
    if dis=='Cochin':
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        
    elif dis=='Delhi':
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        
    elif dis=='New Delhi':
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0
        
    elif dis=='Hyderabad':
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0
        
    elif dis=='Kolkata':
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1
    
    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        
    stops=radio("Choose the number of stops",['Non stop','1 stop','2 stops','3 stops','4 stops'])
    if stops=='Non stop':
        st=4
    elif stops=='1 stop':
        st=0
    elif stops=='2 stops':
        st=1
    elif stops=='3 stops':
        st=2
    elif stops=='4 stops':
        st=3
    
    output=model.predict([[st,journey_day,journey_month,dept_hr,dept_min,arr_hr,arr_min,dur_hr,
            dur_min,Air_India,GoAir,IndiGo,Jet_Airways,Jet_Airways_Business,Multiple_carriers,
            Multiple_carriers_Premium_economy,SpiceJet,Trujet,Vistara,Vistara_Premium_economy,
            s_Chennai,s_Delhi,s_Kolkata,s_Mumbai,d_Cochin,d_Delhi,d_Hyderabad,d_Kolkata,d_New_Delhi]])
    ot=round(output[0],2)
    put_text("Your flight price is Rs. : {}".format(ot))
app.add_url_rule('/tool', 'webio_view',webio_view(predict),methods=['GET','POST','OPTIONS'])
if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument("-p", "--port",type=int,default=8080)
    args=arg.parse_args()
    start_server(predict, port=args.port)
        