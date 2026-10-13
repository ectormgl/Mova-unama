"""Ablação: efeito da faixa do acelerômetro (saturação por eixo) nos limiares publicados, na SisFall."""
import nbformat, numpy as np, pandas as pd, json, sys
nb = nbformat.read('run_real/estudo.ipynb', as_version=4)
cells = [c.source for c in nb.cells if c.cell_type == 'code']
src = "\n".join(cells)
met = next(c for c in cells if 'def wilson' in c).replace("display(por_base(PRED_PUB).round(3))", "")
src = src.split("t0 = time.time()\nPRED_PUB = []")[0] + "\n" + met
src = src.replace("display(", "print(").replace("plt.show()", "plt.close('all')")
src = src.replace("BASE_DIR = Path('.').resolve()", "BASE_DIR = Path('run_real').resolve()")
src = src.replace("DIRECOES = [('SisFall', 'MobiFall'), ('MobiFall', 'SisFall')]", "DIRECOES = [('SisFall', 'SisFall')]")
src = src.replace("RESULTS_DIR = BASE_DIR / 'results', BASE_DIR / 'results'", "")
out = []
for clip in (None,):
    s = src.replace("CLIP_G = 8.0", f"CLIP_G = {clip}").replace("FS     = 50 ", "FS     = 200 ").replace("RESULTS_DIR.mkdir(exist_ok=True)", "RESULTS_DIR = BASE_DIR / 'results_200hz'; RESULTS_DIR.mkdir(exist_ok=True)")
    g = {}; exec(s, g)
    tr = g['DADOS']['SisFall']
    preds = [g['pred_limiar'](tr, 'Kangas', g['KANGAS_PUB']).assign(metodo='Kangas'),
             g['pred_limiar'](tr, 'Bourke3', g['BOURKE_PUB']).assign(metodo='Bourke3'),
             pd.DataFrame([g['_linha'](t, n_alarmes=len(g['pipto_detect'](t.acc))) for t in tr]).assign(metodo='PIPTO')]
    for p in preds:
        m = g['metricas'](p)
        out.append(dict(faixa_g=('sem limite (±16 g do sensor)' if clip is None else f'±{clip:g} g'), metodo=p.metodo.iloc[0],
                        SE=m['SE'], SP=m['SP'], F1=m['F1'], FA_h=m['FA_h']))
        print(out[-1], flush=True)
pd.DataFrame(out).to_csv('run_real/results/taxa_nativa_200hz_sisfall.csv', index=False)
print('FIM')
