# How to check type of linked libraries

* Use `file` util

If you check output, you can see `dynamically linked`. It means binary use dynamic library

```bash
$ file /usr/local/bin/virtiofsd
# OUTPUT
# /usr/local/bin/virtiofsd: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=cc1ae0ebccbe96dbd7d7012980b00bf76311fc08, with debug_info, not stripped
```

* To check libraries and where is pointed use `ldd` util

Libs which linking with => will use shared lib(dynamic). Also user can rewrite it use env `LD_LIBRARY_PATH`

```bash
ldd /usr/local/bin/virtiofsd

# OUTPUT
# linux-vdso.so.1 (0x00007ffecf1f8000)
# libseccomp.so.2 => /lib/x86_64-linux-gnu/libseccomp.so.2 (0x00007f20719ef000)
# libcap-ng.so.0 => /lib/x86_64-linux-gnu/libcap-ng.so.0 (0x00007f20719e7000)
# libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f20719cc000)
# librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f20719c2000)
# libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f207199f000)
# libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f2071850000)
# libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f2071848000)
# libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f2071656000)
# /lib64/ld-linux-x86-64.so.2 (0x00007f2071c04000)
```

* Case with `statically linked`

```bash
$ file ../helmsman 
../helmsman: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=giKpqB_eEQ4pCsw_zwab/HXVXhwhlCd8onwlovFAY/b_HNul8q2i32pIwivh31/vGA8O26tkLqxQW-WXnoN, stripped

$ ldd ../helmsman 
not a dynamic executable
```

