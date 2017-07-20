{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  #include "Riostream.h"
  ifstream in;
  in.open("peaks.dat");
  Float_t xi;
  Int_t nlines = 0;
  TFile* _file = new TFile("readData.root","RECREATE");
  TH1F* _histo = new TH1F("_histo","Peaks", 1250, 0., 1250 );

  while (1) {
   in >> xi;
    if (!in.good()) break;
    _histo->SetBinContent( nlines, xi );
    nlines++;
  }
  cout<<"found "<<nlines<<" data points"<<endl;
  in.close();
  _histo->Draw();
  _file->Write();
}

