import ROOT as r

nlines=0
histo = r.TH1F('_histo','Peaks', 1250, 0., 1250 )
c = r.TCanvas('myCanvas')

for line in open('peaks.dat'):
    nlines=nlines+1
    elems = line.split()
    histo.SetBinContent( nlines, int(elems[0]) )

print 'found '+str(nlines)+' data points'
histo.Draw()
c.SaveAs('readFile.png')

