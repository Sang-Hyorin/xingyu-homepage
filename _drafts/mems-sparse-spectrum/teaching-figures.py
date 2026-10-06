from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent
# Requires matplotlib, numpy, Pillow; outputs remain within this draft.
# Set these font paths for your platform if regenerating outside Windows.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.font_manager import FontProperties
from PIL import Image
import json

OUT = ROOT / 'assets'
import os
QA = Path(os.environ.get('MEMS_FIGURE_QA_DIR', r'D:\CodexGenerated\temp\mems-figure-qa'))
QA.mkdir(exist_ok=True)
cn = FontProperties(fname=r'C:\Windows\Fonts\msyh.ttc')
plt.rcParams.update({'font.family':'Arial','font.size':12,'axes.labelweight':'bold',
                     'axes.linewidth':1.1,'xtick.direction':'in','ytick.direction':'in',
                     'savefig.facecolor':'white','figure.facecolor':'white'})
blue, orange, purple, grey = '#356c91', '#b36b23', '#735272', '#59636d'
audit = []

def save(fig, name):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    bounds = fig.bbox
    for item in fig.findobj(matplotlib.text.Text):
        if item.get_visible() and item.get_text():
            b = item.get_window_extent(renderer)
            assert b.x0 >= -1 and b.y0 >= -1 and b.x1 <= bounds.x1 + 1 and b.y1 <= bounds.y1 + 1, (name,item.get_text(),b)
    fig.savefig(OUT / name, dpi=200)
    with Image.open(OUT / name) as image:
        height = round(image.height * 780 / image.width)
        preview = image.convert('RGB').resize((780, height), Image.Resampling.LANCZOS)
        preview.save(QA / name)
    audit.append({'file':name,'preview_width':780,'preview_height':height,'text_bounds':'pass'})
    plt.close(fig)

fig, ax = plt.subplots(figsize=(7.8,4.8))
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
ax.set(xlim=(0,780),ylim=(0,480)); ax.axis('off')
def text(x,y,label,size=12,color='#23313d',ha='center'):
    ax.text(x,y,label,fontproperties=cn,fontsize=size,color=color,ha=ha,va='center')
def box(x,y,w,h,label,color=grey):
    ax.add_patch(Rectangle((x,y),w,h,fc='white',ec=color,lw=1.5))
    text(x+w/2,y+h/2,label)
def arrow(a,b,color=grey):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,color=color,lw=1.6))
box(30,310,120,75,'正弦信号源',blue)
box(230,295,210,110,'定向耦合器 / 电桥',blue)
box(585,295,160,110,'SAW 谐振器',grey)
arrow((155,355),(225,355),blue)
arrow((445,365),(580,365),blue); text(514,392,'入射波 $a_1$',color=blue)
arrow((580,325),(445,325),orange); text(514,297,'反射波 $b_1$',color=orange)
ax.plot([557,557],[275,425],color=grey,ls='--',lw=1)
text(560,447,'校准参考面',size=11)
box(100,145,155,65,'参考接收机',blue)
box(340,145,155,65,'测量接收机',orange)
arrow((280,290),(180,215),blue); arrow((395,290),(420,215),orange)
text(166,251,'取样 $a_1$',size=11,color=blue); text(446,248,'取样 $b_1$',size=11,color=orange)
arrow((180,140),(260,125),blue); arrow((420,140),(360,125),orange)
text(297,109,'比较幅度与相位 → 校准后的 $S_{11}$ = $b_1$ / $a_1$',size=13)
text(390,44,'一个频点得到一个复数；改变频率，重复测量。',size=12)
save(fig,'teaching-vna-measurement.png')

# Constructed BVD equivalent circuit; no fitted or measured device data.
fr = 2.49e9
Cm, C0, Rm = .1e-12, 2e-12, .25
Lm = 1/((2*np.pi*fr)**2*Cm)
def admittance(f):
    w=2*np.pi*f
    return 1j*w*C0 + 1/(Rm+1j*(w*Lm-1/(w*Cm)))
f = np.linspace(2.4e9,2.6e9,20001)
fs = np.linspace(2.4e9,2.6e9,16)
fp = fr*np.sqrt(1+Cm/C0)
fig,ax=plt.subplots(figsize=(7.8,4.6))
fig.subplots_adjust(left=.12,right=.97,bottom=.18,top=.90)
ax.semilogy(f/1e9, np.abs(admittance(f))*1e3,color=grey,lw=1.6,label='Dense toy-model curve')
ax.semilogy(fs/1e9,np.abs(admittance(fs))*1e3,'o',color=blue,ms=5,label='16 sampled values')
ax.set(xlim=(2.4,2.6),ylim=(.05,9000),xlabel='Frequency (GHz)',ylabel='Admittance magnitude (mS)')
ax.legend(loc='upper right',fontsize=10,frameon=False)
ax.annotate('Resonance',xy=(fr/1e9,np.abs(admittance(fr))*1e3),xytext=(2.425,2200),
            arrowprops={'arrowstyle':'->','color':orange},color=orange,fontsize=11)
ax.annotate('Antiresonance',xy=(fp/1e9,np.abs(admittance(fp))*1e3),xytext=(2.570,.65),
            arrowprops={'arrowstyle':'->','color':orange},color=orange,fontsize=11,ha='center')
ax.tick_params(which='both',top=True,right=True)
fig.text(.12,.97,'Constructed example · log vertical axis',fontsize=10,color=grey,va='top')
save(fig,'teaching-sparse-sweep.png')

phase=np.linspace(0,2*np.pi,601)
fig,axes=plt.subplots(2,1,figsize=(7.8,5.4),sharex=True)
fig.subplots_adjust(left=.12,right=.97,bottom=.14,top=.89,hspace=.45)
for ax,phi,label in zip(axes,[0,np.pi/2],['(a) In phase: G = 1 mS, B = 0','(b) Current leads by 90°: G = 0, B = 1 mS']):
    ax.plot(phase/(2*np.pi),np.cos(phase),color=blue,lw=1.8,label='Voltage / 1 V')
    ax.plot(phase/(2*np.pi),np.cos(phase+phi),color=purple,lw=1.8,ls='--',label='Current / 1 mA')
    ax.set(ylim=(-1.25,1.25),yticks=[-1,0,1],ylabel='Normalized value')
    ax.set_title(label,fontsize=11,loc='left',pad=8)
    ax.tick_params(top=True,right=True)
    ax.axhline(0,color='#d9dfe3',lw=.6,zorder=0)
axes[0].legend(loc='upper right',fontsize=10,frameon=False,bbox_to_anchor=(1,1.30),ncol=2)
axes[1].set(xlabel='Time / period',xlim=(0,1),xticks=[0,.25,.5,.75,1])
save(fig,'teaching-complex-phase.png')
(QA/'audit.json').write_text(json.dumps({'figures':audit,'BVD_parameters':{'Rm_ohm':Rm,'Lm_H':Lm,'Cm_F':Cm,'C0_F':C0,'fr_Hz':fr,'lossless_fp_Hz':fp}},indent=2),encoding='utf-8')
print(json.dumps(audit))


