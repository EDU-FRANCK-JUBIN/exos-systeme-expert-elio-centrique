# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:07:18 2019

@author: delan
"""
from pyDatalog import pyDatalog

pyDatalog.clear()

pyDatalog.load("""
    P01(X) <=G001(X) & G002(X) & G003(X) & G004(X)
    P02(X) <=G001(X) & G002(X) & G005(X) & G006(X)
    P03(X) <=G007(X) & G008(X)
    P04(X) <=G009(X) & G0010(X) & G0011(X) & G0012(X)
    P05(X) <=G0013(X) & G0014(X) & G0015(X) & G0016(X)
    P06(X) <=G0010(X) & G0015(X) & G0016(X) & G0017(X) & G0018(X) & G0019(X)
    P07(X) <=G0010(X) & G0019(X) & G0020(X) & G0021(X)
    P08(X) <=G001(X) & G0010(X) & G0019(X) & G0022(X)& G0023(X)
    
    blepharite(X) <= P01(X)
    orgelet_de_prevention(X) <= P02(X)
    
   
    G001(X) <= paupiere_rouge(X) 
    G002(X) <= paupiere_enflee(X) 
    G003(X) <= douleur_et_demangeaison_oculaire(X)
    G004(X) <= salete_oculaire_collante(X)
    
""")

pyDatalog.assert_fact('paupiere_rouge', 'fritz')
pyDatalog.assert_fact('paupiere_enflee', 'fritz')
pyDatalog.assert_fact('douleur_et_demangeaison_oculaire', 'fritz')
pyDatalog.assert_fact('salete_oculaire_collante', 'fritz')

print(pyDatalog.ask('salete_oculaire_collante(X)'))