#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fpdf import FPDF

DATES = ["14/02/22","01/08/22","31/05/23","22/03/24","28/03/24*","14/01/25","06/11/25","18/06/26"]

# (categoria, nome, unidade, min, max, [8 valores], {disp})
CATS = [("hemograma","HEMOGRAMA"),("metabolico","GLICEMIA & METABOLISMO"),("lipidios","PERFIL LIPÍDICO"),
        ("renal","FUNÇÃO RENAL"),("hepatico","FUNÇÃO HEPÁTICA"),("minerais","CÁLCIO & MINERAIS"),
        ("ferro","FERRO"),("vitaminas","VITAMINAS"),("tireoide","TIREOIDE"),("hormonios","HORMÔNIOS"),
        ("inflamacao","INFLAMAÇÃO")]
N=None
M = [
 ("hemograma","Eritrócitos","milhões/µL",3.8,5.0,[4.27,3.51,4.55,4.50,N,4.13,3.61,4.27],{}),
 ("hemograma","Hemoglobina","g/dL",12.0,15.8,[12.8,10.8,13.6,13.8,N,12.3,11.0,12.6],{}),
 ("hemograma","Hematócrito","%",36,46,[38.3,32.2,40.6,40.2,N,36.8,31.9,38.3],{}),
 ("hemograma","VCM","fL",80,100,[89.7,91.7,89.2,89.3,N,89.1,88.4,89.7],{}),
 ("hemograma","HCM","pg",27,32,[30.0,30.8,29.8,30.7,N,29.8,30.5,29.5],{}),
 ("hemograma","CHCM","g/dL",32,36,[33.4,33.5,33.4,34.3,N,33.4,34.5,32.9],{}),
 ("hemograma","RDW","%",11.9,15.5,[12.1,12.1,13.3,12.4,N,12.2,13.2,11.9],{}),
 ("hemograma","Leucócitos","/µL",3900,11100,[6580,11600,6500,5430,N,6040,5660,6040],{}),
 ("hemograma","Neutrófilos (segm.)","/µL",1700,7500,[3550,8170,3445,1710,N,1812,3150,2240],{}),
 ("hemograma","Eosinófilos","/µL",30,500,[190,180,260,270,N,242,210,240],{}),
 ("hemograma","Basófilos","/µL",0,200,[30,50,65,40,N,0,30,50],{}),
 ("hemograma","Linfócitos","/µL",1000,3200,[2350,2410,2340,3030,N,3745,1970,3130],{}),
 ("hemograma","Monócitos","/µL",200,900,[460,790,390,380,N,242,300,380],{}),
 ("hemograma","Plaquetas","/µL",150000,400000,[307000,260000,293000,249000,N,289000,226000,250000],{}),
 ("hemograma","VPM","fL",7.9,12.6,[10.7,10.3,9.0,10.4,N,9.5,10.0,10.3],{}),
 ("metabolico","Glicose","mg/dL",70,99,[72,71,70,73,N,80,78,71],{}),
 ("metabolico","HbA1c","%",N,5.7,[4.8,5.2,5.2,4.9,N,5.0,4.5,4.8],{}),
 ("metabolico","Insulina","µU/mL",2.6,24.9,[8,7.7,2.5,8.2,N,11.7,4.0,4.6],{}),
 ("lipidios","Colesterol total","mg/dL",N,190,[149,237,154,155,N,145,174,182],{}),
 ("lipidios","HDL","mg/dL",40,N,[72,98,83,74,N,70.5,81,95],{}),
 ("lipidios","LDL","mg/dL",N,130,[63,109.2,62,67.9,N,60.8,78.3,77],{}),
 ("lipidios","Triglicérides","mg/dL",N,150,[55,139,30,46,N,48,66,35],{}),
 ("renal","Creatinina","mg/dL",0.52,1.04,[0.57,0.40,0.57,0.70,N,0.72,0.46,0.69],{}),
 ("renal","Ureia","mg/dL",15,43,[18,10,19,31,N,27,14,27],{}),
 ("renal","Ácido úrico","mg/dL",2.5,6.2,[N,2.7,4.20,N,N,N,N,N],{}),
 ("renal","Filtração glom. (TFG)","mL/min",60,N,[N,139,N,120,N,N,132,119],{}),
 ("hepatico","TGO / AST","U/L",N,32,[15,23,18,24,N,12,28,48],{}),
 ("hepatico","TGP / ALT","U/L",N,33,[5,9,5,8,N,5,9,34],{}),
 ("hepatico","Gama-GT","U/L",8,41,[10,10,9,13,N,6,10,13],{6:"<10"}),
 ("hepatico","Albumina","g/dL",3.5,5.2,[4.5,3.4,4.1,4.4,N,N,3.5,N],{}),
 ("minerais","Cálcio (soro)","mg/dL",8.4,10.3,[9.4,8.70,9.0,9.20,N,9.1,8.80,9.40],{}),
 ("minerais","Cálcio iônico","mmol/L",1.11,1.32,[1.23,1.21,1.14,1.17,N,1.17,1.13,1.24],{}),
 ("minerais","Cálcio urina 24h","mg/24h",100,300,[294,341.6,133,N,182,445,189,N],{}),
 ("ferro","Ferro sérico","µg/dL",37,170,[182,77,137,81,N,50.9,111,97],{}),
 ("ferro","Ferritina","ng/mL",15,150,[99,9.8,11.5,49.7,N,22.3,41.4,39.2],{}),
 ("vitaminas","Vitamina D (25-OH)","ng/mL",20,60,[304,287,154.2,208,N,154.2,218,202],{2:">154,2",5:">154,2"}),
 ("vitaminas","Vitamina B12","pg/mL",191,890,[776,489,503,1062,N,499,595,1113],{}),
 ("vitaminas","Ácido fólico","ng/mL",3.89,N,[N,8.20,16.87,10.90,N,10.55,15.70,11.10],{}),
 ("tireoide","TSH","µUI/mL",0.45,4.30,[1.0,1.02,0.90,1.25,N,2.76,0.93,1.37],{}),
 ("tireoide","T4 total","µg/dL",5.1,14.1,[8.4,6.83,9.6,6.84,N,10.2,8.16,6.43],{}),
 ("tireoide","T3 livre","pg/mL",2.0,4.4,[N,2.54,3.02,2.97,N,4.28,2.81,3.16],{}),
 ("tireoide","Anti-TPO","UI/mL",N,34,[34,9,0.40,9.8,N,0.30,N,13.8],{0:"<34",1:"<9,0"}),
 ("hormonios","Cortisol (manhã)","µg/dL",4.8,19.5,[N,27.4,7.40,15.2,N,7.53,30.9,14.8],{}),
 ("hormonios","PTH (paratormônio)","pg/mL",12,65,[14,12.7,26,17.7,N,22,11.4,12.4],{}),
 ("inflamacao","PCR","mg/L",N,5,[2.4,14.1,2.9,1.28,N,0.7,5.64,5.0],{7:"<5,0"}),
 ("inflamacao","VHS","mm",N,20,[12,22,11,5,N,8,16,18],{}),
 ("inflamacao","Homocisteína","µmol/L",N,14,[5,3.30,4.18,6.30,N,5.99,3,4.80],{0:"<5",6:"<3"}),
]

def status(mn,mx,x):
    if x is None: return "na"
    if mx is not None and x>mx: return "high"
    if mn is not None and x<mn: return "low"
    return "ok"

def fmt(x):
    if x is None: return "—"
    if x>=1000: return f"{x:,.0f}".replace(",",".")
    s = f"{x:g}"
    return s.replace(".",",")

def disp(d,i,x):
    if i in d: return d[i]
    return fmt(x)

def reftxt(mn,mx):
    a = fmt(mn) if mn is not None else ""
    b = fmt(mx) if mx is not None else ""
    if mn is not None and mx is not None: return f"{a}-{b}"
    if mx is not None: return f"<= {b}"
    if mn is not None: return f">= {a}"
    return ""

pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_font("D","", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
pdf.add_font("D","B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
pdf.add_page()

# Title
pdf.set_font("D","B",15)
pdf.set_text_color(15,23,42)
pdf.cell(0,8,"Exames laboratoriais — Camila Thaiani da Silva Gules de Lima", ln=1)
pdf.set_font("D","",9)
pdf.set_text_color(90,100,115)
pdf.cell(0,5,"Nasc. 18/10/1995  ·  Médico: Dr. Renato Slomka  ·  8 coletas (fev/2022 → jun/2026), em ordem cronológica", ln=1)
# legend
pdf.set_font("D","",8)
y=pdf.get_y()+1; pdf.set_y(y)
pdf.set_fill_color(219,234,254); pdf.cell(4,4,"",fill=True); pdf.cell(34,4," abaixo da ref. (v)")
pdf.set_fill_color(254,226,226); pdf.cell(4,4,"",fill=True); pdf.cell(34,4," acima da ref. (^)")
pdf.set_fill_color(241,245,249); pdf.cell(4,4,"",fill=True); pdf.cell(28,4," não medido")
pdf.ln(7)

# columns widths
name_w, ref_w = 46, 24
date_w = (277 - name_w - ref_w) / 8.0  # ~25.9 each
row_h = 5.6

def header_row():
    pdf.set_font("D","B",8)
    pdf.set_fill_color(15,118,110); pdf.set_text_color(255,255,255)
    pdf.cell(name_w,row_h+1,"Indicador (unidade)",border=0,fill=True)
    pdf.cell(ref_w,row_h+1,"Referência",border=0,fill=True,align="C")
    for d in DATES:
        pdf.cell(date_w,row_h+1,d,border=0,fill=True,align="C")
    pdf.ln(row_h+1)

header_row()

colmap={"low":(219,234,254),"high":(254,226,226),"ok":(255,255,255),"na":(248,250,252)}
txtmap={"low":(30,64,175),"high":(185,28,28),"ok":(30,41,59),"na":(203,213,225)}

for cid,clabel in CATS:
    # category band
    if pdf.get_y()+row_h+8 > 200:
        pdf.add_page(); header_row()
    pdf.set_font("D","B",8)
    pdf.set_fill_color(224,242,241); pdf.set_text_color(15,118,110)
    pdf.cell(name_w+ref_w+date_w*8,row_h,"  "+clabel,border=0,fill=True,ln=1)
    for (mc,mn_,unit,lo,hi,vals,dd) in M:
        if mc!=cid: continue
        if pdf.get_y()+row_h > 200:
            pdf.add_page(); header_row()
        pdf.set_font("D","",7.5)
        pdf.set_fill_color(241,245,249); pdf.set_text_color(30,41,59)
        label = f"{mn_} ({unit})"
        pdf.cell(name_w,row_h,"  "+label,border="B",fill=True)
        pdf.set_font("D","",7)
        pdf.set_text_color(110,120,135); pdf.set_fill_color(250,250,251)
        pdf.cell(ref_w,row_h,reftxt(lo,hi),border="B",fill=True,align="C")
        pdf.set_font("D","",7.5)
        for i,x in enumerate(vals):
            s=status(lo,hi,x)
            pdf.set_fill_color(*colmap[s]); pdf.set_text_color(*txtmap[s])
            txt=disp(dd,i,x)
            if s=="high": txt+=" ^"
            elif s=="low": txt+=" v"
            pdf.cell(date_w,row_h,txt,border="B",fill=True,align="C")
        pdf.ln(row_h)

# Insights + disclaimer on new page
pdf.add_page()
pdf.set_font("D","B",12); pdf.set_text_color(15,23,42)
pdf.cell(0,8,"Padrões que se destacam", ln=1)
pdf.set_font("D","",9); pdf.set_text_color(40,50,65)
ins = [
 "1. Hipercalciúria recorrente — cálcio na urina 24h no limite/elevado (pico 445 em jan/2025; ref 100-300). Principal motivo do acompanhamento.",
 "2. Vitamina D muito alta (200-304; toxicidade >100) com PTH suprimido — padrão de suplementação em dose alta, possível relação com a calciúria.",
 "3. Deficiência de ferro intermitente — ferritina baixa (9,8 em ago/2022; 11,5 em 2023) com anemia leve (Hb 10,8 e 11,0).",
 "4. Evento inflamatório isolado em ago/2022 — leucócitos 11.600, PCR 14,1, VHS 22, cortisol 27,4 (normalizado depois).",
 "5. Enzimas hepáticas elevadas em jun/2026 (TGO 48, TGP 34) — primeira ocorrência; reavaliar.",
 "6. Sempre bons: glicemia, HbA1c, insulina e perfil lipídico (HDL alto).",
]
for t in ins:
    pdf.multi_cell(0,5.5,t); pdf.ln(0.5)
pdf.ln(3)
pdf.set_font("D","B",9); pdf.cell(0,5,"Outros exames pontuais", ln=1)
pdf.set_font("D","",8.5); pdf.set_text_color(70,80,95)
pdf.multi_cell(0,5,"HOMA-IR 1,4 (fev/2022) sem resistência insulínica · Serotonina 207,2 ng/mL (mai/2023) discretamente alta · "
 "Alumínio 6,2 µg/L (jan/2025) normal · Beta-HCG <5 (jan/2025) não gestante · FAN negativo (ago/2022 e mai/2023) · "
 "T3 reverso 0,25-0,29 ng/mL (2022-2024) · Urina tipo I (nov/2025 e jun/2026) sem alterações relevantes.")
pdf.ln(4)
pdf.set_font("D","",8); pdf.set_text_color(146,64,14)
pdf.set_fill_color(254,243,199)
pdf.multi_cell(0,5,"AVISO: organização dos laudos para visualização — não é diagnóstico nem substitui avaliação médica. "
 "As faixas de referência variam entre laboratórios (Weinmann, Unimed e outros) e algumas unidades foram padronizadas para comparação "
 "(ex.: PCR em mg/L, B12 em pg/mL). * a coleta de 28/03/2024 contém apenas o cálcio urinário 24h. Sempre interprete com o médico.",
 fill=True)

pdf.output("exames-camila/tabela-exames.pdf")
print("PDF gerado: exames-camila/tabela-exames.pdf")
