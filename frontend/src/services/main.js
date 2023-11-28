const BASE_URL = "http://127.0.0.1:5001";

async function getList() {
  try {
    const responseAPI = await fetch(
      `${BASE_URL}/patient`,
      {
        method: 'GET',
      }
    )
    return responseAPI.json()
  }
  catch (error) {
    console.warn("Erro ao listar pacientes:", error)
    return error
  }
}

async function createPatient(data) {
  const st_slope = data.st_slope;
  const chest_pain = data.chest_pain;
  const ecg = data.ecg;

  const payload = {
    name: data.name,
    age: Number(data.age),
    sex: Number(data.sex),
    resting_b: Number(data.resting_b),
    cholesterol: Number(data.cholesterol),
    fastingBS: Number(data.fastingBS),
    max_hr: Number(data.max_hr),
    exercise_angina: Number(data.exercise_angina),
    oldpeak: Number(data.oldpeak),
    st_slope_down: st_slope == "down" ? 1 : 0,
    st_slope_flat: st_slope == "flat" ? 1 : 0,
    st_slope_up: st_slope == "up" ? 1 : 0,
    chest_pain_asy: chest_pain == "chest_pain_asy" ? 1 : 0,
    chest_pain_ata: chest_pain == "chest_pain_ata" ? 1 : 0,
    chest_pain_nap: chest_pain == "chest_pain_nap" ? 1 : 0,
    chest_pain_ta: chest_pain == "chest_pain_ta" ? 1 : 0,
    resting_lvh: ecg == "resting_lvh" ? 1 : 0,
    resting_normal: ecg == "resting_normal" ? 1 : 0,
    resting_st: ecg == "resting_st" ? 1 : 0,
  }

  try {
    const responseAPI = await fetch(
      `${BASE_URL}/patient`,
      {
        headers:{
          "Content-Type": "application/json" 
        },
        method: 'POST',
        body: JSON.stringify(payload)
      },
    )
    return responseAPI.json()
  }
  catch (error) {
    console.warn("Erro ao cadastrar paciente:", error)
    throw error
  }
}