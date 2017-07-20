{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  gStyle->SetOptFit();
  TH1F* myH1 = new TH1F("myHisto","lin. regression",10,0.,10.);
  TF1* myPol1 = new TF1("myPol1","2*x",0.,10.);
  myH1->FillRandom("myPol1",100);
  myH1->SetMarkerColor(2);  
  myH1->SetMarkerStyle(20);  
  myH1->Fit("pol1");  
  myH1->Draw("E");  
  TVirtualFitter *fitter = TVirtualFitter::GetFitter();
  TMatrixD *matrix = new TMatrixD(2,2,fitter->GetCovarianceMatrix());
  matrix->Print();
}
