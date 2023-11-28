from pydantic import BaseModel
from typing import List

class PatientSchema(BaseModel):
    """Schema para cadastro do paciente"""

    name: str = "Rainério"
    age: int = 40
    sex: int = 1
    resting_b: int = 140
    cholesterol: int = 289
    fastingBS: int = 0
    max_hr: int = 172
    exercise_angina: int = 0
    oldpeak: float = 0.0
    st_slope_down: int = 0
    st_slope_flat: int = 0
    st_slope_up: int = 1
    chest_pain_asy: int = 0
    chest_pain_ata: int = 1
    chest_pain_nap: int = 0
    chest_pain_ta: int = 0
    resting_lvh: int = 0
    resting_normal: int = 1
    resting_st: int = 0


class PatientViewSchema(BaseModel):
    """Schema para retorno de paciente cadastrado """

    id: int = 0


class PatientListViewSchema(BaseModel):
    """Schema para listagem de pacientes """

    name: str = 'Rainério'
    age: int = 40
    sex: int = 1
    resting_b: int = 140
    cholesterol: int = 289
    fastingBS: int = 0
    max_hr: int = 172
    exercise_angina: int = 0
    oldpeak: float = 0.0
    st_slope_down: int = 0
    st_slope_flat: int = 0
    st_slope_up: int = 1
    chest_pain_asy: int = 0
    chest_pain_ata: int = 1
    chest_pain_nap: int = 0
    chest_pain_ta: int = 0
    resting_lvh: int = 0
    resting_normal: int = 1
    resting_st: int = 0
    heart_disease: int = 0


def create_patient_response(patient: PatientViewSchema):
    """Schema de retorno apos cadastrar paciente"""
    return {
        "id": patient.id
    }


def patient_list(patientList: List[PatientListViewSchema]):
    """Schema para retorno de lista de pacientes"""
    list = []
    for patient in patientList:
            list.append(
               {
                    "name": patient.name,
                    "age": patient.age,
                    "sex": patient.sex,
                    "resting_b": patient.resting_b,
                    "cholesterol": patient.cholesterol,
                    "fastingBS": patient.fastingBS,
                    "max_hr": patient.max_hr,
                    "exercise_angina": patient.exercise_angina,
                    "oldpeak": patient.oldpeak,
                    "st_slope_down": patient.st_slope_down,
                    "st_slope_flat": patient.st_slope_flat,
                    "st_slope_up": patient.st_slope_up,
                    "chest_pain_asy": patient.chest_pain_asy,
                    "chest_pain_ata": patient.chest_pain_ata,
                    "chest_pain_nap": patient.chest_pain_nap,
                    "chest_pain_ta": patient.chest_pain_ta,
                    "resting_lvh": patient.resting_lvh,
                    "resting_normal": patient.resting_normal,
                    "resting_st": patient.resting_st,
                    "heart_disease": patient.heart_disease,
                }  
            )
    return { "patient_list": list }
