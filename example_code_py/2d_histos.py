import ROOT as r

c= r.TCanvas('c1', 'multiple plots', 800, 800)
c.Divide(2,2)
h2 = r.TH2F('h2','Energy vs Momentum',20,-5.,5.,20,-5.,5.)
xygaus = r.TF2("xygaus","xygaus",0,10,0,10)
xygaus.SetParameters(1,0,2,0,2)  #amplitude, meanx,sigmax,meany,sigmay
h2.FillRandom('xygaus',10000)
h2.GetXaxis().SetTitle('Energy E (GeV)')
h2.GetYaxis().SetTitle('Momentum p (GeV)')
h2.GetZaxis().SetTitle('Events')
f2= r.TF2('func2','sin(x)*sin(y)/(x*y)',-10.,10.,-10.,10.)
c.cd(1)
h2.Draw('LEGO2')
c.cd(2)
h2.Draw('COL')
c.cd(3)
f2.Draw('SURF1')
c.cd(3)
f2.Draw('SURF1')
c.cd(4)
f2.Draw('COLZ')
c.SaveAs('2d_histos.png')


  
  
