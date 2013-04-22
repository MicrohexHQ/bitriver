

all : bitriver

bitriver : bitriver.py cpp
	python2 bitriver.pycpp

cpp :
	cpp -C -nostdinc bitriver.py > bitriver.pycpp; exit 0

clean :
	rm -f bitriver.pycpp
