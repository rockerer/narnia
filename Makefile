doc:	README.md
	pandoc -t pdf README.md -o readme.pdf

clean:
	rm -f README.pdf
