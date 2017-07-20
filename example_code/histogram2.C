{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  TH1F* myH1 = new TH1F("myHisto","Distribution from 0 to 1",100,-5.,5.);
  myH1->FillRandom("gaus",6000);
  TH1F* myH2 = new TH1F("myHisto2","Distribution from 0 to 1",100,0.,10.);
  TF1* f1=new TF1("f1","2*x",0,10);
  myH2->FillRandom("f1",6000);
  TCanvas* c1=new TCanvas("myCanvas");
  c1->Divide(1,2);
  c1->cd(1);
  myH1->Draw();  
  c1->cd(2);  
  myH2->Draw();  
}
