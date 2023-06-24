#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Günlük Kalori Hesaplama Makinesi
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Günlük Kalori Hesaplama Makinesi")
        grid = QGridLayout()
        #Kolon 1
        grid.addWidget(QLabel("Kişisel Bilgileriniz"),0,0)
        grid.addWidget(QLabel("Yaşınız:"),1,0)
        grid.addWidget(QLabel("Boyunuz(cm):"),2,0)
        grid.addWidget(QLabel("Kilonuz(kg):"),3,0)
        grid.addWidget(QLabel("Cinsiyetiniz:"),4,0)
        self.yazi_alani = QLabel("")
        grid.addWidget(self.yazi_alani,8,5)
        
        self.yas = QLineEdit()
        self.boy = QLineEdit()
        self.kilo = QLineEdit()
        grid.addWidget(self.yas,1,1,1,2)
        grid.addWidget(self.boy,2,1,1,2)
        grid.addWidget(self.kilo,3,1,1,2)
        
        self.cinsiyet = QButtonGroup()
        self.erkek = QRadioButton("Erkek")
        self.kadin = QRadioButton("Kadın")
        self.cinsiyet.addButton(self.erkek)
        self.cinsiyet.addButton(self.kadin)
        grid.addWidget(self.erkek,4,1)
        grid.addWidget(self.kadin,4,2)
        
        self.hesapla_butonu = QPushButton("Hesapla")
        self.hesapla_butonu.clicked.connect(lambda: self.hesapla(self.erkek.isChecked(),self.kadin.isChecked(),
                                                                 self.buton1.isChecked(),self.buton2.isChecked(),
                                                                 self.buton3.isChecked(),self.buton4.isChecked(),
                                                                 self.buton5.isChecked()))
        grid.addWidget(self.hesapla_butonu,7,5,1,2)
        
        #Kolon 2
        grid.addWidget(QLabel("Gün içi hareketlilik seviyeniz"),0,5)
        self.buton1 = QRadioButton("Sedanter (Hareket etmiyorum veya çok az hareket ediyorum.)")
        self.buton2 = QRadioButton("Az hareketli (Hafif hareketli bir yaşam / Haftada 1-3 gün egzersiz yapıyorum.)")
        self.buton3 = QRadioButton("Orta derece hareketli (Hareketli bir yaşam / Haftada 3-5 gün egzersiz yapıyorum.)")
        self.buton4 = QRadioButton("Çok hareketli (Çok hareketli bir yaşam / Haftada 6-7 gün egzersiz yapıyorum.)")
        self.buton5 = QRadioButton("Aşırı hareketli (Profesyonel sporcu, atlet seviyesi.)")
        
        grid.addWidget(self.buton1,1,5)
        grid.addWidget(self.buton2,2,5)
        grid.addWidget(self.buton3,3,5)
        grid.addWidget(self.buton4,4,5)
        grid.addWidget(self.buton5,5,5)
        
        #Horizontal Box Layout ve Vertical Box Layout
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(grid)
        h_box.addStretch()
        
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        
        
        self.resize(400,400)
        self.setLayout(v_box)
        self.show()
        
    def hesapla(self,erkek,kadin,buton1,buton2,buton3,buton4,buton5):
        cm = 0
        try: cm = int(self.boy.text())
        except: pass
        
        yil = 0
        try: yil = int(self.yas.text())
        except: pass
        
        kutle = 0
        try: kutle = int(self.kilo.text())
        except: pass
        
        bpmErkek = 66.5+(13.75*kutle)+(5*cm)-(6.77*yil)
        bpmKadin = 655.1+(9.56*kutle)+(1.85*cm)-(4.67*yil)
        
        if erkek and buton1:
            sonuc = bpmErkek*1.2
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif erkek and buton2:
            sonuc = bpmErkek*1.3
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif erkek and buton3:
            sonuc = bpmErkek*1.4
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif erkek and buton4:
            sonuc = bpmErkek*1.5
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif erkek and buton5:
            sonuc = bpmErkek*1.6
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
            
        bmhKadin = 655.1 + (9.56*kutle) + (1.85*cm) - (4.67*yil)
        if kadin and buton1:
            sonuc = bpmKadin*1.2
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif kadin and buton2:
            sonuc = bpmKadin*1.3
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif kadin and buton3:
            sonuc = bpmKadin*1.4
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif kadin and buton4:
            sonuc = bpmKadin*1.5
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
        elif kadin and buton5:
            sonuc = bpmKadin*1.6
            self.yazi_alani.setText("Günlük kalori ihtiyacınız {} Kcal'dir.".format(sonuc))
uygulama = QApplication(sys.argv)
pencere = pencere()
sys.exit(uygulama.exec_())


# In[ ]:





# In[ ]:




