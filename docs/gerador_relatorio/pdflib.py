"""Utilitários para montar o relatório em PDF (reportlab)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak,
                                ListFlowable, ListItem, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage

import matplotlib, os as _os
F = _os.path.join(_os.path.dirname(matplotlib.__file__), 'mpl-data/fonts/ttf') + '/'
pdfmetrics.registerFont(TTFont('DV', F + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', F + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVI', F + 'DejaVuSans-Oblique.ttf'))
pdfmetrics.registerFont(TTFont('DVM', F + 'DejaVuSansMono.ttf'))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('DV', normal='DV', bold='DVB', italic='DVI', boldItalic='DVB')

ss = getSampleStyleSheet()
S = {
    'title': ParagraphStyle('t', fontName='DVB', fontSize=17, leading=22, alignment=TA_CENTER, spaceAfter=6),
    'sub': ParagraphStyle('s', fontName='DV', fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#444444')),
    'h1': ParagraphStyle('h1', fontName='DVB', fontSize=13.5, leading=17, spaceBefore=12, spaceAfter=6, textColor=colors.HexColor('#12355b')),
    'h2': ParagraphStyle('h2', fontName='DVB', fontSize=11, leading=14, spaceBefore=8, spaceAfter=4, textColor=colors.HexColor('#12355b')),
    'p': ParagraphStyle('p', fontName='DV', fontSize=9.3, leading=13, alignment=TA_JUSTIFY, spaceAfter=5),
    'small': ParagraphStyle('sm', fontName='DV', fontSize=7.8, leading=10, textColor=colors.HexColor('#333333')),
    'cap': ParagraphStyle('c', fontName='DVI', fontSize=8, leading=10.5, alignment=TA_CENTER, textColor=colors.HexColor('#333333'), spaceAfter=8),
    'box': ParagraphStyle('b', fontName='DV', fontSize=9.3, leading=13, alignment=TA_JUSTIFY, backColor=colors.HexColor('#eef3f8'),
                          borderColor=colors.HexColor('#9bb3cc'), borderWidth=0.6, borderPadding=6, spaceBefore=4, spaceAfter=10),
    'cell': ParagraphStyle('cell', fontName='DV', fontSize=7.2, leading=8.8),
    'cellb': ParagraphStyle('cellb', fontName='DVB', fontSize=7.2, leading=8.8, textColor=colors.white),
}

class Doc:
    def __init__(self, path, titulo):
        self.path, self.story = path, []
        self.doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm,
                                     bottomMargin=1.6 * cm, title=titulo, author='Projeto Mova (UNAMA)')

    def t(self, s): self.story.append(Paragraph(s, S['title']))
    def sub(self, s): self.story.append(Paragraph(s, S['sub']))
    def h1(self, s): self.story.append(Paragraph(s, S['h1']))
    def h2(self, s): self.story.append(Paragraph(s, S['h2']))
    def p(self, s): self.story.append(Paragraph(s, S['p']))
    def box(self, s): self.story.append(Paragraph(s, S['box']))
    def sp(self, h=0.25): self.story.append(Spacer(1, h * cm))
    def br(self): self.story.append(PageBreak())
    def cap(self, s): self.story.append(Paragraph(s, S['cap']))

    def ul(self, itens):
        self.story.append(ListFlowable([ListItem(Paragraph(i, S['p']), leftIndent=10, value='•') for i in itens],
                                       bulletType='bullet', start='•', leftIndent=12, bulletFontName='DV'))

    def ol(self, itens):
        self.story.append(ListFlowable([ListItem(Paragraph(i, S['p']), leftIndent=12) for i in itens],
                                       bulletType='1', leftIndent=14, bulletFontName='DV', bulletFontSize=9))

    def tab(self, cab, linhas, larg=None, destaque=None, fonte=7.2):
        cs = ParagraphStyle('c2', parent=S['cell'], fontSize=fonte, leading=fonte * 1.22)
        cb = ParagraphStyle('c3', parent=S['cellb'], fontSize=fonte, leading=fonte * 1.22)
        data = [[Paragraph(str(c), cb) for c in cab]] + [[Paragraph(str(c), cs) for c in l] for l in linhas]
        tw = self.doc.width
        t = Table(data, colWidths=[w * tw for w in larg] if larg else None, repeatRows=1)
        st = [('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#12355b')), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
              ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#b8c4d0')),
              ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f4f7fa')]),
              ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
              ('LEFTPADDING', (0, 0), (-1, -1), 3), ('RIGHTPADDING', (0, 0), (-1, -1), 3)]
        for r in (destaque or []):
            st.append(('BACKGROUND', (0, r + 1), (-1, r + 1), colors.HexColor('#fff4d6')))
        t.setStyle(TableStyle(st)); self.story.append(t); self.sp(0.15)

    def img(self, path, largura=1.0, legenda=None):
        w, h = PILImage.open(path).size
        W = self.doc.width * largura
        self.story.append(KeepTogether([Image(path, width=W, height=W * h / w)] + ([Paragraph(legenda, S['cap'])] if legenda else [])))

    def build(self):
        def rodape(c, d):
            c.saveState(); c.setFont('DV', 7.5); c.setFillColor(colors.HexColor('#666666'))
            c.drawString(1.8 * cm, 1.0 * cm, 'Mova (UNAMA): limiar × CNN-LSTM entre bases')
            c.drawRightString(A4[0] - 1.8 * cm, 1.0 * cm, f'pág. {d.page}'); c.restoreState()
        self.doc.build(self.story, onFirstPage=rodape, onLaterPages=rodape)
