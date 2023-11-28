import numpy as np
import pickle


class Model:

    def load_model(path):
        if path.endswith('.pkl'):
            return pickle.load(open(path, "rb"))
        else:
            raise Exception('Formato de arquivo não suportado')

    def predictor(model, form):
        X_input = np.array([
            form.age,
            form.sex,
            form.resting_b,
            form.cholesterol,
            form.fastingBS,
            form.max_hr,
            form.exercise_angina,
            form.oldpeak,
            form.st_slope_down,
            form.st_slope_flat,
            form.st_slope_up,
            form.chest_pain_asy,
            form.chest_pain_ata,
            form.chest_pain_nap,
            form.chest_pain_ta,
            form.resting_lvh,
            form.resting_normal,
            form.resting_st,
        ])

        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])
