import ROOT as r

nlines=0
histo = r.TH1F('histo','Peaks', 350, 0., 350 )
c= r.TCanvas('myCanvas')

for line in open('peak.dat'):
    nlines=nlines+1
    elems = line.split()
    histo.SetBinContent( int(elems[0]), int(elems[1]) )

print 'found '+str(nlines)+' data points'
fitFunc = r.TF1('fitFunc','pol1(0)+gaus(2)',0,300)
fitFunc.SetParameter(3,175)
fitFunc.SetParameter(4,20)

r.gStyle.SetOptFit()
histo.Rebin(3)
histo.Fit('fitFunc')
histo.Draw('E')
c.SaveAs('fit2.png')
