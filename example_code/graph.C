// graph.C
{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  gStyle->SetOptFit();
  
  const int n = 10;
  float x[n]  = {-0.22, 0.05, 0.25, 0.35, 0.5, 0.61,0.7,0.85,0.89,0.95};
  float y[n]  = {1,2.9,5.6,7.4,9,9.6,8.7,6.3,4.5,1};
  
  TGraph *myGraph = new TGraph(n,x,y);
  myGraph->SetTitle("myGraph");
  myGraph->SetMarkerColor(2);
  myGraph->SetMarkerStyle(20);
  myGraph->SetMarkerSize(0.7);
  myGraph->Draw("apl");
}
