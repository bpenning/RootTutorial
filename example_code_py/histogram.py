import ROOT as r

myH1 = r.TH1F('myHisto', 'Distribution from 0 to 1',10,0.,1.)
myH1.Fill(0.37)
myH1.Fill(0.78)
myH1.Fill(0.51)

c= r.TCanvas('myCanvas')
myH1.Draw()
c.SaveAs('histogram.png')
