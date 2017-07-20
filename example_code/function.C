{
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  TF1 *myFunc = new TF1("myFunction","sin(x)/x",0.,1.);
  myFunc->Draw();
}
