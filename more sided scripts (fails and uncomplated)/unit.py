from flask_restful import Resource, Api, request
from package.model import conn
class units(Resource):
    """This contain apis to carry out activity with all nurses"""

    def get(self):
        """Retrive list of all the nurse"""

        units = conn.execute("SELECT * FROM unit ORDER BY unit_date DESC").fetchall()
        return units



    def post(self):
        """Add the new nurse"""

        unitInput = request.get_json(force=True)
        unit_hospital=unitInput['unit_hospital']
        unit_num_machines = unitInput['unit_num_machines']
        unit_num_patients = unitInput['unit_num_patients']
        unit_technicalSupport = unitInput['unit_technicalSupport']
        unitInput['unit_id']=conn.execute('''INSERT INTO unit(unit_hospital,unit_num_machines,unit_num_patients, unit_technicalSupport)
            VALUES(?,?,?,?)''', (unit_hospital, unit_num_machines,unit_num_patients,unit_technicalSupport)).lastrowid
        conn.commit()
        return unitInput

class unit(Resource):
    """It include all the apis carrying out the activity with the single nurse"""


    def get(self,id):
        """get the details of the nurse by the nurse id"""

        nurse = conn.execute("SELECT * FROM nurse WHERE nur_id=?",(id,)).fetchall()
        return nurse

    def delete(self, id):
        """Delete the nurse by its id"""

        conn.execute("DELETE FROM nurse WHERE nur_id=?", (id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """Update the nurse by its id"""

        unitInput = request.get_json(force=True)
        unit_hospital=unitInput['unit_hospital']
        unit_num_machines = unitInput['unit_num_machines']
        unit_num_patients = unitInput['unit_num_patients']
        unit_technicalSupport = unitInput['unit_technicalSupport']
        conn.execute(
            "UPDATE unit SET unit_hospital=?,unit_num_machines=?,unit_num_patients=?,unit_technicalSupport=? WHERE unit_id=?",
            (unit_hospital, unit_num_machines, unit_num_patients, unit_technicalSupport, id))
        conn.commit()
        return unitInput