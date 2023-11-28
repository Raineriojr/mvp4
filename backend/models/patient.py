from sqlalchemy import Column, Integer, Float, String

from models import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age	= Column(Integer)
    sex	= Column(Integer)
    resting_b= Column(Integer)
    cholesterol	= Column(Integer)
    fastingBS = Column(Integer)
    max_hr = Column(Integer)
    exercise_angina = Column(Integer)
    oldpeak	= Column(Float)
    st_slope_down = Column(Integer)
    st_slope_flat = Column(Integer)
    st_slope_up = Column(Integer)
    chest_pain_asy = Column(Integer)
    chest_pain_ata = Column(Integer)
    chest_pain_nap = Column(Integer)
    chest_pain_ta = Column(Integer)
    resting_lvh = Column(Integer)
    resting_normal = Column(Integer)
    resting_st = Column(Integer)
    heart_disease = Column(Integer)

    def __init__(
        self,
        name: str,
        age: int,
        sex: int,
        resting_b: int,
        cholesterol: int,
        fastingBS: int,
        max_hr: int,
        exercise_angina: int,
        oldpeak: float,
        st_slope_down: int,
        st_slope_flat: int,
        st_slope_up: int,
        chest_pain_asy: int,
        chest_pain_ata: int,
        chest_pain_nap: int,
        chest_pain_ta: int,
        resting_lvh: int,
        resting_normal: int,
        resting_st: int,
        heart_disease: int,
    ):
            """
                Cria um paciente com esses parametros;
                
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
                heart_disease: Doença Cardíaca (Variável de Saída)
            """
            self.name = name
            self.age = age
            self.sex = sex
            self.resting_b = resting_b
            self.cholesterol = cholesterol
            self.fastingBS = fastingBS
            self.max_hr = max_hr
            self.exercise_angina = exercise_angina
            self.oldpeak = oldpeak
            self.st_slope_down = st_slope_down
            self.st_slope_flat = st_slope_flat
            self.st_slope_up = st_slope_up
            self.chest_pain_asy = chest_pain_asy
            self.chest_pain_ata = chest_pain_ata
            self.chest_pain_nap = chest_pain_nap
            self.chest_pain_ta = chest_pain_ta
            self.resting_lvh = resting_lvh
            self.resting_normal = resting_normal
            self.resting_st = resting_st
            self.heart_disease = heart_disease
