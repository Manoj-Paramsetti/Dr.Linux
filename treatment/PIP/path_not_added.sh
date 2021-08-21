#!/bin/bash
# ['no_sudo', 'write']

echo -e "\n" >> $HOME/.bashrc
echo "# Exporting pip library binary files" >> $HOME/.bashrc
echo 'export PATH=$HOME"/.local/bin/":$PATH' >> $HOME/.bashrc

echo "PATH is updated"
echo "Issue solved"
