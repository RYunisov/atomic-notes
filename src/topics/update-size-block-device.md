# How to update size of a block device without reboot

We often faced a situation to update size of block devices without reboot VM machine.

> Note: The solution verified on Debian-based distributions.

```bash
echo 1 > /sys/block/sd*/device/rescan
```

To check an updated size by tools as `fdisk`, `cfdisk` and etc.

