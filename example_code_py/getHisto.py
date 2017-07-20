import ROOT as r

file = r.TFile('histo.root','OPEN')  
myH1 = file.Get('myHisto')
c= r.TCanvas('myCanvas')
myH1.Draw()
c.SaveAs('getHisto.png')

