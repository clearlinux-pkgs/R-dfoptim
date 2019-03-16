#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dfoptim
Version  : 2018.2.1
Release  : 15
URL      : https://cran.r-project.org/src/contrib/dfoptim_2018.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dfoptim_2018.2-1.tar.gz
Summary  : Derivative-Free Optimization
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n dfoptim

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523301470

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523301470
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dfoptim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dfoptim
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dfoptim
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library dfoptim|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dfoptim/DESCRIPTION
/usr/lib64/R/library/dfoptim/INDEX
/usr/lib64/R/library/dfoptim/Meta/Rd.rds
/usr/lib64/R/library/dfoptim/Meta/demo.rds
/usr/lib64/R/library/dfoptim/Meta/features.rds
/usr/lib64/R/library/dfoptim/Meta/hsearch.rds
/usr/lib64/R/library/dfoptim/Meta/links.rds
/usr/lib64/R/library/dfoptim/Meta/nsInfo.rds
/usr/lib64/R/library/dfoptim/Meta/package.rds
/usr/lib64/R/library/dfoptim/NAMESPACE
/usr/lib64/R/library/dfoptim/NEWS
/usr/lib64/R/library/dfoptim/R/dfoptim
/usr/lib64/R/library/dfoptim/R/dfoptim.rdb
/usr/lib64/R/library/dfoptim/R/dfoptim.rdx
/usr/lib64/R/library/dfoptim/demo/dfoptim.R
/usr/lib64/R/library/dfoptim/help/AnIndex
/usr/lib64/R/library/dfoptim/help/aliases.rds
/usr/lib64/R/library/dfoptim/help/dfoptim.rdb
/usr/lib64/R/library/dfoptim/help/dfoptim.rdx
/usr/lib64/R/library/dfoptim/help/paths.rds
/usr/lib64/R/library/dfoptim/html/00Index.html
/usr/lib64/R/library/dfoptim/html/R.css
