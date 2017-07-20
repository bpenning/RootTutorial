
{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  TH1F* myH1 = new TH1F("myHisto","Distribution from 0 to 1",100,-5.,5.);
  TFile* _file=new TFile("histo.root","RECREATE");  
  myH1->FillRandom("gaus",6000);
  myH1->Draw();
  myH1->Write();
  _file->Close();
}
