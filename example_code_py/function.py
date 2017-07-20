import ROOT as r

myFunc = r.TF1("myFunction","sin(x)/x",0.,1.)
c= r.TCanvas('myCanvas')
myFunc.Draw()
c.SaveAs('function.png')

