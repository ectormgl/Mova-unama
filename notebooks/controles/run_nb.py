"""Executa um notebook célula a célula, salvando após cada célula. Uso: python run_nb.py entrada.ipynb saida.ipynb"""
import sys, time, nbformat
from nbclient import NotebookClient
src, dst = sys.argv[1], sys.argv[2]
nb = nbformat.read(src, as_version=4)
t0 = time.time()
def salvar(cell, cell_index, **kw):
    nbformat.write(nb, dst)
    print(f'[{time.time()-t0:7.0f}s] célula {cell_index} ok', flush=True)
    for o in cell.get('outputs', []):
        txt = o.get('text') or o.get('data', {}).get('text/plain', '')
        if txt and 'Figure' not in txt: print('   ', txt[-1500:].replace('\n', '\n    '), flush=True)
client = NotebookClient(nb, timeout=None, kernel_name='python3', on_cell_executed=salvar)
try:
    client.execute(); print('FIM OK', round(time.time()-t0), 's', flush=True)
except Exception as e:
    print('ERRO:', str(e)[-4000:], flush=True)
nbformat.write(nb, dst)
