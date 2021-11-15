from django.db.models import fields
from rest_framework import serializers
from .models import *

class LOBserializer(serializers.ModelSerializer):
    label=serializers.SerializerMethodField('get_lobname_from_lob')
    value=serializers.SerializerMethodField('get_value_from_lob')
    class Meta:
        model=LOB
        fields = ['id','User','Lob_name','label','value']
    def get_lobname_from_lob(self, lob):
        label=lob.Lob_name
        return label
    def get_value_from_lob(self, lob):
        value=lob.id
        return value
class Reportingmanagerserialiazer(serializers.ModelSerializer):
    class Meta:
        model=Reporting_Manager
        fields="__all__"
class Teamserializer(serializers.ModelSerializer):
    Reporting_manager=Reportingmanagerserialiazer()
    LOB=LOBserializer(many=True)
    label=serializers.SerializerMethodField('get_teamname_from_Team')
    value=serializers.SerializerMethodField('get_value_from_Team')
    class Meta:
        model=Teams
        fields = ['id','Team_name','No_agentns','Locations','Reporting_manager','LOB','label','value','Lob_list']
        fields="__all__"

    def get_teamname_from_Team(self, team):
        label=team.Team_name
        return label
    def get_value_from_Team(self, team):
        value=team.id
        return value         
class Agentserializer(serializers.ModelSerializer):
    Team=Teamserializer()
    label=serializers.SerializerMethodField('get_agentname_from_Agent')
    value=serializers.SerializerMethodField('get_value_from_Agent')
    class Meta:
        model=Agents
        fields = ['id','Agent_name','Agent_id','Date_of_join','Team','label','value']

    def get_agentname_from_Agent(self, agent):
        label=agent.Agent_name
        return label
    def get_value_from_Agent(self, agent):
        value=agent.id
        return value

class Reportingserializer(serializers.ModelSerializer):
    label=serializers.SerializerMethodField('get_agentname_from_Agent')
    value=serializers.SerializerMethodField('get_value_from_Agent')
    class Meta:
        model=Reporting
        fields = ['id','Matrix_type','User','Weights','label','value']

    def get_agentname_from_Agent(self, matrix):
        label=matrix.Matrix_type
        return label
    def get_value_from_Agent(self, matrix):
        value=matrix.id
        return value

class SOPserializer(serializers.ModelSerializer):
    class Meta:
        model=SOP
        fields='__all__'

class SOPTypesserializer(serializers.ModelSerializer):
    Sop_sub_types=SOPserializer(many=True)
    class Meta:
        model=SOP_Types
        fields = ['id','User','Sop_name','Sop_sub_types']

