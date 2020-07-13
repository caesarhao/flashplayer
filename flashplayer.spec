Name:           flashplayer
Version:        32.0.0.387
Release:        7%{?dist}
Summary:        Adobe flash player and debugger

License:        Public Domain and MIT
URL:            https://github.com/caesarhao/flashplayer
Source0:        https://github.com/caesarhao/flashplayer/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  
BuildArch:      noarch

%description
The mailcap file is used by the metamail program.  Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material.  Basically, mailcap associates a particular type of file
with a particular program that a mail agent or other program can call
in order to handle the file.  Mailcap should be installed to allow
certain programs to be able to handle non-text files.

Also included in this package is the mime.types file which contains a
list of MIME types and their filename "extension" associations, used
by several applications e.g. to determine MIME types for filenames.

%package     -n nginx-mimetypes
Summary:        MIME type mappings for nginx
License:        Public Domain
Requires:       nginx-filesystem

%description -n nginx-mimetypes
MIME type mappings for nginx.


%prep
%setup -q


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install sysconfdir=%{_sysconfdir} mandir=%{_mandir}


%check
make check


%files
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/mailcap
%config(noreplace) %{_sysconfdir}/mime.types
%{_mandir}/man4/mailcap.*

%files -n nginx-mimetypes
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/nginx/mime.types


%changelog
* Mon Jul 13 2020 Hao Zhang <caesarhao@gmail.com>
- update spec file

* Sun Jul 12 2020 Hao Zhang <caesarhao@gmail.com>
- made a noarch package

