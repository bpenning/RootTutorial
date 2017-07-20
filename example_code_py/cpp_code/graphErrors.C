// grapherrors.C
{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  gStyle->SetOptFit();

  const int n = 10;
  float x[n]  = {-0.22, 0.05, 0.25, 0.35, 0.5, 0.61,0.7,0.85,0.89,0.95};
  float y[n]  = {1,2.9,5.6,7.4,9,9.6,8.7,6.3,4.5,1};
  float ex[n] = {.05,.1,.07,.07,.04,.05,.06,.07,.08,.05};
  float ey[n] = {.8,.7,.6,.5,.4,.4,.5,.6,.7,.8};
  
  TGraphErrors *myGraph = new TGraphErrors(n,x,y,ex,ey);
  
  myGraph->Draw("ap");
  TF1 *func = new TF1("func","[0]+[1]*x+[2]*pow(x,2)+[3]*pow(x,3)",-0.3,1.);
  func->SetParameter(0,1);
  func->SetParameter(1,1);
  func->SetParameter(2,1);
  func->SetParameter(3,-10);
  func->SetLineColor(4);
  
  myGraph->Fit(func,"R");
  myGraph->SetMaximum(13);
  myGraph->GetHistogram()->SetXTitle("X-Axis");
  myGraph->GetHistogram()->SetYTitle("Y-Axis");
}
