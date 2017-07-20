#execute with python -i histogram2.py

import ROOT as r

myH1 = r.TH1F('myHisto','Distribution from 0 to 1',100,-5.,5.)
myH1.FillRandom('gaus',6000)
myH2 = r.TH1F('myHisto2','Distribution from 0 to 1',100,0.,10.)
f1=r.TF1('f1','2*x',0,10)
myH2.FillRandom('f1',6000)
c= r.TCanvas('myCanvas')
c.Divide(1,2)
c.cd(1)
myH1.Draw()  
c.cd(2)  
myH2.Draw()  
c.SaveAs('histogram2.png')
