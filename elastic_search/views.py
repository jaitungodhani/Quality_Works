from django.shortcuts import render
from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
from elasticsearch import helpers
from decouple import config
from rest_framework import fields
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import json
import utils.response_handler as rh
import random
from auth_login.models import Reporting
from auth_login.serializers import Reportingserializer
import xmltodict
from urllib.request import urlopen
import requests
# Create your views here.

es = Elasticsearch(
    cloud_id=config("cloud_id"),
    http_auth=(config("user"), config("password"))
)

def generator(df2, index):
        try:
            for c, line in enumerate(df2):
                yield{
                    '_index':index,
                    '_doc_type':'test',
                    '_id': c,
                    '_source':line,
                }
        except Exception as e:
            print(e)

class elasticview(APIView):
    def post(self,request, format=None):
        file_obj=request.data.get('file')
        print(file_obj)
        es.indices.create(index='quality_works', ignore=400)
        print(es.ping())
        df = pd.read_json(file_obj)
        df["Keyword trends"] = df["Keyword trends"].replace(np.nan, 0)
        df2= df.to_dict('records')
        # generator(df2=df2, index="quality_works")
        try:
            helpers.bulk(es, generator(df2,index="quality_works"))
            print("working")
            return Response({"msg":"success"})
        except Exception as e:
            print(e)
            return Response({"msg":"failed"})
class xml_to_json(APIView):
    def post(self, request, format=None):
        file_obj=request.data.get('file')
        # var_url =requests.get("https://b2fbb4e9e7419c26abfc058fc121da71bd7a7e80d309da9d:98c1929fdd453184896ef516b0d411378fc1bd4636f955b8api.exotel.com/v1/Accounts/thinclab1/Calls/301e58c2727277ec420a36dd0f98159p")
        dictionary = xmltodict.parse(file_obj)
        json_object = json.dumps(dictionary) 
        return Response({'received data': dictionary})

class classelasticview(APIView):
    # parser_classes = [XMLParser]
    def post(self,request, format=None):
        # file_obj=request.data.get('file')
        # print(file_obj)
        es.indices.create(index='second', ignore=400)
        print(es.ping())
        # df = pd.read_json(file_obj)
        # df["Keyword trends"] = df["Keyword trends"].replace(np.nan, 0)
        df2= request.data.get('Call')
        print(df2)
        generator(df2=df2, index="second")
        try:
            res=helpers.bulk(es, generator(df2 , index="second"))
            print("working")
            return Response({"msg":"success"})
        except Exception as e:
            print(e)
            return Response({"msg":"failed"})    

class Allfilterview(APIView):
    def post(self,request,format=None):
        lOB_id=request.data.get('Lob_id')
        team_id=request.data.get('Team_id')
        agent_id=request.data.get('Agent_id')
        start_date= request.data.get('start_date')
        end_date=request.data.get('end_date')
        tenure=request.data.get('tenure')
        if tenure:
            tenure=json.loads(tenure)
        callopening=request.data.get('callopening')
        if callopening:
            callopening=json.loads(callopening)
        customerauthentication=request.data.get('customerauthentication')
        if customerauthentication:
            customerauthentication=json.loads(customerauthentication)
        onhold=request.data.get('onhold')
        if onhold:
            onhold=json.loads(onhold)
        Curiousity=request.data.get('Curiousity')
        if Curiousity:
            Curiousity=json.loads(Curiousity)
        activelistening=request.data.get('activelistening')
        if activelistening:
            activelistening=json.loads(activelistening)
        probing=request.data.get('probing')
        if probing:
            probing=json.loads(probing)
        paraphrasing=request.data.get('paraphrasing')
        if paraphrasing:
            paraphrasing=json.loads(paraphrasing)
        rateofspeech=request.data.get('rateofspeech')
        if rateofspeech:
            rateofspeech=json.loads(rateofspeech)
        overtalkincidents=request.data.get('overtalkincidents')
        if overtalkincidents:
            overtalkincidents=json.loads(overtalkincidents) 
        silenceincidents=request.data.get('silenceincidents')
        if silenceincidents:
            silenceincidents=json.loads(silenceincidents)  
        voicevolume=request.data.get('voicevolume')
        if voicevolume:
            voicevolume=json.loads(voicevolume)  
        clarity=request.data.get('clarity')
        if clarity:
            clarity=json.loads(clarity) 
        responsiveness=request.data.get('responsiveness')
        if responsiveness:
            responsiveness=json.loads(responsiveness) 
        confidence=request.data.get('confidence')
        if confidence:
            confidence=json.loads(confidence)
        listening=request.data.get('listening')
        if listening:
            listening=json.loads(listening)
        answering=request.data.get('answering')
        if answering:
            answering=json.loads(answering)
        questioning=request.data.get('questioning')
        if questioning:
            questioning=json.loads(questioning) 
        informationaccuracy=request.data.get('informationaccuracy')
        if informationaccuracy:
            informationaccuracy=json.loads(informationaccuracy)
        criticalmiss=request.data.get('criticalmiss')
        if criticalmiss:
            criticalmiss=json.loads(criticalmiss) 
        noncriticalmiss=request.data.get('noncriticalmiss')
        if noncriticalmiss:
            noncriticalmiss=json.loads(noncriticalmiss)
        calltransferrate=request.data.get('calltransferrate')
        if calltransferrate:
            calltransferrate=json.loads(calltransferrate) 
        troubleshooting=request.data.get('troubleshooting')
        if troubleshooting:
            troubleshooting=json.loads(troubleshooting) 
        callsummarization=request.data.get('callsummarization')
        if callsummarization:
            callsummarization=json.loads(callsummarization)    
        csat=request.data.get('csat')
        if csat:
            csat=json.loads(csat) 
        search_param = {}
        fields=["Tenure","Call opening","Customer Authentication","On Hold","Curiousity","Active Listening","Probing","Paraphrasing","Rate of speech (WPM)","overtalk incidents","Silence incidents","Voice volume","Clarity","Responsiveness","Confidence","Listening","Answering","Questioning","Information accuracy","Critical miss","Non-critical miss","Call trasfer rate","Troubleshooting","call summarization","CSAT"]
        data={
                    "bool": {
                    "must": []
                    }
                }
        search_param["size"]=0
        if(start_date and end_date):
            date_query={
                    "range": {
                    "Date of call": {
                        "gte": start_date,
                        "lte": end_date
                        }
                    }
                    }
            query=date_query
            data["bool"]["must"].append(query)
            
        if(lOB_id):
            lob_query= {
                    "match": {
                        "LOB_id": lOB_id
                    }
                    }
            query1=lob_query
            data["bool"]["must"].append(query1)
               
        if(team_id):
            team_query={
                    "match": {
                        "Team_id": team_id
                    }
                    }
            query2=team_query
            data["bool"]["must"].append(query2)
            
        if(agent_id):
            agent_query={
                    "match": {
                        "Agent_id": agent_id
                    }
                    }
            query3=agent_query
            data["bool"]["must"].append(query3)

        if(tenure):
            tenure_query={
                    "range": {
                    "Tenure": {
                        "gte":  tenure[0],
                        "lte":  tenure[1]
                        }
                    }
                    }
            query4=tenure_query
            data["bool"]["must"].append(query4)

        if(callopening):
            callopening_query={
                    "range": {
                    "Call opening": {
                        "gte":  callopening[0],
                        "lte":  callopening[1]
                        }
                    }
                    }
            query5=callopening_query
            data["bool"]["must"].append(query5)
        
        if(customerauthentication):
            customerauthentication_query={
                    "range": {
                    "Customer Authentication": {
                        "gte": customerauthentication[0],
                        "lte": customerauthentication[1]
                        }
                    }
                    }
            query6=customerauthentication_query
            data["bool"]["must"].append(query6)
        
        if(onhold):
            onhold_query={
                    "range": {
                    "On Hold": {
                        "gte": onhold[0],
                        "lte": onhold[1]
                        }
                    }
                    }
            query7=onhold_query
            data["bool"]["must"].append(query7)
        
        if(Curiousity):
            curiousity_query={
                    "range": {
                    "Curiousity": {
                        "gte": Curiousity[0],
                        "lte": Curiousity[1]
                        }
                    }
                    }
            query8=curiousity_query
            data["bool"]["must"].append(query8)
        
        if(activelistening):
            activelistening_query={
                    "range": {
                    "Active Listening": {
                        "gte":  activelistening[0],
                        "lte":  activelistening[1]
                        }
                    }
                    }
            query9=activelistening_query
            data["bool"]["must"].append(query9)

        if(probing):
            probing_query={
                    "range": {
                    "Probing": {
                        "gte": probing[0],
                        "lte": probing[1]
                        }
                    }
                    }
            query10=probing_query
            data["bool"]["must"].append(query10)
        
        if(paraphrasing):
            paraphrasing_query={
                    "range": {
                    "Paraphrasing": {
                        "gte": paraphrasing[0],
                        "lte": paraphrasing[1]
                        }
                    }
                    }
            query11=paraphrasing_query
            data["bool"]["must"].append(query11)
        
        if(rateofspeech):
            rateofspeech_query={
                    "range": {
                    "Rate of speech (WPM)": {
                        "gte": rateofspeech[0],
                        "lte": rateofspeech[1]
                        }
                    }
                    }
            query12=rateofspeech_query
            data["bool"]["must"].append(query12)

        if(overtalkincidents):
            overtalkincidents_query={
                    "range": {
                    "overtalk incidents": {
                        "gte": overtalkincidents[0],
                        "lte": overtalkincidents[1]
                        }
                    }
                    }
            query13=overtalkincidents_query
            data["bool"]["must"].append(query13)

        if(silenceincidents):
            silenceincidents_query={
                    "range": {
                    "Silence incidents": {
                        "gte": silenceincidents[0],
                        "lte": silenceincidents[1]
                        }
                    }
                    }
            query14=silenceincidents_query
            data["bool"]["must"].append(query14)

        if(voicevolume):
            voicecolume_query={
                    "range": {
                    "Voice volume": {
                        "gte": voicevolume[0],
                        "lte": voicevolume[1]
                        }
                    }
                    }
            query15=voicecolume_query
            data["bool"]["must"].append(query15)

        if(clarity):
            clarity_query={
                    "range": {
                    "Clarity": {
                        "gte": clarity[0],
                        "lte": clarity[1]
                        }
                    }
                    }
            query16=clarity_query
            data["bool"]["must"].append(query16)

        if(responsiveness):
            responsiveness_query={
                    "range": {
                    "Responsiveness": {
                        "gte": responsiveness[0],
                        "lte": responsiveness[1]
                        }
                    }
                    }
            query17=responsiveness_query
            data["bool"]["must"].append(query17)

        if(confidence):
            confidence_query={
                    "range": {
                    "Confidence": {
                        "gte": confidence[0],
                        "lte": confidence[1]
                        }
                    }
                    }
            query18=confidence_query
            data["bool"]["must"].append(query18)
        
        if(listening):
            listening_query={
                    "range": {
                    "Listening": {
                        "gte": listening[0],
                        "lte": listening[1]
                        }
                    }
                    }
            query19=listening_query
            data["bool"]["must"].append(query19)
        
        if(answering):
            answering_query={
                    "range": {
                    "Answering": {
                        "gte": answering[0],
                        "lte": answering[1]
                        }
                    }
                    }
            query20=answering_query
            data["bool"]["must"].append(query20)
        
        if(questioning):
            questioning_query={
                    "range": {
                    "Questioning": {
                        "gte": questioning[0],
                        "lte": questioning[1]
                        }
                    }
                    }
            query21=questioning_query
            data["bool"]["must"].append(query21)
        
        if(informationaccuracy):
            informationaccuracy_query={
                    "range": {
                    "Information accuracy": {
                        "gte": informationaccuracy[0],
                        "lte": informationaccuracy[1]
                        }
                    }
                    }
            query22=informationaccuracy_query
            data["bool"]["must"].append(query22)
        
        if(criticalmiss):
            criticalmiss_query={
                    "range": {
                    "Critical miss": {
                        "gte": criticalmiss[0],
                        "lte": criticalmiss[1]
                        }
                    }
                    }
            query23=criticalmiss_query
            data["bool"]["must"].append(query23)
        
        if(noncriticalmiss):
            noncriticalmiss_query={
                    "range": {
                    "Non-critical miss": {
                        "gte": noncriticalmiss[0],
                        "lte": noncriticalmiss[1]
                        }
                    }
                    }
            query24=noncriticalmiss_query
            data["bool"]["must"].append(query24)
        
        if(calltransferrate):
            calltrasferrate_query={
                    "range": {
                    "Call trasfer rate": {
                        "gte": calltransferrate[0],
                        "lte": calltransferrate[1]
                        }
                    }
                    }
            query25=calltrasferrate_query
            data["bool"]["must"].append(query25)
        
        if(troubleshooting):
            troubleshooting_query={
                    "range": {
                    "Troubleshooting": {
                        "gte": troubleshooting[0],
                        "lte": troubleshooting[1]
                        }
                    }
                    }
            query26=troubleshooting_query
            data["bool"]["must"].append(query26)
        
        if(callsummarization):
            callsummarization_query={
                    "range": {
                    "call summarization": {
                        "gte": callsummarization[0],
                        "lte": callsummarization[1]
                        }
                    }
                    }
            query27=callsummarization_query
            data["bool"]["must"].append(query27)
        
        if(csat):
            csat_query={
                    "range": {
                    "CSAT": {
                        "gte": csat[0],
                        "lte": csat[1]
            
                    }
                    }
                    }
            query28=csat_query
            data["bool"]["must"].append(query28)

        search_param["query"]=data
        final_data={}
        for field in fields:
            search_param["aggs"]={
                    "field_avg": {
                    "avg": {
                        "field": field
                    }
                    }
                }
            data=es.search(index='quality_works', body=search_param)
            final_data[field]=round(data["aggregations"]["field_avg"]["value"],2)
        r=rh.ResponseMsg(data=final_data, error=False, msg="filter works successfully")
        return Response(r.response)

class Minmaxvalueview(APIView):
    def get(self,request,format=None):
        search_param = {}
        final_data={}
        fields=["Tenure","Call opening","Customer Authentication","On Hold","Curiousity","Active Listening","Probing","Paraphrasing","Rate of speech (WPM)","overtalk incidents","Silence incidents","Voice volume","Clarity","Responsiveness","Confidence","Listening","Answering","Questioning","Information accuracy","Critical miss","Non-critical miss","Call trasfer rate","Troubleshooting","call summarization","CSAT"]
        search_param["size"]=0
        for field in fields:
            minmax=[]
            search_param["aggs"]={
                    "max_value": {
                        "max": {
                        "field": field
                        }
                    },
                    "min_value": {
                        "min": {
                        "field": field
                        }
                    }
                    }
            data=es.search(index='quality_works', body=search_param)
            min_value=round(data["aggregations"]["min_value"]["value"],2)
            max_value=round(data["aggregations"]["max_value"]["value"],2)
            minmax.append(min_value)
            minmax.append(max_value)
            final_data[field]=minmax
        r=rh.ResponseMsg(data=final_data, error=False, msg="min max value for allfilter get successfully")
        return Response(r.response)