import ROOT as r
import array
r.gStyle.SetOptFit()

x  = [-0.22, 0.05, 0.25, 0.35, 0.5, 0.61,0.7,0.85,0.89,0.95]
y  = [1,2.9,5.6,7.4,9,9.6,8.7,6.3,4.5,1]
ex = [.05,.1,.07,.07,.04,.05,.06,.07,.08,.05]
ey = [.8,.7,.6,.5,.4,.4,.5,.6,.7,.8]
xv = array.array('d', x)
yv = array.array('d', y)
exv = array.array('d', ex)
eyv = array.array('d', ey)
myGraph = r.TGraphErrors(len(x),xv,yv,exv,eyv)
c= r.TCanvas('myCanvas')  
myGraph.Draw("ap")
func = r.TF1("func","[0]+[1]*x+[2]*pow(x,2)+[3]*pow(x,3)",-0.3,1.)
func.SetParameter(0,1)
func.SetParameter(1,1)
func.SetParameter(2,1)
func.SetParameter(3,-10)
func.SetLineColor(4)
 
myGraph.Fit(func,"R")
myGraph.SetMaximum(13)
myGraph.GetHistogram().SetXTitle("X-Axis")
myGraph.GetHistogram().SetYTitle("Y-Axis")
c.SaveAs('grapherrors.png')
