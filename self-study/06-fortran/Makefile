FC ?= gfortran
FFLAGS ?= -O2 -Wall -std=f2008

all: calibration_demo

calibration_demo: calibration_mod.o main.o
	$(FC) $(FFLAGS) -o $@ $^

calibration_mod.o: calibration_mod.f90
	$(FC) $(FFLAGS) -c $<

main.o: main.f90 calibration_mod.o
	$(FC) $(FFLAGS) -c main.f90

clean:
	rm -f *.o *.mod calibration_demo

.PHONY: all clean
