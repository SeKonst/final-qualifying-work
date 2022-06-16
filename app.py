from tensorflow import keras
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Main.html', name='Предсказание значения "Соотношение матрица-наполнитель"')


def processing_params(plotn, mod_uprug, quant_otverd, content_epoks, temp_flash, surf_dens, mod_upr_rast, proch_rast, consum_smol, angl_patch, step_patch, dens_patch):
#     TODO: Добавить логику модели
     model = keras.models.load_model("\финал\app")
     pred = model.predict([plotn, mod_uprug, quant_otverd, content_epoks, temp_flash, surf_dens, mod_upr_rast, proch_rast, consum_smol, angl_patch, step_patch, dens_patch])
     message = f"Предсказание равно {pred}"
     return message

@app.route('/params/', methods=['post', 'get'])
def get_params():
    message = ''
    if request.method == 'POST':
        plotn = request.form.get('plotn')  # запрос к данным формы
        mod_uprug = request.form.get('mod_uprug')  # запрос к данным формы
        quant_otverd = request.form.get('quant_otverd')  
        content_epoks = request.form.get('content_epoks')
        temp_flash = request.form.get('temp_flash')
        surf_dens = request.form.get('surf_dens')
        mod_upr_rast = request.form.get('mod_upr_rast')
        proch_rast = request.form.get('proch_rast')
        consum_smol = request.form.get('consum_smol')
        angl_patch = request.form.get('angl_patch')
        step_patch = request.form.get('step_patch')
        dens_patch = request.form.get('dens_patch')
        
        
        
        
        plotn = float(plotn)
        mod_uprug = float(mod_uprug)
        quant_otverd = float(quant_otverd)
        content_epoks = float(content_epoks)
        temp_flash = float(temp_flash)
        surf_dens = float(surf_dens)
        mod_upr_rast = float(mod_upr_rast)
        proch_rast = float(proch_rast)
        consum_smol = float(consum_smol)
        angl_patch = int(angl_patch)
        step_patch = float(step_patch)
        dens_patch = float(dens_patch)
        

        message = processing_params(plotn, mod_uprug, quant_otverd, content_epoks, temp_flash, surf_dens, mod_upr_rast, proch_rast, consum_smol, angl_patch, step_patch, dens_patch)

    return render_template('params.html', message=message)

if __name__ == '__main__':
    app.run()