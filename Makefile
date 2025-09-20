# Makefile for building resume profiles

# List of all profiles
PROFILES = general devops backend fullstack web3 full

# Default target
all: $(patsubst %, %-resume.pdf, $(PROFILES))

# Rule to build a PDF for a specific profile
%-resume.pdf: main.tex
	@echo "Building $@..."
	@cp main.tex main.tmp.tex
	@sed -i 's/^\\input{profiles\/.*}/%&/' main.tmp.tex
	@sed -i 's/^%\\s*\\input{profiles\/$(patsubst %-resume.pdf, %, $@)}/\\input{profiles\/$(patsubst %-resume.pdf, %, $@)}/' main.tmp.tex
	@latexmk -xelatex -jobname=$(patsubst %.pdf, %, $@) main.tmp.tex
	@rm main.tmp.tex

# Rule to build a specific profile by name (e.g., make general)
.PHONY: $(PROFILES)
$(PROFILES):
	@$(MAKE) $@-resume.pdf

# Clean up build files
clean:
	@latexmk -C
	@rm -f *-resume.pdf

# Phony targets
.PHONY: all clean
