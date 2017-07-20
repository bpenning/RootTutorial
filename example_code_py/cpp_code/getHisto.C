{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  TFile* _file=new TFile("histo.root","OPEN");  
  TH1F* _myH1 = (TH1F*)_file->Get("myHisto");
  _myH1->Draw();
}
