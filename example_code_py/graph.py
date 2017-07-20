import ROOT as r
import array


r.gStyle.SetOptFit()

x  = [-0.22, 0.05, 0.25, 0.35, 0.5, 0.61,0.7,0.85,0.89,0.95]
y  = [1,2.9,5.6,7.4,9,9.6,8.7,6.3,4.5,1]
xv = array.array('d', x)
yv = array.array('d', y)
myGraph = r.TGraph(len(x), xv, yv)
myGraph.SetTitle('myGraph')
myGraph.SetMarkerColor(2)
myGraph.SetMarkerStyle(20)
myGraph.SetMarkerSize(0.7)
c= r.TCanvas('myCanvas')
myGraph.Draw('apl')
c.SaveAs('graph.png')


  
  
