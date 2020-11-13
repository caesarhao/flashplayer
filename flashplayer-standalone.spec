Name:           flashplayer-standalone
Version:        32.0.0.453
Release:        1%{?dist}
Summary:        Adobe flash player standalone, debugger and flashlcu (local content update)

License:        Public Domain and MIT
URL:            https://github.com/caesarhao/flashplayer-standalone
Source0:        https://github.com/caesarhao/flashplayer/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildArch:      x86_64

%description
flashplayer standalone version and the debugger

%changelog
* Mon Jul 13 2020 Hao Zhang <caesarhao@gmail.com>
- update spec file

* Sun Jul 12 2020 Hao Zhang <caesarhao@gmail.com>
- made a noarch package


