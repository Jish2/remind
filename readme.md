### installation

run `./install.sh`

```
bash ./install.sh
```

alternatively, cherry pick the steps if you already have some

install `reminders-cli`

```
brew install keith/formulae/reminders-cli
```

add alias (optional, replace with your path and command)

```
echo "alias remind=\"python ~/documents/projects/github/remind/main.py/\"" >> ${ZDOTDIR:-$HOME}/.zshrc
```

### roadmap

- [ ] add cli args
- [ ] show low priority tasks with flag (`-l`)
