Name:       hawaii-icon-theme
Summary:    Icon theme for Hawaii desktop environment
Version:    0.2.0
Release:    1
License:    CC-BY-SA and GPLv2 and LGPLv2
Source0:    http://sourceforge.net/projects/mauios/files/hawaii/hawaii-icon-themes/hawaii-icon-themes-%{version}.tar.gz
Requires(post): /bin/touch
Requires(post): %{_bindir}/gtk-update-icon-cache
BuildRequires:  cmake


%description
This is an icon-theme for Hawaii desktop environment.


%prep
%setup -q


%build
cd upstream
%cmake .  \
    -DCMAKE_INSTALL_PREFIX=/usr
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
cd upstream
%make_install


%post
for dir in elegant hawaii; do
    /bin/touch --no-create %{_datadir}/icons/${dir} || :
done


%posttrans
for dir in elegant hawaii; do
  %{_bindir}/gtk-update-icon-cache \
    --quiet %{_datadir}/icons/${dir} 2> /dev/null|| :
done


%postun
for dir in elegant hawaii; do
  /bin/touch --no-create %{_datadir}/icons/${dir} || :
  %{_bindir}/gtk-update-icon-cache \
    --quiet %{_datadir}/icons/${dir} 2> /dev/null|| :
done


%files
%defattr(-,root,root,-)
%{_datadir}/icons/elegant
%{_datadir}/icons/hawaii
