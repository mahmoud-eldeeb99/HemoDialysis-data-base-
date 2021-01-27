from flask_restful import Resource, Api, request
from package.model import conn

class stat(Resource):
    def get(self):
        ### retrives patients number

        total=conn.execute("SELECT COUNT(*) FROM patient")
        return  total
    def get(self):
        old=conn.executeen("select count(*) from patient where  _age >60")
        return old
    def get(self):
        ava= conn.execute("select ava( pat_age) from patient ")
        return ava
    def get(self):
        hypertension=conn.execute("select count(*) from patient where pat_blood_pressure==hypertension ")
        return hypertension
    def get(self):
        hypotension =conn.execute("select count(*) from patient where pat_blood_pressure==hypotention")
        return hypotension





