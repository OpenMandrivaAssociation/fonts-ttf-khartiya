%define pkgname khartiya-ttf

Summary:	Extended Bitstream Charter font
Name:		fonts-ttf-khartiya
Version:	0.4
Release:	%mkrel 1
License:	OFL
Group:		System/Fonts/True type
URL:		http://code.google.com/p/khartiya/
Source0:	http://khartiya.googlecode.com/files/%{pkgname}-%{version}.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
These fonts are based on Bitstream Charter font which was released by Bitstream
for X Window System. They are extended by addition of Cyrillic letters.

%prep
%setup -q -c -n %{pkgname}-%{version}
dos2unix OFL-FAQ.txt

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/khartiya

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/khartiya
ttmkfdir %{buildroot}%{_xfontdir}/TTF/khartiya -o %{buildroot}%{_xfontdir}/TTF/khartiya/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/khartiya/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/khartiya \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-khartiya:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FontLog.txt OFL.txt OFL-FAQ.txt
%dir %{_xfontdir}/TTF/khartiya
%{_xfontdir}/TTF/khartiya/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/khartiya/fonts.dir
%{_xfontdir}/TTF/khartiya/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-khartiya:pri=50
