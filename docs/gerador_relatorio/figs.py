import pandas as pd, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R = 'run_real/results/'
BLUE, ORANGE, AQUA, INK, INK2, GRID = '#2a78d6', '#eb6834', '#1baf7a', '#0b0b0b', '#52514e', '#e4e3df'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'axes.edgecolor': '#b9b8b3', 'axes.labelcolor': INK2,
                     'xtick.color': INK2, 'ytick.color': INK2, 'axes.spines.top': False, 'axes.spines.right': False})
SEL = ['Kangas (publicado)', 'Bourke3 (publicado)', 'PIPTO (publicado)', 'Kangas (ajustado)', 'Bourke3 (ajustado)',
       'CNN-LSTM [z treino] k=2', 'CNN-LSTM [z treino] k=1', 'CNN-LSTM [z por base] k=2', 'CNN-LSTM rot [z treino] k=1']
NOME = {'CNN-LSTM [z treino] k=2': 'CNN-LSTM (k=2, regra do artigo)', 'CNN-LSTM [z treino] k=1': 'CNN-LSTM (k=1)',
        'CNN-LSTM [z por base] k=2': 'CNN-LSTM (k=2, z por base = protocolo do artigo)',
        'CNN-LSTM rot [z treino] k=1': 'CNN-LSTM + rotação 3D (k=1)'}
def dumbbell(ba, bb, arq):
    t = pd.read_csv(R + f'tabela_{ba}_{bb}.csv').set_index('Método').loc[SEL].reset_index()
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={'width_ratios': [1.25, 1]})
    y = np.arange(len(t))[::-1]
    for yi, a, b in zip(y, t[f'{ba} F1'], t[f'{bb} F1']):
        ax[0].plot([a, b], [yi, yi], color='#c9c8c3', lw=2, zorder=1)
    ax[0].scatter(t[f'{ba} F1'], y, s=46, color=BLUE, zorder=2, label=f'{ba} (base de treino, validação por sujeito)', edgecolor='white', lw=1.5)
    ax[0].scatter(t[f'{bb} F1'], y, s=46, color=ORANGE, zorder=3, label=f'{bb} (outra base, sem retreino)', edgecolor='white', lw=1.5)
    ax[0].set_yticks(y, [NOME.get(m, m) for m in t['Método']]); ax[0].set_xlim(-0.02, 1.02); ax[0].set_xlabel('F1 por tentativa')
    ax[0].grid(axis='x', color=GRID, lw=0.8); ax[0].legend(loc='upper center', bbox_to_anchor=(0.45, -0.13), ncol=1, frameon=False, fontsize=8)
    d = t['ΔF1']; lo, hi = t['ΔF1 IC95% inf'], t['ΔF1 IC95% sup']
    cor = [INK2 if m.startswith('CNN') else BLUE for m in t['Método']]
    ax[1].errorbar(d, y, xerr=[d - lo, hi - d], fmt='none', ecolor='#9a9994', elinewidth=1.4, capsize=3)
    ax[1].scatter(d, y, s=40, c=cor, zorder=3, edgecolor='white', lw=1.2)
    ax[1].axvline(0, color='#9a9994', lw=1); ax[1].set_yticks(y, ['']*len(y)); ax[1].grid(axis='x', color=GRID, lw=0.8)
    ax[1].set_xlabel(f'ΔF1 = F1({ba}) − F1({bb})  [IC 95%]')
    for yi, v in zip(y, d): ax[1].annotate(f'{v:+.2f}', (v, yi), xytext=(0, 6), textcoords='offset points', ha='center', fontsize=7.5, color=INK)
    ax[1].set_title('perda ao trocar de base (maior = pior)', fontsize=8.5, color=INK2, loc='left')
    plt.tight_layout(); plt.savefig(arq, dpi=200, bbox_inches='tight'); plt.close()
dumbbell('SisFall', 'MobiFall', 'figs/f1_sis_mobi.png'); dumbbell('MobiFall', 'SisFall', 'figs/f1_mobi_sis.png')

# Ablação de faixa
a = pd.read_csv(R + 'ablacao_faixa_sisfall.csv')
ordem = ['sem limite (±16 g do sensor)', '±8 g', '±4 g', '±3 g', '±2 g']; xl = ['±16 g\n(original)', '±8 g', '±4 g', '±3 g', '±2 g\n(Galaxy S3)']
fig, ax = plt.subplots(figsize=(6.4, 3.4))
for m, c in (('Kangas', BLUE), ('Bourke3', ORANGE), ('PIPTO', AQUA)):
    v = a[a.metodo == m].set_index('faixa_g').loc[ordem, 'SE'].values
    ax.plot(range(5), v, color=c, lw=2, marker='o', ms=6, mec='white', mew=1.2)
    ax.annotate(m, (4, v[-1]), xytext=(8, 0), textcoords='offset points', va='center', color=INK, fontsize=8.5)
ax.set_xticks(range(5), xl); ax.set_ylim(0, 1); ax.set_ylabel('Sensibilidade na SisFall'); ax.set_xlim(-0.2, 4.7)
ax.grid(axis='y', color=GRID, lw=0.8); ax.set_xlabel('faixa simulada do acelerômetro (saturação por eixo)')
plt.tight_layout(); plt.savefig('figs/ablacao_faixa.png', dpi=200); plt.close()

# Distribuição dos picos
d = pd.read_csv('picos.csv'); fig, ax = plt.subplots(figsize=(6.4, 3.0))
bins = np.linspace(1, 12, 45)
ax.hist(d[(d.base == 'SisFall') & d.queda].pico, bins, color=BLUE, alpha=0.85, label='SisFall (cintura), quedas', density=True, edgecolor='white', lw=0.5)
ax.hist(d[(d.base == 'MobiFall') & d.queda].pico, bins, color=ORANGE, alpha=0.85, label='MobiFall (bolso, Galaxy S3), quedas', density=True, edgecolor='white', lw=0.5)
for v, txt in ((2.8, 'UFT Bourke3 = 2,8 g'), (3.06, 'PIPTO ≈ 3,06 g')):
    ax.axvline(v, color=INK2, lw=1, ls='--')
ax.annotate('limiares de impacto\nBourke3 (2,8 g) e PIPTO (≈3,06 g)', (3.1, ax.get_ylim()[1] * 0.75), fontsize=7.5, color=INK2)
ax.set_xlabel('pico de |a| na tentativa (g), a 50 Hz'); ax.set_ylabel('densidade'); ax.legend(frameon=False, fontsize=8)
plt.tight_layout(); plt.savefig('figs/picos.png', dpi=200); plt.close()

# Heatmap FP por ADL (SisFall→MobiFall e MobiFall→SisFall)
for ba, bb in (('SisFall', 'MobiFall'), ('MobiFall', 'SisFall')):
    fp = pd.read_csv(R + f'fp_por_adl_{ba}_{bb}.csv', index_col=0)
    cols = ['Kangas (publicado)', 'Bourke3 (publicado)', 'PIPTO (publicado)', 'Kangas (ajustado)', 'CNN-LSTM [z treino] k=1', 'CNN-LSTM rot [z treino] k=1']
    fp = fp[cols]
    fig, ax = plt.subplots(figsize=(6.6, 0.24 * len(fp) + 1.6))
    im = ax.imshow(fp.values, cmap='Blues', vmin=0, vmax=1, aspect='auto')
    ax.set_yticks(range(len(fp)), fp.index); ax.set_xticks(range(len(cols)), [NOME.get(c, c) for c in cols], rotation=30, ha='right')
    for i in range(fp.shape[0]):
        for j in range(fp.shape[1]):
            v = fp.values[i, j]
            if v >= 0.05: ax.text(j, i, f'{v:.2f}', ha='center', va='center', fontsize=6.5, color='white' if v > 0.55 else INK)
    ax.spines[:].set_visible(False); cb = plt.colorbar(im, ax=ax, fraction=0.03); cb.set_label('fração das tentativas com alarme falso', fontsize=7.5)
    ax.set_title(f'Falsos positivos por atividade na {bb} (detectores da {ba})', fontsize=9, loc='left')
    plt.tight_layout(); plt.savefig(f'figs/fp_{ba}_{bb}.png', dpi=200); plt.close()
print('ok')
