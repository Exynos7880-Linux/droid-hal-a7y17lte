%define device a7y17lte
%define vendor samsung
%define vendor_pretty SAMSUNG
%define device_pretty Samsung A7 2017
%define droid_target_aarch64 1
%define installable_zip 1
%define enable_kernel_update 1

%define android_config \
#define MALI_QUIRKS 1\
%{nil}

%define makefstab_skip_entries / /system_root /system

%define straggler_files \
/bugreports\
/d\
/product_services\
/vendor\
/vendor_service_contexts\
/product\
/sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc

