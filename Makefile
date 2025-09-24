# Makefile for building resume profiles

# List of all profiles (each must have a corresponding .tex file)
PROFILES = general devops backend fullstack web3 full

# Default target: build all PDFs
all: $(patsubst %, %-resume.pdf, $(PROFILES))

# Rule to build a PDF for a specific profile
%-resume.pdf: %.tex
	@echo "Building $@..."
	@latexmk -xelatex -jobname=$* $<

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
