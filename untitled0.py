import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Jensen_Model_3D import Jensen_Calc
from Jensen_Model_3D2 import Jensen_Calc2

u = 8.1
rnot = 20
alpha = 0.1
theta = np.linspace(-20,20,41)
downwind = np.linspace(120, 320, 41)


Model = Jensen_Calc(alpha,downwind,rnot,u,theta)
Model2 = Jensen_Calc2(alpha,downwind,rnot,u,theta)
Cos6 = pd.read_excel (r'C:\Users\Owner\Documents\495R\Digitizer Data.xlsx', 'Cos 6') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
Cos6 = np.asarray(Cos6)

Cos10 = pd.read_excel (r'C:\Users\Owner\Documents\495R\Digitizer Data.xlsx', 'Cos 10') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
Cos10 = np.asarray(Cos10)

Cos16 = pd.read_excel (r'C:\Users\Owner\Documents\495R\Digitizer Data.xlsx', 'Cos 16') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
Cos16 = np.asarray(Cos16)

A6 = pd.read_excel (r'C:\Users\Owner\Documents\495R\Digitizer Data.xlsx', 'TH 6') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
A6 = np.asarray(A6)

TH10 = pd.read_excel (r'C:\Users\Owner\Documents\495R\Digitizer Data.xlsx', 'TH 10') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
TH10 = np.asarray(TH10)

TH16 = pd.read_excel (r'C:\Users\Owner\Documents\495R\Digitizer Data.xlsx', 'TH 16') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
TH16 = np.asarray(TH16)




fig, axes = plt.subplots(nrows=4, ncols=4)
fig.tight_layout()



ax1 = plt.subplot(321)
plt.title("Top Hat at x/r0 = 6")
plt.plot(A6[:,0],A6[:,1])
plt.plot(theta,Model2[0,:,20]/u)
plt.xlabel('\u0394 \u03F4 Degrees')
plt.ylabel('u/v')
plt.setp(ax1.get_xticklabels(), visible=False)
#plt.legend({"Jensen Paper", "My Model"}, frameon = False)
ax2 = plt.subplot(323, sharex = ax1, sharey = ax1)
plt.title("Top Hat at x/r0 = 10")
plt.plot(TH10[:,0],TH10[:,1])
plt.plot(theta,Model2[16,:,20]/u)
plt.xlabel('\u0394 \u03F4 Degrees')
plt.ylabel('u/v')
plt.setp(ax2.get_xticklabels(), visible=False)
#plt.legend({"Jensen Paper", "My Model"}, frameon = False)
ax3 = plt.subplot(325, sharex = ax1, sharey = ax1)
plt.title("Top Hat at x/r0 = 16")
plt.plot(TH16[:,0],TH16[:,1])
plt.plot(theta,Model2[40,:,20]/u)
plt.xlabel('\u0394 \u03F4 Degrees')
plt.ylabel('u/v')

#plt.legend({"Jensen Paper", "My Model"}, frameon = False)
ax4 = plt.subplot(322, sharex = ax1, sharey = ax1)
plt.title("Cosine at x/r0 = 6")
plt.plot(Cos6[:,0],Cos6[:,1])
plt.plot(theta,Model[0,:,20]/u)
plt.xlabel('\u0394 \u03F4 Degrees')
plt.ylabel('u/v')
plt.setp(ax4.get_xticklabels(), visible=False)
#plt.legend({"Jensen Paper", "My Model"}, frameon = False)
ax5 = plt.subplot(324, sharex = ax1, sharey = ax1)
plt.title("Cosine at x/r0 = 10")
plt.plot(Cos10[:,0], Cos10[:,1])
plt.plot(theta,Model[16,:,20]/u)
plt.xlabel('\u0394 \u03F4 Degrees')
plt.ylabel('u/v')
plt.setp(ax5.get_xticklabels(), visible=False)
#plt.legend({"Jensen Paper", "My Model"}, frameon = False)
ax6 = plt.subplot(326, sharex = ax1, sharey = ax1)
plt.title("Cosine at x/r0 = 16")
plt.plot(Cos16[:,0],Cos16[:,1])
plt.plot(theta,Model[40,:,20]/u)
plt.xlabel('\u0394 \u03F4 Degrees')
plt.ylabel('u/v')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.legend({"Jensen Paper", "My Model"}, frameon = False, bbox_to_anchor=(-1.1,-.7))

fig.savefig('full_figure.png')

plt.show()
plt.savefig('Plots.PNG')
#subplot()