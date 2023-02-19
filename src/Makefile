PKG = StrucTiSM
PREFIX = $(shell pkg-config --variable=prefix gretl)

INP = $(PKG).inp $(PKG)_sample.inp $(PKG)_GUI.inp StateSpace.inp utils.inp special_cases.inp
GFN = $(PKG).gfn
PDF = pdflatex $(PKG).tex

$(PKG).gfn : $(INP) $(PKG).spec
	gretlcli -m $(PKG).inp

$(PKG).zip : $(INP) $(GFN) doc copy_pdf copy_exampled
	echo makepkg $(PKG).zip | gretlcli -b -

copy_exampled :
	cp -r ../examples ./

copy_pdf : ../doc/$(PKG).pdf
	cp -r ../doc ./

install : $(PKG).zip
	echo "install $(PKG).zip --local" | gretlcli -b -

doc : ../doc/$(PKG).tex ../doc/ref.bib
	# this ought to be enough
	cd ../doc; $(PDF); $(PDF); bibtex $(PKG).aux; $(PDF); $(PDF); $(PDF)

tarball : clean
	tar -cvzf ../$(PKG).tar.gz *

clean : 
	rm -rf $(GFN) $(PKG).zip
	rm -rf ./doc ./examples
	rm -rf *~ doc/*~ examples/*~
	rm -rf ../doc/*.aux ../doc/*~ ../doc/*.toc ../doc/*.log  ../doc/*.bbl ../doc/*.bbl ../doc/auto/
	rm -rf session.inp
	touch ../doc/$(PKG).tex
