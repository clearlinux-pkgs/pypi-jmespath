#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jmespath
Version  : 1.0.0
Release  : 63
URL      : https://files.pythonhosted.org/packages/06/7e/44686b986ef9ca6069db224651baaa8300b93af2a085a5b135997bf659b3/jmespath-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/7e/44686b986ef9ca6069db224651baaa8300b93af2a085a5b135997bf659b3/jmespath-1.0.0.tar.gz
Summary  : JSON Matching Expressions
Group    : Development/Tools
License  : MIT
Requires: pypi-jmespath-bin = %{version}-%{release}
Requires: pypi-jmespath-license = %{version}-%{release}
Requires: pypi-jmespath-python = %{version}-%{release}
Requires: pypi-jmespath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
========

%package bin
Summary: bin components for the pypi-jmespath package.
Group: Binaries
Requires: pypi-jmespath-license = %{version}-%{release}

%description bin
bin components for the pypi-jmespath package.


%package license
Summary: license components for the pypi-jmespath package.
Group: Default

%description license
license components for the pypi-jmespath package.


%package python
Summary: python components for the pypi-jmespath package.
Group: Default
Requires: pypi-jmespath-python3 = %{version}-%{release}

%description python
python components for the pypi-jmespath package.


%package python3
Summary: python3 components for the pypi-jmespath package.
Group: Default
Requires: python3-core
Provides: pypi(jmespath)

%description python3
python3 components for the pypi-jmespath package.


%prep
%setup -q -n jmespath-1.0.0
cd %{_builddir}/jmespath-1.0.0
pushd ..
cp -a jmespath-1.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653339019
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jmespath
cp %{_builddir}/jmespath-1.0.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jmespath/c012ed6967c9b5f4a93271c9b3132bcbd76320e0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jp.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jmespath/c012ed6967c9b5f4a93271c9b3132bcbd76320e0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
