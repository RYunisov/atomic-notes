# Libvirt

Linux virtualization tool

## Tips

List of domain

```bash

# virsh list --all

```

Update config of VM

```bash

# virsh edit <VM>

```

Clone VM

> Note: VM have to stopped

```bash

# virt-clone --original <name_of_vm> --name <name_of_vm> --file <new_path_to_image_vm>

```

Extend disk on the fly

> Shutdown VM isn't require

- Identify disk, which do you want to extend

```bash

# virsh domblklist <name_of_vm>
 Target   Source
--------------------------------
 vda      /volumes/disk01.qcow2

```

- Using name for `Target` and `VM name` define a new size.

> Usually `size` define in KB

```bash

# virsh blockresize <name_of_vm> vda 500G
Block device 'vda' is resized

```

- Check updated size

```bash

# qemu-img info /volumes/disk01.qcow2 --force-share

```

## Troubleshouting

Case 01. In during starting VM in `cockpit-ui` or `Terraform` deploy `Libvirt` return error:

- System information:
  - Ubuntu 20.04
  - Apparmor
  - Libvirt

```bash

libvirtd[18883]: internal error: qemu unexpectedly closed the monitor: 2023-03-27T11:31:54.139065Z qemu-system-x86_64: -blockdev {"driver":"file","filename":"/volumes/disk01.qcow2","node-name":"libvirt-1-storage","auto-read-only":true,"discard":"unmap"}: Could not open '/volumes/disk01.qcow2': Permission denied

```

Just update `Apparmor` template: `/etc/apparmor.d/libvirt/TEMPLATE.qemu`

Example fix:

```bash

#include <tunables/global>

profile LIBVIRT_TEMPLATE flags=(attach_disconnected) {
  #include <abstractions/libvirt-qemu>
  "/volumes/{,**}" rwk, # <- Add the line
}

```
