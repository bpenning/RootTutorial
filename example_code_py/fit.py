#execute with python -i histogram2.py

import ROOT as r


myH1 = r.TH1F('myHisto','gaussian distribution 1',100,-5.,5.)
myGaus = r.TF1('myGaus','gaus',-5,5)
myH1.FillRandom('gaus',6000)
myH1.SetMarkerColor(2)  
myH1.SetMarkerStyle(20)  
myH1.Fit('myGaus')  
c= r.TCanvas('myCanvas')
myH1.Draw('E')  
c.SaveAs('fit.png')
print ' --------------------------------' 
print ' chi2/dof: ' + str( myGaus.GetChisquare()/myGaus.GetNDF() )
print ' mean: ' + str( myGaus.GetParameter(1) ) +'+/-' + str( myGaus.GetParError(1) )
print ' width: ' + str( myGaus.GetParameter(2) ) + '+/- ' + str(myGaus.GetParError(2) )
