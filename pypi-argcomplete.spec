#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8AFAFCD242818A52 (kislyuk@gmail.com)
#
Name     : pypi-argcomplete
Version  : 2.0.0
Release  : 85
URL      : https://files.pythonhosted.org/packages/05/f8/67851ae4fe5396ba6868c5d84219b81ea6a5d53991a6853616095c30adc0/argcomplete-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/f8/67851ae4fe5396ba6868c5d84219b81ea6a5d53991a6853616095c30adc0/argcomplete-2.0.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/05/f8/67851ae4fe5396ba6868c5d84219b81ea6a5d53991a6853616095c30adc0/argcomplete-2.0.0.tar.gz.asc
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

%description
argcomplete - Bash tab completion for argparse
==============================================
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
%setup -q -n argcomplete-2.0.0
cd %{_builddir}/argcomplete-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650510899
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose test/test.py || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-argcomplete
cp %{_builddir}/argcomplete-2.0.0/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-argcomplete/598f87f072f66e2269dd6919292b2934dbb20492
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/activate-global-python-argcomplete
/usr/bin/python-argcomplete-check-easy-install-script
/usr/bin/python-argcomplete-tcsh
/usr/bin/register-python-argcomplete

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-argcomplete/598f87f072f66e2269dd6919292b2934dbb20492

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
