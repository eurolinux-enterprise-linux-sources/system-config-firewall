sconfdir = $(sysconfdir)/sysconfig
dist_sconf_DATA = ${PACKAGE_NAME}

desktop_FILES = ${PACKAGE_NAME}.desktop.in
desktopdir = $(datadir)/applications
dist_desktop_DATA = $(desktop_FILES:.in=)

pam_FILES = ${PACKAGE_NAME}.pam
pamdir = $(sysconfdir)/pam.d
if USE_USERMODE
pam_DATA = $(pam_FILES)
endif

console_FILES = ${PACKAGE_NAME}.console
if USE_USERMODE
consoledir = $(sysconfdir)/security/console.apps
console_DATA = $(console_FILES)
endif

polkit0_policy_FILES = org.fedoraproject.config.firewall.0.policy.in
if USE_POLICYKIT0
polkit0_policydir = $(datadir)/PolicyKit/policy
dist_polkit0_policy_DATA = $(polkit0_policy_FILES:.in=)
endif

polkit1_action_FILES = org.fedoraproject.config.firewall.policy.in
if USE_POLICYKIT1
polkit1_actiondir = $(datadir)/polkit-1/actions
dist_polkit1_action_DATA = $(polkit1_action_FILES:.in=)
endif

if USE_DBUS
dbus_policydir = $(sysconfdir)/dbus-1/system.d
dist_dbus_policy_DATA = org.fedoraproject.Config.Firewall.conf

dbus_servicedir = $(datadir)/dbus-1/system-services
dist_dbus_service_DATA = org.fedoraproject.Config.Firewall.service
endif

@INTLTOOL_DESKTOP_RULE@
@INTLTOOL_POLICY_RULE@

all: $(dist_desktop_DATA) $(dist_polkit0_policy_DATA) $(dist_polkit1_action_DATA)

CLEANFILES = *~ *\# .\#*

DISTCLEANFILES = \
	$(dist_desktop_DATA) \
	$(dist_polkit0_policy_DATA) \
	$(dist_polkit1_action_DATA)

EXTRA_DIST = \
	$(pam_FILES) \
	$(console_FILES) \
	$(desktop_FILES) \
	$(polkit0_policy_FILES) \
	$(polkit1_action_FILES)
