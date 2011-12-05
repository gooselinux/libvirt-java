Summary:    Java bindings for the libvirt virtualization API
Name:       libvirt-java
Version:    0.4.5
Prefix:     libvirt
Release:    2%{?dist}
License:    LGPLv2+
BuildArch:  noarch
Group:      Development/Libraries
Source:     http://libvirt.org/sources/java/%{name}-%{version}.tar.gz
URL:        http://libvirt.org/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root

# https://bugzilla.redhat.com/show_bug.cgi?id=582294
# extraneous CopyOf from java-1.6 broke that release
Patch0:     libvirt-java-0.4.5-copy-of.patch

Requires:   jna
Requires:   libvirt-client >= 0.8.1
Requires:   java >= 1.5.0
Requires:   jpackage-utils
BuildRequires:  ant
BuildRequires:  jna
BuildRequires:  ant-junit
BuildRequires:  java-devel >= 1.5.0
BuildRequires:  jpackage-utils

#
# the jpackage-utils should provide a %{java_home} macro
# to select a different Java JVM from the default one use the following
# rpmbuild --define 'java_home /usr/lib/jvm/your_jvm_of_choice'
#

%description
Libvirt-java is a base framework allowing to use libvirt, the virtualization
API though the Java programming language.
It requires libvirt-client >= 0.8.1

%package    devel
Summary:    Compressed Java source files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description    devel
Libvirt-java is a base framework allowing to use libvirt, the virtualization
API though the Java programming language. This is the development part needed
to build applications with Libvirt-java.


%package    javadoc
Summary:    Java documentation for %{name}
Group:      Development/Documentation
Requires:   jpackage-utils

%description    javadoc
API documentation for %{name}.
%prep
%setup -q
%patch0 -p1

%build
ant build docs

%install
rm -fr %{buildroot}
install -d -m0755 %{buildroot}%{_javadir}
install -d -m0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp target/%{prefix}-%{version}.jar %{buildroot}%{_javadir}
%{__ln_s} %{_javadir}/%{prefix}-%{version}.jar %{buildroot}%{_javadir}/%{prefix}.jar 
cp -r target/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{_javadocdir}/%{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%check
ant test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README INSTALL
%{_javadir}/*.jar

%files devel
%defattr(-,root,root)
%doc src/test/java/test.java


%files javadoc
%defattr(-,root,root)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Thu Jul  8 2010 Daniel Veillard <veillard@redhat.com> - 0.4.5-2
- extraneous CopyOf from java-1.6 broke the release on old java versions
- Resolves: rhbz#582294

* Tue Jun 29 2010 Daniel Veillard <veillard@redhat.com> - 0.4.5-1
- rebase to 0.4.5
- Added libvirt support up to 0.8.1 API
- Improved packaging for javadocs
- Better Free/Close handling
- Resolves: rhbz#582332

* Wed May 26 2010 Deepak Bhole <dbhole@redhat.com> - 0.4.2-3
- Remove epoch from the java 1.5.0 requirements

* Thu Apr 15 2010 Daniel Veillard <veillard@redhat.com> - 0.4.2-2
- Missing /usr/share/javadoc/libvirt symlink
- Resolves: rhbz#579037
- Allow libvirt-java build on all architecture, lower require to java >= 1.5
- Resolves: rhbz#582294

* Tue Feb  2 2010 Daniel Veillard <veillard@redhat.com> - 0.4.2-1
- update to upstream 0.4.2
- fix a crash in getSchedulerParameters()
- Resolves: rhbz#560658

* Wed Jan 20 2010 Daniel Veillard <veillard@redhat.com> - 0.4.1-1
- update to upstream 0.4.1
- better scheduler parameters checking and error reporting 
- Resolves: rhbz#557066

* Mon Jan 11 2010 Daniel Veillard <veillard@redhat.com> - 0.4.0-1
- update to 0.4.0
- Modified the dependency to be libvirt-client instead of libvirt.
- Added libvirt APIs up through 0.7.0
- Added maven building tools.
- Fixed connection and domain bugs found by Thomas Treutner
- Resolves: rhbz#554348

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.3.0-1.1
- Rebuilt for RHEL 6

* Wed Jul 29 2009 Bryan Kearney <bkearney@redhat.com> - 0.3.0-1
- refactored the code to use jna (https://jna.dev.java.net/)
    
* Fri Jul 18 2008 Daniel Veillard <veillard@redhat.com> - 0.2.0-1
- new release 0.2.0
- finished cleanup of APIs

* Thu Jul  3 2008 Daniel Veillard <veillard@redhat.com> - 0.1.2-1
- new release 0.1.2

* Tue Jul  1 2008 Daniel Veillard <veillard@redhat.com> - 0.1.1-1
- new release 0.1.1

* Tue Jun 24 2008 Daniel Veillard <veillard@redhat.com> - 0.1.0-1
- created

