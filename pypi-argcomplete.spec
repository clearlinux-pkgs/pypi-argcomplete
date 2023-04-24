#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
# Source0 file verified with key 0x8AFAFCD242818A52 (kislyuk@gmail.com)
#
Name     : pypi-argcomplete
Version  : 3.0.8
Release  : 106
URL      : https://files.pythonhosted.org/packages/42/cd/fdb872d826b76b65b23147e83b1ca4c033445bbff59f8836a118657dd050/argcomplete-3.0.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/cd/fdb872d826b76b65b23147e83b1ca4c033445bbff59f8836a118657dd050/argcomplete-3.0.8.tar.gz
Source1  : https://files.pythonhosted.org/packages/42/cd/fdb872d826b76b65b23147e83b1ca4c033445bbff59f8836a118657dd050/argcomplete-3.0.8.tar.gz.asc
Summary  : Bash tab completion for argparse
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-argcomplete-bin = %{version}-%{release}
Requires: pypi-argcomplete-license = %{version}-%{release}
Requires: pypi-argcomplete-python = %{version}-%{release}
Requires: pypi-argcomplete-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi-pexpect
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
argcomplete - Bash/zsh tab completion for argparse
==================================================
*Tab complete all the things!*

%package bin
Summary: bin components for the pypi-argcomplete package.
Group: Binaries
Requires: pypi-argcomplete-license = %{version}-%{release}

%description bin
bin components for the pypi-argcomplete package.


%package license
Summary: license components for the pypi-argcomplete package.
Group: Default

%description license
license components for the pypi-argcomplete package.


%package python
Summary: python components for the pypi-argcomplete package.
Group: Default
Requires: pypi-argcomplete-python3 = %{version}-%{release}

%description python
python components for the pypi-argcomplete package.


%package python3
Summary: python3 components for the pypi-argcomplete package.
Group: Default
Requires: python3-core
Provides: pypi(argcomplete)

%description python3
python3 components for the pypi-argcomplete package.


%prep
%setup -q -n argcomplete-3.0.8
cd %{_builddir}/argcomplete-3.0.8
pushd ..
cp -a argcomplete-3.0.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682349850
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose test/test.py || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-argcomplete
cp %{_builddir}/argcomplete-%{version}/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-argcomplete/598f87f072f66e2269dd6919292b2934dbb20492 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/activate-global-python-argcomplete
/usr/bin/python-argcomplete-check-easy-install-script
/usr/bin/register-python-argcomplete

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-argcomplete/598f87f072f66e2269dd6919292b2934dbb20492

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
