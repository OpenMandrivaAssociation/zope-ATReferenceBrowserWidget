%define Product ATReferenceBrowserWidget
%define product atreferencebrowserwidget
%define name    zope-%{Product}
%define version 2.0.1
%define release %mkrel 1

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    ATReferenceBrowserWidget is an add-on to Archtetypes
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:   zope >= %{zope_minver}
Requires:   zope-Archetypes
BuildArch:  noarch

%description
ATReferenceBrowserWidget is an add-on to Archtetypes. It adds a new reference
widget that allows you to search or browse the portal when creating references.
This new widget inherits from the standard reference widget so you can use all
it's properties.For now, the addable feature has not been implemented/activated
but that's not difficult. The only reason I haven't so far is that I have
my doubts for it's usefulness. But of course, I can be wrong ;-)

When you use this widget, there are two buttons presented for each widget. One
that opens a popup-window that let's you do the search/browsing and one that
let's you clear the reference or selected references (will be in effect after
the form's Save). 

The popop window basically consists of two parts. The top half is a search form
and the bottom half is the browser/search results part. Both parts can be 
turned off or on using the widget's properties.

The search part has additional configuration in the widget (see properties
below).

Properties

    The popup window can be configured using the following widget properties:

    * default_search_index: when a user searches in the popup, this index is
used by default

    * show_indexes: in the popup, when set to True, a drop-down list is shown
with the index to be used for searching. If set to False, default_search_index
will be used.

    * size: in case of single-select widget, the default is set to 30. In case
of multi-select, default is 8.

    * available_indexes: optional dictionary that lists all the indexes that 
can be used for searching. Format: {'<catalog index>':'<friendly name'>, ... } 
The friendly name is what the end-users sees to make the indexes more sensible
for him. If you do not use this property then all the indexes will be shown (I 
think nobody should allow this to happen!).

    * allow_search: shows the search section in the popup
    
    * allow_browse: shows the browse section in the popup
    
    * startup_directory: directory where the popup opens. Optional. When
omitted, the current folder is used
      
    * force_close_on_insert: closes the popup when the user choses insert. This
overrides the behavior in multiselect mode.
    * base_query: defines query terms that will apply to all searches, mainly
useful to create specific restrictions when allow_browse=0.  Can be either a
dictonary with query parameters, or the name of a method or callable available
in cotext that will return such a dictionary.
    
This add-on comes with an example content type that uses this widget. You can
enable the installation
of the type by uncommenting the appropriate line in Install.py under Extension.
See ATReferenceBrowserDemo.py.



%prep
%setup -c -q 

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/

%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
