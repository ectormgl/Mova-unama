"""Verificação: limiares reajustados com grade AMPLIADA (a grade original ficou na borda)."""
import nbformat, numpy as np, pandas as pd
nb = nbformat.read('run_real/estudo.ipynb', as_version=4)
cells = [c.source for c in nb.cells if c.cell_type == 'code']
ate = next(i for i, c in enumerate(cells) if 'GRADE = {' in c)
src = "\n".join(cells[:ate + 1])
src = src.replace("display(", "print(").replace("plt.show()", "plt.close('all')")
src = src.replace("BASE_DIR = Path('.').resolve()", "BASE_DIR = Path('run_real').resolve()")
src = src.replace("RESULTS_DIR.mkdir(exist_ok=True)", "RESULTS_DIR = BASE_DIR / 'results_grade'; RESULTS_DIR.mkdir(exist_ok=True)")
nova = '''GRADE = {'Kangas': [dict(KANGAS_PUB, inicio=i, svtot=2.0 * s, svd=1.7 * s, maxmin=2.0 * s, z2=1.5 * s)
                    for s in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.4, 1.7, 2.0, 2.4) for i in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)],
         'Bourke3': [dict(BOURKE_PUB, uft=u, lft=l) for u in (1.3, 1.5, 1.7, 1.8, 2.0, 2.2, 2.6, 2.8, 3.2, 3.6, 4.0, 4.4)
                     for l in (0.5, 0.65, 0.8, 0.9, 0.95)]}
'''
i0 = src.index("GRADE = {"); i1 = src.index("def folds_por_sujeito")
src = src[:i0] + nova + "\n" + src[i1:]
src = src.replace("PRED_PUB = pd.concat(PRED_PUB, ignore_index=True)", "PRED_PUB = pd.concat(PRED_PUB, ignore_index=True)")
g = {}; exec(src, g)
linhas = []
for (ba, bb), pred in g['PRED_AJ'].items():
    t = g['tabela'](pred, ba, bb); t.insert(0, 'direcao', f'{ba}→{bb}'); linhas.append(t)
    for alg in ('Kangas', 'Bourke3'):
        p = g['PARAMS_AJ'][(ba, alg)]; print(ba, alg, {k: p[k] for k in p if k in ('inicio', 'svtot', 'uft', 'lft')})
out = pd.concat(linhas); out.to_csv('run_real/results/limiares_grade_ampliada.csv', index=False); print(out.round(3).to_string()); print('FIM')
