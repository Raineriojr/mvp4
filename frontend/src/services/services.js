function renderList(array, tableBody) {
  if (array.length == 0) {
    return tableBody.innerHTML = `
      <tr>
          <td colspan="15" class="text-center">Sem pacientes cadastrados</td>
      </tr>`;
  }

  tableBody.innerHTML = array.map((item, index) => {

    const setSTSlope = () => {
      if (item.st_slope_up == 1) {
        return 'Up'
      } else if (item.st_slope_down == 1) {
        return 'Down'
      } else if (item.st_slope_flat == 1) {
        return 'Flat'
      }
    }

    const setChestPain = () => {
      if (item.chest_pain_asy == 1) {
        return 'Dor Torácica Assintomática'
      } else if (item.chest_pain_ata == 1) {
        return 'Dor Torácica Atípica'
      } else if (item.chest_pain_nap == 1) {
        return 'Dor Torácica Não Anginosa'
      } else if (item.chest_pain_ta == 1) {
        return 'Dor Torácica Típica'
      }
    }

    const setECG = () => {
      if (item.resting_lvh == 1) {
        return 'Hipertrofia Ventricular Esquerda em Repouso'
      } else if (item.resting_normal == 1) {
        return 'Eletrocardiograma de Repouso Normal'
      } else if (item.resting_st == 1) {
        return 'Anormalidade do Segmento ST no Eletrocardiograma de Repouso'
      }
    }

    return `
      <tr>
          <td class="text-nowrap">${index + 1}</td>
          <td class="text-nowrap">${item.heart_disease == 0 ? 'Normal' : 'Doença Cardíaca'}</td>
          <td class="text-nowrap">${item.name}</td>
          <td class="text-nowrap">${item.age} anos</td>
          <td class="text-nowrap">${item.sex == 0 ? 'F' : 'M'}</td>
          <td class="text-nowrap">${setChestPain()}</td>
          <td class="text-nowrap">${item.resting_b} mm Hg</td>
          <td class="text-nowrap">${item.cholesterol} mm/dl</td>
          <td class="text-nowrap">${item.fastingBS}</td>
          <td class="text-nowrap">${setECG()}</td>
          <td class="text-nowrap">${item.max_hr}</td>
          <td class="text-nowrap">${item.exercise_angina}</td>
          <td class="text-nowrap">${item.oldpeak}</td>
          <td class="text-nowrap">${setSTSlope()}</td>
      </tr>`;
  }).join('');
}