import ROOT as r
r.gStyle.SetOptStat(0)

e = 0.01
hist = r.TH2D("regions", ";;", 2, 0., 2., 2, 0., 2.)
hist.GetXaxis().SetBinLabel(1, "poor shower shape")
hist.GetXaxis().SetBinLabel(2, "good shower shape")
hist.GetYaxis().SetBinLabel(1, "non-isolated")
hist.GetYaxis().SetBinLabel(2, "isolated")
#hist.LabelsOption("v", "Y")
#hist.LabelsOption("h", "X")
selected_top = r.TLine(1.+e, 2.-e, 2.-e, 2.-e)
selected_top.SetLineWidth(5)
selected_top.SetLineColor(4)
selected_left = r.TLine(1.+e, 1.+e, 1.+e, 2.-e)
selected_left.SetLineWidth(5)
selected_left.SetLineColor(4)
selected_right = r.TLine(2.-e, 1.+e, 2.-e, 2.-e)
selected_right.SetLineWidth(5)
selected_right.SetLineColor(4)
selected_bottom = r.TLine(1.+e, 1.+e, 2.-e, 1.+e)
selected_bottom.SetLineWidth(5)
selected_bottom.SetLineColor(4)
text_selected = r.TLatex(1.3, 1.5, "#color[4]{Selected}")
control_top = r.TLine(1.+e, 1.-e, 2.-e, 1.-e)
control_top.SetLineWidth(5)
control_top.SetLineColor(2)
control_left = r.TLine(1.+e, 0.+e, 1.+e, 1.-e)
control_left.SetLineWidth(5)
control_left.SetLineColor(2)
control_right = r.TLine(2.-e, 0.+e, 2.-e, 1.-e)
control_right.SetLineWidth(5)
control_right.SetLineColor(2)
control_bottom = r.TLine(1.+e, 0.+e, 2.-e, 0.+e)
control_bottom.SetLineWidth(5)
control_bottom.SetLineColor(2)
text_control = r.TLatex(1.3, 0.5, "#color[2]{Control}")
sideband_top = r.TLine(0.+e, 2.-e, 1.-e, 2.-e)
sideband_top.SetLineWidth(5)
sideband_top.SetLineColor(r.kGreen+2)
sideband_left = r.TLine(0.+e, 0.+e, 0.+e, 2.-e)
sideband_left.SetLineWidth(5)
sideband_left.SetLineColor(r.kGreen+2)
sideband_right = r.TLine(1.-e, 0.+e, 1.-e, 2.-e)
sideband_right.SetLineWidth(5)
sideband_right.SetLineColor(r.kGreen+2)
sideband_bottom = r.TLine(0.+e, 0.+e, 1.-e, 0.+e)
sideband_bottom.SetLineWidth(5)
sideband_bottom.SetLineColor(r.kGreen+2)
text_sideband = r.TLatex(0.55, 0.6, "#color[418]{S i d e b a n d}")
text_sideband.SetTextAngle(90.)
c = r.TCanvas("c", "c", 1000, 1000)
hist.Draw()
selected_top.Draw()
selected_left.Draw()
selected_right.Draw()
selected_bottom.Draw()
control_top.Draw()
control_left.Draw()
control_right.Draw()
control_bottom.Draw()
sideband_top.Draw()
sideband_left.Draw()
sideband_right.Draw()
sideband_bottom.Draw()
text_selected.Draw()
text_control.Draw()
text_sideband.Draw()
c.SaveAs("Regions.png")
c.SaveAs("Regions.eps")
c.SaveAs("Regions.pdf")