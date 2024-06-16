# install reminders-cli
brew install keith/formulae/reminders-cli

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# add alias to .zshrc 
echo "alias remind=\"python $DIR/main.py\"" >> ${ZDOTDIR:-$HOME}/.zshrc