import ROOT as r

r.gStyle.SetOptFit()

myH1 = r.TH1F('myHisto','lin. regression',10,0.,10.)
myPol1 = r.TF1('myPol1','2*x',0.,10.)
myH1.FillRandom('myPol1',100)
myH1.SetMarkerColor(2)  
myH1.SetMarkerStyle(20)  
myH1.Fit('pol1')  
c= r.TCanvas('myCanvas')
myH1.Draw('E')
c.SaveAs('linRegression.png')

fitter = r.TVirtualFitter.GetFitter()
matrix = r.TMatrixD(2,2, fitter.GetCovarianceMatrix())
matrix.Print()

