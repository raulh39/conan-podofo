#include <iostream>
#include "podofo/base/PdfParser.h"

int main() {
    PdfParser parser;
    std::cout << "Podofo: " << parser.GetPdfVersionString() << std::endl;
}
