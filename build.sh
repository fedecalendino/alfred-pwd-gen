function build() {
  echo "Cleaning workspace"
  echo

  rm -rf "./bin/"

  echo "Generating binary file for $1"
  echo

  poetry run pyinstaller --onedir --paths ./src/ "src/$1.py" 1> /dev/null
  mv "./dist/$1/" "./bin/"
  echo

  echo "Cleaning up temporary files..."
  rm "./$1.spec"
  rm -rf "./build/"
  rm -rf "./dist/"

  echo
	echo "Finished generating bin file for $1"
}

build main

