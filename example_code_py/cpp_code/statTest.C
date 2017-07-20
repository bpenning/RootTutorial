{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  TH1F* myH1 = new TH1F("myHisto","gaussian distribution",100,-5.,5.);
  myH1->FillRandom("gaus",6000);
  TH1F* myH2 = new TH1F("myHisto2","gaussian distribution",100,-5.,5.);
  myH2->FillRandom("gaus",6000);
  myH2->Scale(0.5);
  myH1->SetLineColor(2);
  myH2->SetLineColor(4);
  myH1->Draw("E");
  myH2->Draw("SAME,E");
  myH2->KolmogorovTest(myH1,"DN");
}
