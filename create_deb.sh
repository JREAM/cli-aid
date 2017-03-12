#!/bin/sh
set -e

make-deb
cd debian

cat > postinst <<- EOM
#!/bin/bash

echo "Setting up symlink to cli_aid"
ln -sf /usr/share/python/cli_aid/bin/cli_aid /usr/local/bin/cli_aid
EOM
echo "Created postinst file."

cat > postrm <<- EOM
#!/bin/bash

echo "Removing symlink to cli_aid"
rm /usr/local/bin/cli_aid
EOM
echo "Created postrm file."

for f in *
do
    echo "" >> $f;
done

echo "INFO: debian folder is setup and ready."
echo "INFO: 1. Update the changelog with real changes."
echo "INFO: 2. Run:\n\tvagrant provision || vagrant up"
