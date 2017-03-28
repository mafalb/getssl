Name:           getssl
Version:        2.10
Release:        1%{?dist}
Summary:        Obtain SSL certificates from the letsencrypt.org ACME server.
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%if 0%{?rhel} == 5
Group:          Applications/Internet
%endif

License:        GPLv3
URL:            https://github.com/srvrco/getssl
Source0:        %{name}-%{version}.tar.gz
#Patch0:         %{name}-libexec.patch
#Patch1:         %{name}-nosni.patch

Requires:       curl, bind-utils

%description

Obtain SSL certificates from the letsencrypt.org ACME server.  Suitable for automating the process on remote servers.

Features:

- Bash - It runs on virtually all linux machines, including BSD, Slackware, MAC OSX.
- Get certificates for remote servers - The tokens used to provide validation of domain ownership, and the certificates themselves can be automatically copied to remote servers (via ssh, sftp or ftp for tokens). The script doesn't need to run on the server itself. This can be useful if you don't have access to run such scripts on the server itself, as it's a shared server for example.
- Runs as a daily cron - so certificates will be automatically renewed when required.
- Automatic certificate renewals
- Checks certificates are correctly loaded. After installation of a new certificate it will test the port specified ( see [Server-Types](#server-types) for options ) that the certificate is actually being used correctly.
- Automatically updates - The script can automatically update itself with bug fixes etc if required.
- Extensively configurable - With a simple configuration file for each certificate it is possible to configure it exactly for your needs, whether a simple single domain or multiple domains across multiple servers on the same certificate.
- Supports http and dns challenges - Full ACME implementation
- Simple and easy to use
- Detailed debug info - Whilst it shouldn't be needed, detailed debug information is available.
- Reload services - After a new certificate is obtained then the relevant services (e.g. apache/nginx/postfix) can be reloaded.

%prep
%setup -q
%if 0%{?rhel} == 5
mv -f getssl-nosni getssl
%endif

%build

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT make install
#mkdir -p $RPM_BUILD_ROOT/usr/bin
#mkdir -p $RPM_BUILD_ROOT/usr/libexec
#cp getssl create-getssl-config $RPM_BUILD_ROOT/usr/bin
#cp -r dns_scripts $RPM_BUILD_ROOT/usr/libexec/

%files

%defattr(0644, root, root)
%doc LICENSE
%doc README.md

%defattr(0755, root, root)
%_bindir/getssl
%_libexecdir/%{name}/dns_scripts
%_libexecdir/%{name}/other_scripts

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 28 2017 Markus Falb <rpm@mafalb.at> - 2.10
- Bump version to 2.10
* Thu Oct 20 2016 Markus Falb <rpm@mafalb.at> - 1.61
- Build rpm

