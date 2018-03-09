Thanks for downloading this Pine64 Debian image from
us at https://www.pine64.pro/.

Please remember to resize your rootfs by executing
the following via terminal on first boot.

sudo -i
resize_rootfs.sh
reboot

Also to keep up to date with the latest kernels and
uboot version simply execute teh following via terminal

sudo -i
pine64_update_uboot.sh
pine64_update_kernel.sh
reboot

For those of you who have the bluetooth/wifi module
please active the Bluetooth Service via terminal by
executing the following

sudo -i
systemctl enable bluetooth-module.service
reboot

Remember to check out our community and latest tutorials.
We also have a thriving community on irc which can be
reached at https://www.pine64.pro/chat/.

Lenny Raposo
