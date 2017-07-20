#execute with: python saveHisto.py

import ROOT as r

myH1 = r.TH1F('myHisto','Distribution from 0 to 1',100,-5.,5.)
file=r.TFile('histo.root','RECREATE')  
myH1.FillRandom('gaus',6000)
myH1.Draw()
myH1.Write()
file.Close()


