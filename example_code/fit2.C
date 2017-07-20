{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  #include "Riostream.h"
  ifstream in;
  in.open("peak.dat");
  Int_t xi;
  Float_t yi;
  Int_t nlines = 0;
  TH1F* _histo = new TH1F("_histo","Peaks", 350, 0., 350 );
  while (1) {
    in >> yi >> xi;
    if (!in.good()) break;
    _histo->SetBinContent( yi, xi );
    nlines++;
  }
  cout<<"found "<<nlines<<" data points"<<endl;
  TF1* fitFunc = new TF1("fitFunc","pol1(0)+gaus(2)",0,300);
  fitFunc->SetParameter(3,175);
  fitFunc->SetParameter(4,20);
  in.close();
   gStyle->SetOptFit();
  _histo->Rebin(3);
  _histo->Fit("fitFunc");
  _histo->Draw("E");
}

