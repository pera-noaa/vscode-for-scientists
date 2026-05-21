# latexmk config — runs pdflatex + bibtex + pdflatex as many times as needed.
$pdf_mode = 1;                  # build PDF (1=pdflatex, 4=lualatex, 5=xelatex)
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
$bibtex_use = 2;                # always run bibtex if a .bib file is referenced
$out_dir = 'build';             # keep aux files out of the source dir
$clean_ext = 'synctex.gz';      # cleanup extensions
