from flask import Flask, redirect, request, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
import requests

from flask_cors import CORS

from models import Session, Patient, Model
from schemas import *

from logger import logger

info = Info(
    title="MVP 4 - Projeto",
    description="API para MVP 4 de Eng. de Software",
    version="1.0.0",
)


app: Flask = OpenAPI(__name__, info=info)
CORS(app, resources={r"/*": {"origins": "*"}})

# tags
doc_tag = Tag(name="Documentação",
              description="Documentação de rotas da aplicação")

patient_tag = Tag(name="Paciente", description="Rotas de paciente")


@app.get("/", tags=[doc_tag])
def index():
    """Retorna documentação da API no swagger"""
    return redirect("openapi/swagger")


@app.get("/patient", tags=[patient_tag], responses={"200": PatientListViewSchema, "404": ErrorSchema})
def patientList():
    """Lista pacientes cadastrados"""
    try:
        session = Session()

        patients = (
            session.query(Patient).all()
        )

        if not patients:
            return {"patient_list": []}, 200
        else:
            return patient_list(patients), 200

    except Exception as e:
        logger.warning(f"Erro ao listar pacientes: {e}")
        return {"error": f"Erro ao listar pacientes: {e}"}, 400


@app.post("/patient", tags=[patient_tag], responses={"200": PatientViewSchema, "404": ErrorSchema})
def createPatient(body: PatientSchema):
    """
        Cadastro de novo paciente para predição;
        
        name: Nome
        age: Idade
        sex: Sexo
        resting_b: Pressão Arterial de Repouso
        cholesterol: Colesterol
        fastingBS: Glicemia de Jejum
        max_hr: Frequência Cardíaca Máxima Atingida
        exercise_angina: Angina Induzida por Exercício
        oldpeak: Depressão do Segmento ST (medida numérica)
        st_slope_down: Inclinação para Baixo do Segmento ST
        st_slope_flat: Inclinação Plana do Segmento ST
        st_slope_up: Inclinação para Cima do Segmento ST
        chest_pain_asy: Dor Torácica Assintomática
        chest_pain_ata: Dor Torácica Atípica
        chest_pain_nap: Dor Torácica Não Anginosa
        chest_pain_ta: Dor Torácica Típica
        resting_lvh: Hipertrofia Ventricular Esquerda em Repouso
        resting_normal: Eletrocardiograma de Repouso Normal
        resting_st: Anormalidade do Segmento ST no Eletrocardiograma de Repouso
    """
    try:
        patient_data = PatientSchema.model_validate(request.get_json())
        
        session = Session()

        #carregando modelo
        ml_path = 'ml_model/modelo.pkl'
        model = Model.load_model(ml_path)

        patient = Patient(
            name = patient_data.name,
            age = patient_data.age,
            sex = patient_data.sex,
            resting_b = patient_data.resting_b,
            cholesterol = patient_data.cholesterol,
            fastingBS = patient_data.fastingBS,
            max_hr = patient_data.max_hr,
            exercise_angina = patient_data.exercise_angina,
            oldpeak = patient_data.oldpeak,
            st_slope_down = patient_data.st_slope_down,
            st_slope_flat = patient_data.st_slope_flat,
            st_slope_up = patient_data.st_slope_up,
            chest_pain_asy = patient_data.chest_pain_asy,
            chest_pain_ata = patient_data.chest_pain_ata,
            chest_pain_nap = patient_data.chest_pain_nap,
            chest_pain_ta = patient_data.chest_pain_ta,
            resting_lvh = patient_data.resting_lvh,
            resting_normal = patient_data.resting_normal,
            resting_st = patient_data.resting_st,
            heart_disease= Model.predictor(model, patient_data)
        )

        if session.query(Patient).filter(Patient.name == patient_data.name).first():
            logger.warning(f"Paciente já existe na base: {patient.name}")
            return {"error": f"Paciente já existe na base"}, 409
        
        #adiciona paciente
        session.add(patient);
        session.commit();

        logger.debug(f"Paciente adicionado com sucesso: {patient.name}")
        return create_patient_response(patient), 200
    
    except Exception as e:
        logger.warning(f"Erro ao cadastrar paciente: {e}")
        return {"error": f"Erro ao cadastrar paciente: {e}"}, 400



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
