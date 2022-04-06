################################################################################
#
# worms
#
################################################################################

BUGGY_VERSION = 1.0
BUGGY_SITE = $(BR2_EXTERNAL_SWIS1_PATH)/src/buggy
BUGGY_SITE_METHOD = local

define BUGGY_BUILD_CMDS
$(TARGET_MAKE_ENV) $(MAKE) $(TARGET_CONFIGURE_OPTS) all -C $(@D)
endef
define BUGGY_INSTALL_TARGET_CMDS 
   $(INSTALL) -D -m 0755 $(@D)/bug1 $(TARGET_DIR)/usr/bin 
   $(INSTALL) -D -m 0755 $(@D)/bug2 $(TARGET_DIR)/usr/bin 
   $(INSTALL) -D -m 0755 $(@D)/bug3 $(TARGET_DIR)/usr/bin 
endef
WORMS_LICENSE = Proprietary

$(eval $(generic-package))
