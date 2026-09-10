# latexmk config: use biber (not bibtex) for biblatex
$biber = 'biber';
$pdf_mode = 5;  # xelatex
$pdflatex = 'xelatex -interaction=nonstopmode -file-line-error %O %S';
$xelatex = 'xelatex -interaction=nonstopmode -file-line-error %O %S';
$bibtex_use = 2;  # always use biber for biblatex
