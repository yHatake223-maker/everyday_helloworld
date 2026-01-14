unable to access '/Users/xxx/.gitconfig': Is a directory
fatal: unknown error occurred while reading the configuration files
error: cannot run editor: No such file or directory

These errors indicate that Git cannot read your global config properly.

## How to detect .gitconfig being a directory
Run the following command:
```bash
ls -ld ~/.gitconfig
```

Expected result (file):
-rw-r--r--  1 user  staff  ... ~/.gitconfig

Problematic result (directory):
drwxr-xr-x  2 user  staff  ... ~/.gitconfig

If .gitconfig is a directory, Git cannot read it.

## Safe recovery steps

⚠️ These steps only affect your local environment.

1. Backup the existing directory (if any):
```bash
mv ~/.gitconfig ~/.gitconfig.backup
```
2. Create a fresh config file:
```bash
touch ~/.gitconfig
```

3. (Optional) Reconfigure basic settings:
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## Verification commands
Run the following commands and confirm no errors appear:
```bash
git --version
git config --global --list
```

If these commands run without errors, your Git config is fixed.