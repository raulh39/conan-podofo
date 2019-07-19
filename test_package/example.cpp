#include <iostream>
#include <podofo/podofo.h>

int main() {
  using namespace std;
  PoDoFo::PdfStreamedDocument document("test.pdf");
  PoDoFo::PdfPage *pPage = document.CreatePage(
      PoDoFo::PdfPage::CreateStandardPageSize(PoDoFo::ePdfPageSize_A4));
  PoDoFo::PdfPainter painter;
  painter.SetPage(pPage);
  PoDoFo::PdfFont *pFont = document.CreateFont("Arial");
  pFont->SetFontSize(18.0);
  painter.SetFont(pFont);
  painter.DrawText(56.69, pPage->GetPageSize().GetHeight() - 56.69,
                   "Hello World!");
  painter.FinishPage();
  document.Close();
  return 0;
}
