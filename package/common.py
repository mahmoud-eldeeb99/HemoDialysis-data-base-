from flask_restful import Resource, Api, request
from package.model import conn


class Common(Resource):
    """This contain common api ie noe related to the specific module"""

    def get(self):
        """Retrive the patient, doctor, appointment, medication count for the dashboard page"""

        getPatientCount=conn.execute("SELECT COUNT(*) AS patient FROM patient").fetchone()
        getDoctorCount = conn.execute("SELECT COUNT(*) AS doctor FROM doctor").fetchone()
        getAppointmentCount = conn.execute("SELECT COUNT(*) AS appointment FROM appointment").fetchone()
        getMedicationCount = conn.execute("SELECT COUNT(*) AS medication from medication").fetchone()
        getDepartmentCount = conn.execute("SELECT COUNT(*) AS department FROM department").fetchone()
        getNurseCount = conn.execute("SELECT COUNT(*) AS nurse FROM nurse").fetchone()


        getPatientCount.update(getDoctorCount)
        getPatientCount.update(getAppointmentCount)
        getPatientCount.update(getMedicationCount)
        getPatientCount.update(getDepartmentCount)
        getPatientCount.update(getNurseCount)


        return getPatientCount